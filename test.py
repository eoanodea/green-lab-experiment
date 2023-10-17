#Note: Before executing the script, run the command "adb shell pm clear com.android.chrome" to clear the Chrome application data

# Physical size: 1080x2400
# First Button
# /dev/input/event3: EV_ABS       ABS_MT_POSITION_X    0000022c = 556 = ((556 * 1080) / 1079) = 556.51529194
# /dev/input/event3: EV_ABS       ABS_MT_POSITION_Y    000008a8 = 2216 ((2216 * 2400) / 2399) = 2216.92371822

# Second Button
# /dev/input/event3: EV_ABS       ABS_MT_POSITION_X    00000081 = 129 = ((129 * 1080) / 1079) = 129.11978968
# /dev/input/event3: EV_ABS       ABS_MT_POSITION_Y    000008d0 = 2256 = ((2256 * 2400) / 2399) = 2256.94039266

# Third Button
# /dev/input/event3: EV_ABS       ABS_MT_POSITION_X    00000255 = 597 = ((597 * 1080) / 1079) = 597.51529194
# /dev/input/event3: EV_ABS       ABS_MT_POSITION_Y    000006f9 = 1785 = ((1785 * 2400) / 2399) = 1785.74489371

# import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os
import time

os.system("adb shell pm clear com.android.chrome")
# os.system("adb shell 'echo \"chrome --disable-fre --no-default-browser-check --no-first-run --disable-web-security --ignore-certificate-errors --ignore-urlfetcher-cert-requests\" > /data/local/tmp/chrome-command-line'")
os.system("adb shell am start com.android.chrome --enabl-logging --disable-web-security --ignore-certificate-errors  --allow-insecure-localhost --ignore-urlfetcher-cert-requests")
# os.system("adb shell am start -a android.intent.action.VIEW -d https://www.vu.nl")

# adb shell 'echo --unsafely-treat-insecure-origin-as-secure=http://a.test > /data/local/tmp/chrome-command-line'

# appium_server_url = 'http://localhost:4723'
# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='Pixel 6',
#     appPackage='com.android.chrome',
#     appActivity='com.google.android.apps.chrome.Main',
#     language='en',
#     locale='US',
#     chromedriverExecutableDir='/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac',
#     chromedriverUseSystemExecutable=True,
#     # "appium:options": {
#     #     w3c: False,  # Required to use Appium with ChromeDriver
#     #     args: [
#     #         '--disable-fre',
#     #         '--no-default-browser-check',
#     #         '--no-first-run',a
#     #         '--disable-web-security',
#     #         '--ignore-certificate-errors',
#     #         '--ignore-urlfetcher-cert-requests',
#     #         # Add any additional Chrome options here
#     #     ]
#     # }
# )   

# # adb shell am start \
# #   -a android.intent.action.VIEW \
# #   -n org.chrome.content_shell_apk/.ContentShellActivity \
# #   --es activeUrl "http://chromium.org" \
# #   --esa commandLineArgs --show-paint-rects,--show-property-changed-rects


# # # /Users/eoan/Sites/vu/green-lab/test-extension.crx
# capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


# driver = webdriver.Remote(appium_server_url, options=capabilities_options)
# driver.implicitly_wait(5000)

# url = 'https://vu.nl'
# driver.get(url)


# driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Use without an account"]').click()
# driver.find_element(by=AppiumBy.XPATH, value='//*[@text="No thanks"]').click()




# Close the driver when done
# driver.quit()