import random as random

class CodeBook():
    wheels = [1, 2, 3, 4, 5]
    _alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    @classmethod
    def line(cls):
        res = ''
        res += ','.join( str(e) for e in random.sample(cls.wheels, 3) )
        res += ';'
        res += ','.join( str(random.randint(0, 25)) for _ in range(3) )
        res += ';'
        no_pairs = random.randint(4, 13)
        letter_list = random.sample(cls._alfa, no_pairs*2)
        # for i in (0, len(letter_list), 2):
        res += ','.join( letter_list[i]+letter_list[i+1] for i in range(0, len(letter_list)-1, 2) )
        res += ';'
        return res

    @classmethod
    def create(cls, filename, no=100, seed=None):
        if filename[-4:] != '.txt':
            filename += '.txt'
        if seed:
            random.seed(seed)
        with open(filename, 'w') as fl:
            for _ in range(no):
                # fl.write(CodeBook.line()) # nie dziala mi newline z dodaniem \n
                # fl.write('/n')
                print(CodeBook.line(), file=fl)

def UI():
    pass

if __name__=="__main__":
    CodeBook.create('code_book', 150, 'asdakwjdkaw98')