import io
import sys
from execute_command import ReadInput


def test_input_file():
    expected_output = '''Created parking of 6 slots
Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1
Car with vehicle registration number "PB-01-HH-1234" has been parked at slot number 2
1,2
Car with vehicle registration number "PB-01-TG-2341" has been parked at slot number 3
2
Slot number 2 vacated, the car with vehicle registration number "PB-01-HH-1234" left the space, the driver of the car was of age 21
Car with vehicle registration number "HR-29-TG-3098" has been parked at slot number 2
null
null
Slot already vacant
null
'''

    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # and redirect stdout.
    filename = "test-input.txt"
    ReadInput(filename).process()

    sys.stdout = sys.__stdout__  # Reset redirect.
    output = captured_output.getvalue()
    exp_arr = expected_output.split("\n")
    act_arr = output.split("\n")
    for i in range(len(exp_arr)):
        assert exp_arr[i] == act_arr[i]


def test_file_invalid_command():
    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # and redirect stdout.
    filename = "test-input.txt"
    command = "testing invalid"
    expected = "Invalid command: " + command
    ReadInput(filename).command(command)

    sys.stdout = sys.__stdout__  # Reset redirect.
    output = captured_output.getvalue().split("\n")
    assert expected == output[0]
