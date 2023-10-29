from ast import arg
from AndroidRunner.Device import Device
from AndroidRunner.Experiment import Experiment
from typing import Dict
import time
import logging
import requests

server_url = "http://localhost:3000/api/last-received-message"  # Assicurati di usare l'URL corretto

LOGGER = logging.getLogger()

# Dati da inviare come JSON
data = {
    "message": "Questo è un messaggio di esempio in formato JSON."
}

# Impostare gli header per il formato JSON
headers = {'Content-Type': 'application/json'}

# Generally, after every action, we need to wait for the display to update.
# The time to update varies.

def tap(device: Device, x: int, y: int, sleep) -> None:
    device.shell(f'input tap {x} {y}')
    time.sleep(sleep)

def tab(device: Device) -> None:
    device.shell(f'input tap 900 260')
    time.sleep(0.5)
    #device.shell(f'input tap 280 630')
    #time.sleep(0.5)
    device.shell(f'input tap 180 260')
    time.sleep(0.5)


def swipe(device: Device, x1: int, y1: int, x2: int, y2: int, sleep, duration = 1000):
    device.shell(f'input swipe {x1} {y1} {x2} {y2} {duration}')
    time.sleep(sleep)


def tap_notifications(device):
    tap(device,595, 1755, 0.5)

def web(device, app_name):
    print("web", app_name)

    if app_name == "https://www.google.com":
        tap(device, 528, 2173, 0.5)
        tap(device, 568, 1788, 1)
        tap(device, 430, 659, 0.8)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.youtube.com":
        tap(device, 541, 761, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.microsoft.com":
        tap(device, 350, 1804, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.wikipedia.org":
        tap(device, 500, 654, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.wordpress.org":
        tap(device, 846, 424, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.vimeo.com":
        tap(device, 1030, 459, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://bit.ly":
        tap(device, 569, 2061, 1)
        tap(device, 550, 1675, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.adobe.com":
        tap(device, 910, 2286, 1)
        tap(device, 963, 898, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.amazon.com":
        tap(device, 502, 528, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.yahoo.com":
        swipe(device, 569, 1884, 600, 680, 1, 1000)
        tap(device, 529, 1958, 1)
        time.sleep(2)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.europa.eu":
        tap(device, 556, 1536, 1)
        tap(device, 989, 507, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.qq.com":
        tap(device, 904, 650, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.nytimes.com":
        tap(device, 546, 1563, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.gravatar.com":
        tap(device, 381, 1255, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://github.io":
        tap(device, 1025, 381, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://t.me":
        tap(device, 987, 399, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.baidu.com":
        tap(device, 398, 784, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.soundcloud.com":
        tap(device, 565, 2059, 1)
        tap(device, 539, 2242, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.medium.com":
        tap(device, 359, 1427, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.w3.org":
        tap(device, 1050, 655, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.theguardian.com":
        tap(device, 202, 2233, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.forbes.com":
        tap(device, 551, 2031, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.cloudflare.com/":
        tap(device, 522, 2238, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.cnn.com":
        tap(device, 555, 2105, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.bbc.co.uk":
        tap(device, 669, 641, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.netflix.com":
        tap(device, 489, 1222, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.akamai.com/":
        tap(device, 531, 1787, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.xiaomi.com/":
        tap(device, 500, 1800, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.digicert.com/":
        tap(device, 990, 416, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.go.com/":
        tap(device, 500, 780, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.fastly.net/":
        tap(device, 65, 2145, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.bing.com/":
        tap(device, 1006, 398, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.researchgate.net/":
        tap(device, 500, 1000, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.force.com/":
        tap(device, 568, 1010, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.gandi.net/":
        tap(device, 91, 412, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.weibo.com/":
        tap(device, 580, 580, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.skype.com/":
        tap(device, 531, 794, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.reuters.com/":
        tap(device, 500, 1200, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.ntp.org/":
        tap(device, 421, 1362, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://www.comcast.net/":
        tap(device, 94, 419, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://pki.goog/":
        tap(device, 94, 436, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://criteo.com/":
        tap(device, 411, 1070, 1)
        time.sleep(1)
    elif app_name == "https://opera.com/":
        tap(device, 516, 1176, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://intuit.com/":
        tap(device, 72, 432, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://rubiconproject.com/":
        tap(device, 1012, 419, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://taboola.com/":
        tap(device, 1001, 412, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://zemanta.com/":
        tap(device, 512, 1114, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://milanuncios.com/":
        tap(device, 512, 1114, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://appsflyer.com/":
        tap(device, 514, 1114, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://samsung.com/":
        tap(device, 500, 1000, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://adobe.io/":
        tap(device, 500, 1000, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://harvard.edu/":
        tap(device, 500, 1200, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://etsy.com/":
        tap(device, 500, 1500, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://takeaway.com/":
        tap(device, 500, 1500, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://slack.com/":
        tap(device, 500, 1800, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://stackoverflow.com/":
        tap(device, 500, 1800, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://openai.com/":
        tap(device, 500, 1000, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://nvidia.com/":
        tap(device, 500, 800, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)
    elif app_name == "https://riotgames.com/":
        tap(device, 500, 1500, 1)
        time.sleep(0.5)
        tab(device)
        time.sleep(0.5)


def main(device: Device, *args, **kwargs) -> None:
    time.sleep(0.5)
    tap_notifications(device)
    time.sleep(0.5)
    while True:
        response = requests.get(server_url)
        if response.status_code == 200:
            last_received_message = response.json()
            if last_received_message:
                print(f"Ultimo messaggio ricevuto: {last_received_message['timestamp']}: {last_received_message['message']}")
                requests.post("http://localhost:3000/api/mark-message-as-read")
                break 
            else:
                print("no msg")
        else:
            print("Error")
        
        time.sleep(0.05)
    LOGGER.debug(args)
    LOGGER.debug(kwargs)
    experiment: Experiment = args[0]
    current_run: Dict = experiment.get_experiment()
    LOGGER.debug(current_run)
    web(device, args[0].get_experiment()['path'])
    print("finito")
    args[0].stop_run()



