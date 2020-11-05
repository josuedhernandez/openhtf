import openhtf as htf
# Import this output mechanism as it's the specific one we want to use.
from openhtf.output.callbacks import json_factory

from openhtf.plugs import user_input

from openhtf import plugs
# # Import test plug
from openhtf.plugs import test_plug

@htf.plug(tester=test_plug_example.TestPlug.placeholder)
def test_plug(test, tester):
    messages = ["hola", "hi", "you're welcome"]
    to_person = [name + str(val) for val in range(3)]  # Generate names
    for msg, to_  in zip(messages, to_person):
        rsp_t = tester.sayHello(to_)
        tester.sendMessage(msg)

if __name__ == '__main__':
  # We instantiate our OpenHTF test with the phases we want to run as args.
  # Multiple phases would be passed as additional args, and additional
  # keyword arguments may be passed as well.  See other examples for more
  # complex uses.
  test = htf.Test(test_plug)
  test.execute(test_start=user_input.prompt_for_test_start())
  
