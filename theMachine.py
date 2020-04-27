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
    def __init__(self,):
        self.barell = Barell()
        self.board = PlugBoard()

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
        res = ''
        for let in text:
            res += self.output(let)
        return res

    def get_params(self):
        # method prints params of the machine
        return f'''
enigma machine codes:
{ (', ').join(wh.get_code() for wh in self.barell.elements) }
stator: 
{ 5 }
'''

    def crypting_params(self):
        pass

    @classmethod
    def assemble_machine(cls, rotor_numbers, rotos_positions, plug_list):
        # method configures machine according to parameters provided - returns machine object
        # rotor numbers and rotor positions - 3-element lists containing info about wheels to pick and set
        # plug list - list of letters to connect on board
        assert len(rotor_numbers) == len(rotos_positions) and len(rotos_positions) <= 5
        new_machine = cls()
        new_machine.barell = Barell(cls.rotors_seq['stator'])
        for i in rotor_numbers:
            new_machine.barell.add_wheel(cls.rotors_seq[int(i)])
        new_machine.barell.set_wheels(rotos_positions)
        new_machine.board = PlugBoard(*plug_list)
        return new_machine

    def encrypt_file(self, input, output=None):
        # method will encrypt text in file 
        # assumes that machine is already configured
        # returns result into file with prefix enc
        if output == None:
            output = 'enc_' + input
        with open(input, 'r') as inp, open(output, 'w') as out:
            for line in inp:
                print(self.encrypt(line), file=out)
    
    @staticmethod
    def get_code_from_book(no, filename):
        # iterates through text file containing codes until desired number
        assert len(filename) > 3
        if filename[-4:] != '.txt':
            filename += '.txt'
        with open(filename, 'r') as fl:
            i = 0
            for line in fl:
                if i == no:
                    return line
                i += 1
        raise TheMachine.NotFoundError

    @classmethod
    def setup_by_code(cls, code):
        code = [c.split(',') for c in code.split(';')[:-1] ] # tworzy liste stringow
        return cls.assemble_machine(*code)

    class NotFoundError(Exception):
        pass


def test():
    starting_pos = (1,2,19)
    Machine7 = TheMachine.assemble_machine((3,2,4), starting_pos, ['ew','tr','vc'])
    message = Machine7.encrypt('alamaty --512')
    print(message)
    Machine7.barell.set_wheels(starting_pos)
    d_message = Machine7.encrypt(message)
    print(d_message)
    print(Machine7.get_params())

def test1():

    a = TheMachine.get_code_from_book(120, 'codebook')
    bb = TheMachine.setup_by_code(a)
    cc = TheMachine.setup_by_code(a)
    ms = bb.encrypt('alamaty --512')
    print(ms)
    print(cc.encrypt(ms))

def test2():
    a = TheMachine.get_code_from_book(3, 'code_book')
    Machine7 = TheMachine.setup_by_code(a)
    Machine7.encrypt_file('to_decrypt')

if __name__=="__main__":
    test2()
