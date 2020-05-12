from cryptingElems import Stator, Barell, PlugBoard
from cryptingElems import PositionInputError, WrongLetterPair # import exceptions

class TheMachine():
    '''
    this class wraps up all the elements
    letter provided to output method will pass through Plug Board, than Barell in both ways and back through Plug Board
    class handles letters in upper and lower case 
    characters other than letters can be provided but will not be encrypted
    '''
    # historical crypting rotors from Enigma I (1-3) and M3 Army (4-5) :
    rotors_seq = { 1:'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 2:'AJDKSIRUXBLHWTMCQGZNPYFVOE', 3:'BDFHJLCPRTXVZNYEIWGAKMUSQO',
                4:'ESOVPZJAYQUIRHXLNFTGKDCMWB', 5:'VZBRGITYUPSDNHLXAWMJQOFECK', 'stator': 'RDOBJNTKVEHMLFCWZAXGYIPSUQ' }
    def __init__(self, rotor_choice=None, rotor_pos=None, letters_plugged=None): # input: tuple(3), tupe(3), [list of letter pairs]
    # init method configures machine according to provided parameters
    # rotor numbers and rotor positions - 3-element lists containing information about wheels to pick and set
    # plug list - list of letter pairs to connect on board
        self.barell = Barell(self.rotors_seq['stator'])
        self.board = PlugBoard()
        if rotor_choice is not None: # check if they duplicate
            if len(rotor_choice) != 3 or len(set(rotor_choice)) != 3:
                raise RotorChooseError('Enigma has 3 rotors that cannot duplicate')
            try:
                for i in rotor_choice:
                    self.barell.add_wheel(self.rotors_seq[int(i)]) 
            except IndexError:
                raise RotorChooseError('rotors to choose: 1:5')

        if rotor_pos is not None:
            try:
                self.barell.set_wheels(rotor_pos)
            except PositionInputError as e:
                raise RotorSetupError('there are 3 rotors, positions 0:25', e) 
            # problem here - why cant i catch this exception? becouse it wouldnt pass information?
                # raise e

        if letters_plugged is not None:
            try:
                self.board = PlugBoard(*letters_plugged)
            except WrongLetterPair as e:
                raise PlugBoardError('error on plug board', e)


    def output(self, letter):
        # method for processing single character
        if not letter.isalpha():            
            return letter
        letter = letter.upper()             # Machine takse care of lowercase characters before passing to elements
        for el in (self.board, self.barell, self.board):
            letter = el.output(letter)
        return letter

    def encrypt(self, text):
        # method for encrypting text
        # imput can contain lower and uppercase letters, numbers, whitespaces and any other syntax
        # machine encrypts letters and outputs in uppercase
        # text formatting and other characters will be preserved
        return ''.join([ self.output(e) for e in text ])

    def encrypt_file(self, input, output=None):
        # method will encrypt text taken from file 
        # assumes that machine is already configured
        # returns result to file given or to file enc_'input_file'
        if output == None:
            output = 'enc_' + input
        try:
            with open(input, 'r') as inp, open(output, 'w') as out:
                for line in inp:
                    print(self.encrypt(line), file=out)
        except FileNotFoundError:
            raise 


def setup_by_code(code):
    # returns TheMachine object configured according to certain code provided as argument
    code = [c.split(',') for c in code[:-1] ] # last is '\n'
    return TheMachine(*code)


def get_code_from_book(no, filename):
    # iterates through text file containing codes until reaching desired number
    try: 
        with open(filename, 'r') as fl:
            for line in fl:
                line_split = line.split(';')
                if len(line_split) != 5:
                    raise CodeBookError('wrong line in codebook')
                print(line_split)
                if line_split[0] == str(no):
                    return line.split(';')[1:]
        raise CodeBookError('code not fount in book '+filename)
    except FileNotFoundError:
        raise CodeBookError('codebook'+filename+'not found')


class MachineSetupError(Exception):
    pass


class RotorChooseError(MachineSetupError):
    pass


class RotorSetupError(MachineSetupError):
    pass


class PlugBoardError(MachineSetupError):
    pass


class CodeBookError(Exception):
    pass

def test():
    starting_pos = (1,2,52,3)
    Machine7 = TheMachine((3,2,4), starting_pos, ['ew','tr','vc'])
    message = Machine7.encrypt('alamaty --512')
    print(message)
    Machine7.barell.set_wheels(starting_pos)
    d_message = Machine7.encrypt(message)
    print(d_message)

# def test1():
#     a = get_code_from_book(89, 'code_book')
#     bb = setup_by_code(a)
#     cc = setup_by_code(a)
#     ms = bb.encrypt('alamaty --512')
#     print(ms)
#     print(cc.encrypt(ms))

# def test2():
#     a = get_code_from_book(3, 'code_book')
#     Machine7 = setup_by_code(a)
#     Machine7.encrypt_file('to_decrypt')

# def test_empty():
#     a = TheMachine()
#     output = a.encrypt('alamaty --512')
#     print(output)
#     a.barell.set_wheels()
#     print(a.encrypt(output))

if __name__=="__main__":
    test()