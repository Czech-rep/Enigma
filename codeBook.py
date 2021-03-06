import random as random

class CodeBook():
    '''
    class for generating a set of random machine settings
    stored in a text file
    assumes that machine consists of barell with 3 wheels (chosen from 5) and a plug board
    '''
    _wheels = [1, 2, 3, 4, 5]
    _alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, no=100, filename=None, seed=None):
        if seed: random.seed(seed)
        self.c_book = self._create(no)
        self.save(filename) if filename else self.save('codebook')

    def _line(self, _i): 
        # function generates single code
        res = str(_i) + ';'
        res += ','.join( str(e) for e in random.sample(self._wheels, 3) )
        res += ';'
        res += ','.join( str(random.randint(0, 25)) for _ in range(3) )
        res += ';'
        no_pairs = random.randint(4, 13)
        letter_list = random.sample(self._alfa, no_pairs*2)
        res += ','.join( letter_list[i]+letter_list[i+1] for i in range(0, len(letter_list)-1, 2) )
        res += ';'
        return res

    def _create(self, no): 
        # function for creating whole codebook with no machine setups
        # will be saved as filename.txt
        return [ self._line(i) for i in range(1,1+no)]

    def save(self, filename):
        with open(filename, 'w') as fl:
            for line in self.c_book:
                print(line, file=fl)


if __name__=="__main__":
    CodeBook()

