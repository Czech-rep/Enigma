from code_func import *


def test1():
    letters =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    EnigmaI =  ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 
                'AJDKSIRUXBLHWTMCQGZNPYFVOE', 
                'BDFHJLCPRTXVZNYEIWGAKMUSQO']

    Emachine = TheMachine()
    Emachine.board.fill_dict('aq','fd','yt','gJ','bx','ne')
    Emachine.barell.add_wheel(*EnigmaI)


    # processed = EE.process('B')
    a = Emachine.encrypt('alamaty 5 adama')
    print("machine proceses to: " + a + ' ' )
    Emachine.barell.set_wheels(9,4,4)
    print("machine reverses to: " + Emachine.encrypt(a) )


def test2():
    code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
    return all( alfa.index(code[i]) == code.index(alfa[i]) for i in range(len(code)) )


if __name__=="__main__":
    a = test1()
    print(a, "     test ended")