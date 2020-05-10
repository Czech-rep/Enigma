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

def create_code_book(no=100, seed=None, filename=None):
    # writes a book of n codes into file
    CodeBook(no=no, seed=seed, filename=filename)
    return 0

def setup_machine_from_book(n, name):
    # builds machine according to code number n in the book
    if not isinstance(n, int) or n < 0:
        raise IncorrectNumber('code number must be integer greater than zero') 
    code = get_code_from_book(n, name)
    Machine = setup_by_code(code)

# setup machine by hand. So we'll have to provide rotor nums, positions and letter pairs

def build_machine(rotor_choice, rotor_pos, letters_plugged=None): 
    # input: tuple(3), tupe(3), [list of letter pairs]
    if len(rotor_choice) != 3 or len(rotor_pos) != 3 or len(set(rotor_choice)) != 3:
        raise IncorrectInputSize('machines uses three distinct rotors') 
    if not all( isinstance(a, int) and a>=1 and a<=5 for a in rotor_choice ):
        raise IncorrectInputValue('wrong rotor choice') 
    if not all( isinstance(a, int) and a>=0 and a<=25 for a in rotor_pos ):
        raise IncorrectInputValue('wrong rotor starting position') 
    if letters_plugged is not None and not all( isinstance(pair, str) for pair in letters_plugged ): # pytanie - czy to implikacja?
        raise IncorrectInputValue('letter pairs - wrong syntax') 
    # lets leave rest of checking for PlugBoard class cryptingElements/141
    try:
        Machine = TheMachine(rotor_choice=rotor_choice, rotor_pos=rotor_pos, letters_plugged=letters_plugged)
    except WrongLetterPair:
        raise IncorrectInputValue('check letter pairs provided')

    print('executed')



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
    test()