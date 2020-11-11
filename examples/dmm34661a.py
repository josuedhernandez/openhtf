from openhtf.util import conf
import openhtf.plugs as plugs

# try:
#     import pyvisa
# except:
#     raise ("please install pyvisa")

class dmm34662(plugs.BasePlug):
    def __init__(self, ip, port, *args):
        print("we started")

    def read_voltage(selg, param="DC"):
        print("test")