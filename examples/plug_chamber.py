from openhtf.util import conf
import openhtf.plugs as plugs

# # maybe add a try import visa and raise error if not installed.

class ChamberTe1007c(plugs.BasePlug):

    def __init__(self):
        print(f"Initialized {self.__class__.__name__}")

    def setTemperature(self, to_whom):
        msg = f"Temp Set: {to_whom}"
        print(f"{self.__class__.__name__} 'setTemperature': {msg}")
        return msg

    def setHumidity(self, message):
        msg = f"Hunidity Set: {message}"
        print(f"{self.__class__.__name__} 'setHumidity': {msg}")
        return msg