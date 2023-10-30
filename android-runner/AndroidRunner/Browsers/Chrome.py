from .Browser import Browser


class Chrome(Browser):
    def __init__(self):
        # https://stackoverflow.com/a/28151563
        super(Chrome, self).__init__('com.android.chrome', 'com.google.android.apps.chrome.IntentDispatcher')

