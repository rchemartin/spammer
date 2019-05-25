class Error(Exception):
    pass

class CallError(Error):
    def __init__(self, message):
        self.message = message

class InvalidError(Error):
    def __init__(self, message):
        self.message = message