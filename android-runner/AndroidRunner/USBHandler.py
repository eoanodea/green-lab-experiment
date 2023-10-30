import shlex
import subprocess
from .util import ConfigError

class USBHandler(object):
    USB_COMMAND_TIMEOUT_SECONDS = 5

    def __init__(self, usb_handler_config):
        """ Inits an USBHandler instance.

            Parameters
            ----------
            usb_handler_config : dict
                Dictionary containing the keys enable_command, disable_command
                with the enable and disable commands as values, respectively.
        """
        self._usb_enabled = True

        if usb_handler_config == None:
            self.usb_enable_command = None
            self.usb_disable_command = None 
            self._usb_enabled = None
            return

        if usb_handler_config.get("enable_command", None) == None:
            raise ConfigError("Please provide an enable_command for the usb_handler.")

        if usb_handler_config.get("disable_command", None) == None:
            raise ConfigError("Please provide an disable_command for the usb_handler.")

        self.usb_enable_command = usb_handler_config["enable_command"]
        self.usb_disable_command = usb_handler_config["disable_command"]


    def enable_usb(self):
        """ Enables the USB port(s) is non-empty usb_handler_config is given when instantiating the class.

            Please note that Android Runner also calls the device.unplug() at the beginning
            of the experiment and only calls device.plug() at the end of the experiment.
            This only mocks the battery status (so it looks like its unplugged) but it does 
            NOT actually stop charging the device through USB.
            Please take this into account when it seems like enabling the 
            USB port(s) does not seem to work ;).
        
        """
        # Check first whether USB port(s) are "really" disabled otherwise the call in Experiment.cleanup()
        # can result in disabled ports when using same enable and disable command.
        if self._usb_enabled == False:
            self._run_command(self.usb_enable_command)
            self._usb_enabled = True

    def disable_usb(self):
        """ Disables the USB port(s) if non-empty usb_handler_config is given when instantiating the class."""
        if self._usb_enabled == True:
            self._run_command(self.usb_disable_command)
            self._usb_enabled = False

    def _run_command(self, command):
        """ Runs given command

        Parameters
        ----------
        command : string
            Command that needs to be run.
        """
        if command == None:
            return

        proc = subprocess.Popen(shlex.split(command), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            (stdout, stderr) = proc.communicate(timeout=USBHandler.USB_COMMAND_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            raise USBHandlerException("TimeOutError while executing USB command.")

        if stderr:
            err = stderr.decode("ascii")
            raise USBHandlerException(f"Could not execute USB command: {err}")

class USBHandlerException(Exception):
    pass