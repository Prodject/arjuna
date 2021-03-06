
class WaitLenientException(BaseException):

    def __init__(self, message):
        super().__init__(message)

class GuiElementNotFound(WaitLenientException):

    def __init__(self, message, locator):
        super().__init__("GuiElement(s) not found using locator: {}. Tool message: {}".format(locator, message))