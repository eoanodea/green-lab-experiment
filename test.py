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

appium_server_url = 'http://localhost:4723'
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 6',
    appPackage='com.android.chrome',
    appActivity='com.google.android.apps.chrome.Main',
    language='en',
    locale='US',
    chromedriverExecutableDir='/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac',
    chromedriverUseSystemExecutable=True,
)   


# /Users/eoan/Sites/vu/green-lab/test-extension.crx
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5000)


driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Accept & continue"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//*[@text="No thanks"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//*[@text="No thanks"]').click()
time.sleep(5)



driver.execute_script('document.title')

# javascript_code = """
#     // Your JavaScript code here
#     document.body.style.backgroundColor = 'red';
#     //var element = document.getElementById('elementId'); // Replace with the actual element you want to interact with
#     //element.click(); // Example interaction with the element
# """

# Execute the JavaScript code in the context of the web page
# driver.execute_script(javascript_code)


# Close the driver when done
driver.quit()
# PATH_TO_CSV = "urls.csv"
# BUTTON1_X = 556.5
# BUTTON1_Y = 2216.9

# BUTTON2_X = 129.1
# BUTTON2_Y = 2256.9

# BUTTON3_X = 597.5
# BUTTON3_Y = 1785.7

# import os
# import time

# def process(url):

#     adbCommand1 = f"adb shell am start -a android.intent.action.VIEW -d {url}"
    
#     #command to clear the Chrome application data
    # adbCommand2 = "adb shell pm clear com.android.chrome"

#     os.system(adbCommand1)
#     time.sleep(1.5)
    
#     #disable the Chrome welcome screen
#     os.system("adb shell input tap %d %d" % (BUTTON1_X, BUTTON1_Y))
#     time.sleep(0.5)
#     time.sleep(0.5)
#     os.system("adb shell input tap %d %d" % (BUTTON2_X, BUTTON2_Y))
#     time.sleep(0.5)
#     os.system("adb shell input tap %d %d" % (BUTTON3_X, BUTTON3_Y))

#     #wait for the page to load
#     time.sleep(8)

#     os.system(adbCommand2)

# os.system("adb shell pm clear com.android.chrome")

# #loading the urls from csv line by line
# with open(PATH_TO_CSV, "r") as file:
#     for line in file:
#         url = line.strip()
#         process(url)
