import time


# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    device.shell('am start -n "com.example.batterymanager_utility/com.example.batterymanager_utility.MainActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER')
    time.sleep(1)
    device.shell('pm clear com.android.chrome')
    time.sleep(5)

