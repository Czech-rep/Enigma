import pytest
from theMachine import TheMachine, RotorChooseError, RotorSetupError

# test rotor choice
def test_rotor_number():
    with pytest.raises(RotorChooseError):
        TheMachine( (1,2,3,4), )

def test_rotor_duplicate():
    with pytest.raises(RotorChooseError):
        TheMachine( (1,2,2), )

def test_rotor_correct():
    test_machine = TheMachine( (1,2,5), )
    assert test_machine.barell.elements[2].output_forward('A') == 'V'

# test rotor setup
def test_setup_range():
    with pytest.raises(RotorSetupError):
        TheMachine( (1,3,5), (1,2,33), )
