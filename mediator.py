from codeBook import CodeBook
from theMachine import get_code_from_book, setup_by_code, TheMachine
from cryptingElems import WrongLetterPair, WrongInput

_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
'''
what do we need here
a set of methods that will communicate between user interface and out set of functions
so, we choose a few operations that will be allowed 
as implement them as safe as possible
with exception catching

methods:
    creating machine
        creating machine from book -> give book and number
        creating machine from parameters (? rly?) -> quite complicated
    creating code book
        create code book and write as txt
    

'''
Machine_built = 0

def create_code_book(no=100, filename=None, seed=None):
    # writes a book of n codes into file
    CodeBook(no, filename, seed)
    return 0

def setup_machine_from_book(n, name):
    # builds machine according to code number n in the book
    if not isinstance(n, int) or n < 0:
        raise IncorrectNumber('code number must be integer greater than zero') 
    code = get_code_from_book(n, name)  # throws CodeBookError
    Machine = setup_by_code(code)       # throws MachineSetupError

# setup machine by hand. So we'll have to provide rotor nums, positions and letter pairs

# def build_machine(rotor_choice, rotor_pos, letters_plugged=None): 
#     # input: tuple(3), tupe(3), [list of letter pairs]
#     try:
#         Machine = TheMachine(rotor_choice=rotor_choice, rotor_pos=rotor_pos, letters_plugged=letters_plugged)
#     except WrongLetterPair:
#         raise IncorrectInputValue('check letter pairs provided')
#     except RotorChooseError:
#         pass
#     except RotorSetupError:
#         pass
#     except PlugBoardError:
    # print('executed')



class IncorrectInputError(Exception):
    pass

class IncorrectNumber(IncorrectInputError):
    pass

class IncorrectInputSize(IncorrectInputError):
    pass

class IncorrectInputValue(IncorrectInputError):
    pass

def test():
    build_machine((1,5,2), (0,24,1), ['aa'])

if __name__=="__main__":
    create_code_book()