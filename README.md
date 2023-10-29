# 🪴 Green Lab Core Web Vitals Experiment

## ✏️ Description

The purpose of this project is to examine the relationship between Google's (Core Web Vitals metrics)[https://web.dev/explore/learn-core-web-vitals] and energy consumption on an Google Pixel 6. This experiment goes alongside a (research paper)[https://www.overleaf.com/read/snmthytxnrst#1030cc] for the Green Lab module at Vrije Universiteit Amsterdam.

## ✅ Prerequisites

- Raspberry Pi 4 Model B with 4GB of RAM
- Google Pixel 6

The following packages may need to be installed on the Raspberry Pi:

- (mitmproxy)[https://mitmproxy.org/]
- (Node.js)[https://nodejs.org/en/]
- (Python 3)[https://www.python.org/downloads/]
- (ngrok)[https://ngrok.com/]

## 🤔 How to run

This experiment was designed to run on a Raspberry Pi 4 Model B with 4GB of RAM. The Raspberry Pi should be running the latest version of Raspberry Pi OS. To replicate the project, the following steps should be taken:

1. Clone this repository onto the Raspberry Pi
2. Clone the Android Runner in the parent directory of this repository `https://github.com/S2-group/android-runner.git`
3. Install the Android Runner dependencies `cd android-runner && pip3 install -r requirements.txt`
4. Install the python dependencies `pip3 install -r requirements.txt`
5. Install the node depedencies in the receiver directory `cd receiver && npm install`
6. Create 3 ssh sessions to the Raspberry Pi and run the following:
   1. `mitmproxy -s proxy.py`
   2. `node receiver/app.js`
   3. `ngrok http 3000`
7. The `ngrok` window will give you a https url. Copy this URL into the `.env` file.
