import logging
from abc import ABC

class Browser(ABC):

    # noinspection PyUnusedLocal
    def __init__(self, package_name, main_activity):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.package_name = package_name
        self.main_activity = main_activity

    def start(self, device):
        self.logger.info('%s: Start' % device.id)
        device.launch_activity(self.package_name, self.main_activity, from_scratch=True, force_stop=True,
                               action='android.intent.action.VIEW')

    def load_url(self, device, url):
        self.logger.info('%s: Load URL: %s' % (device.id, url))
        device.launch_activity(self.package_name, self.main_activity, data_uri=url,
                               action='android.intent.action.VIEW')

    def stop(self, device, clear_data=False):
        self.logger.info('%s: Stop' % device.id)
        device.force_stop(self.package_name)
        if clear_data:
            device.clear_app_data(self.package_name)

    def to_string(self):
        return self.package_name
