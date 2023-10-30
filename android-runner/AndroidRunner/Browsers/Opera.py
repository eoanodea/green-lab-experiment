from .Browser import Browser


class Opera(Browser):
    def __init__(self):
        super(Opera, self).__init__('com.opera.browser', 'com.opera.Opera')
