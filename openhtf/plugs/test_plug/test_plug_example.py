import openhtf.plugs as plugs

# maybe add a try import visa and raise error if not installed.

class TestPlug(plugs.BasePlug):

    def __init__(self):
        print(f"Initialized {self.__name__}")

    def sayHello(self, to_whom):
        msg = f"Hello {to_whom}"
        print(f"{self.__name__} 'sayHello': {msg}")
        return msg

    def sendMessage(self, message):
        msg = f"Hello {message}"
        print(f"{self.__name__} 'sendMessage': {msg}")
        return msg
