import random

class WheelScrambles(object):
    '''
    class for generating and storing patterns for wheel
    its got 26 combinations
    each combination is different replacement dictionary
    '''
    def __init__(self):
        pass


class CryptingElement(object):
    '''
    class for implementing any crypting elements
    every type has own scramble methos that generates dictionary with replacing letters
    '''
    _alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    def __init__(self):
        # self.
        # self._replacement_dict = self.scramble()
        pass

class ReplacementSet():
    '''
    any element that outputs a scrambled letter
    '''



class Wheel(CryptingElement):
    '''
    class represents encrypting wheel
    its got 26 possible positions
    each posiiton reprezents different letter replacement order
    wheel will generate output for each letter
    '''
    def __init__(self, code, position=0):
        super().__init__()
        assert 0 <= position <= 25
        self._code = code
        self._position = position
        self._foreward = True

    def _foreward_shift(self, letter):
        index = self._position + self._alfa.index(letter)
        if index > 25:
            index -= 26
        return self._alfa[index]

    def _backward_shift(self, letter):
        index = - self._position + self._alfa.index(letter)
        if index < 0:
            index += 26
        return self._alfa[index]

    def click_wheel(self):
        self._position += 1
        if self._position > 25:
            self._position = 0
            return True
        return False

    def set_position(self, n):
        assert 0 <= n <= 25, "invalid position"
        self._position = n

    def output(self, letter):
        letter = self._retreive(letter)
        return letter                             # klikniecie wywuluje maszyna
        
    def _retreive(self, letter):
        '''
        function for replacing letters
        letter always goes through two times: forewards and backwards
        going foreward replaces from alfabet to own code
        going backward replaces from code to alfabet
        mind that rotation of wheel shifts relation of letters
        '''
        if self._foreward:
            self._foreward = False
            letter = self._foreward_shift(letter)
            return self._code[ self._alfa.index(letter) ]
        else:
            self._foreward = True
            letter = self._backward_shift(letter)
            return self._alfa[ self._code.index(letter) ]




class Barell(CryptingElement):
    '''
    Group of wheels
    Letter goes througt them in two directions
    lets make elements a public list, so one can modify it and access members freely
    '''
    elements = []
    def __init__(self, wall_code='RDOBJNTKVEHMLFCWZAXGYIPSUQ'):
        self.elements = []
        self._wall_convol = self._create_wall(wall_code)

    def _create_wall(self, wall_code):
        # for i in range(len(wall_code)):
            # assert wall_code[i] == wall_code[self._alfa.index(wall_code[i])], "invalid wall convolution"
        return Wheel(wall_code, 0)

    def __add__(self, elem):
        if isinstance(elem, Wheel):
            self.elements.append(elem)

    def set_wheels(self, sequence=None):
        if None == sequence:
            for el in self.elements:
                el.set_position(0)
        
    def _operation_click(self):
        for el in self.elements:
            if el.click_wheel() == False:
                break

    def output(self, letter):
        letter = letter.upper()
        for el in (self.elements + [self._wall_convol] + self.elements[::-1]):
            letter = el.output(letter)
        self._operation_click()
        return letter

    def encrypt(self, text):
        res = ''
        for let in text:
            res += self.output(let)
        print(self.elements[0]._position)
        return res
    


def test():
    pass#     "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             #'RDOBJNTKVEHMLFCWZAXGYIPSUQ'
    w = Wheel('EKMFLGDQVZNTOWYHXUSPAIBRCJ',0)
    qq = Barell()
    qq + w

    print(qq.output('z'))
    qq.set_wheels()
    print(qq.output('a'))

if __name__=="__main__":
    # w = Wheel('EKMFLGDQVZNTOWYHXUSPAIBRCJ',0)
    # qq = Barell()
    # print(qq.R_wheel.crypt('z'))
    test()

    print(" finished")

