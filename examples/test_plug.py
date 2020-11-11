import openhtf as htf
# Import this output mechanism as it's the specific one we want to use.
from openhtf.output.callbacks import json_factory
from openhtf.plugs import user_input
# from openhtf.plugs.testPlug import TestPlug  # After install so venv knows about the path
from plug_chamber import ChamberTe1007c # Doesnt need an install

# This is an import from plugs. In my case for this to work
# the path has to be define or install openhtf after the changes
# so that the plug can be part of plugs
# inside openhtf run: "python setup.py install"
# @htf.plug(tester=TestPlug)
# def test_plug(test, tester):
#     messages = ["hola", "hi", "you're welcome"]
#     to_person = ['name_' + str(val) for val in range(3)]  # Generate names
#     for msg, to_  in zip(messages, to_person):
#         rsp_t = tester.sayHello(to_)
#         tester.sendMessage(msg)

# This one since the plug is directly where I'm running
# the test if can be imported without any paths issues.
# I sugges creating plugs in the same location
# Test in the same location and after
# we moved them to the plugs for openHTF
@htf.plug(chamber=ChamberTe1007c)
def test_vdivider(test, chamber):
    messages = ["hola", "hi", "you're welcome"]
    to_person = ['name_' + str(val) for val in range(3)]  # Generate names
    for msg, to_  in zip(messages, to_person):
        rsp_t = chamber.setTemperature(to_)
        chamber.setHumidity(msg)

if __name__ == '__main__':
  # We instantiate our OpenHTF test with the phases we want to run as args.
  # Multiple phases would be passed as additional args, and additional
  # keyword arguments may be passed as well.  See other examples for more
  # complex uses.
  test = htf.Test(test_vdivider) # Names of the tests that I want to
  test.execute(test_start=user_input.prompt_for_test_start())
