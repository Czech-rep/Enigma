from cryptingElems import Stator, Barell, PlugBoard

class TheMachine():
    '''
    Class wrapping up all the elements
    letter provided will pass through Plug Board, than Barell in both ways and back through Plug Board
    class handles letters at upper and lower case 
    characters other than letters can be provided but will not be encrypted
    '''
    rotors_seq = { 1:'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 2:'AJDKSIRUXBLHWTMCQGZNPYFVOE', 3:'BDFHJLCPRTXVZNYEIWGAKMUSQO',
                4:'ESOVPZJAYQUIRHXLNFTGKDCMWB', 5:'VZBRGITYUPSDNHLXAWMJQOFECK', 'stator': 'RDOBJNTKVEHMLFCWZAXGYIPSUQ' }
    def __init__(self, rotor_choice=None, rotor_pos=None, letters_plugged=None): # input: tuple(3), tupe(3), [list of letter pairs]
    # method configures machine according to parameters provided - returns machine object
    # rotor numbers and rotor positions - 3-element lists containing info about wheels to pick and set
    # plug list - list of letters to connect on board
        self.barell = Barell(self.rotors_seq['stator'])
        self.board = PlugBoard()
        if rotor_choice is not None:
            assert len(rotor_choice) == 3
            for i in rotor_choice:
                self.barell.add_wheel(self.rotors_seq[int(i)]) 
        if rotor_pos is not None:
            assert len(rotor_pos) == 3
            self.barell.set_wheels(rotor_pos)
        if letters_plugged is not None: # co jesli pusta lista?
            self.board = PlugBoard(*letters_plugged)

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

    # def get_params(self):
    #     # method returs a dict with machine assembly information
    #     assert self.barell.elements 
    #     return {'wheels': len(self.barell.elements), }

    def encrypt_file(self, input, output=None):
        # method will encrypt text in file 
        # assumes that machine is already configured
        # returns result into file with prefix enc
        if output == None:
            output = 'enc_' + input
        with open(input, 'r') as inp, open(output, 'w') as out:
            for line in inp:
                print(self.encrypt(line), file=out)


def setup_by_code(code):
    # returns TheMachine object configured according to certain code provided as argument
    code = [c.split(',') for c in code.split(';')[:-1] ] # tworzy liste stringow
    return TheMachine(*code)

class FileNotFoundError(Exception):
    pass

def get_code_from_book(no, filename):
    # iterates through text file containing codes until reaching desired number
    assert len(filename) > 3
    if filename[-4:] != '.txt':
        filename += '.txt'
    with open(filename, 'r') as fl:
        i = 0
        for line in fl:
            if i == no:
                return line
            i += 1
    raise FileNotFoundError()


def test():
    starting_pos = (1,2,19)
    Machine7 = TheMachine((3,2,4), starting_pos, ['ew','tr','vc'])
    message = Machine7.encrypt('alamaty --512')
    print(message)
    Machine7.barell.set_wheels(starting_pos)
    d_message = Machine7.encrypt(message)
    print(d_message)

def test1():
    a = get_code_from_book(89, 'code_book')
    bb = setup_by_code(a)
    cc = setup_by_code(a)
    ms = bb.encrypt('alamaty --512')
    print(ms)
    print(cc.encrypt(ms))

def test2():
    a = get_code_from_book(3, 'code_book')
    Machine7 = setup_by_code(a)
    Machine7.encrypt_file('to_decrypt')

def test_empty():
    a = TheMachine()
    output = a.encrypt('alamaty --512')
    print(output)
    a.barell.set_wheels()
    print(a.encrypt(output))

if __name__=="__main__":
    test()