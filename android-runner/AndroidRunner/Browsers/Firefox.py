from .Browser import Browser


class Firefox(Browser):
    def __init__(self):
        super(Firefox, self).__init__('org.mozilla.firefox', 'org.mozilla.gecko.BrowserApp')

