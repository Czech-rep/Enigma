from code_func import *


def test1():
    letters =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    EnigmaI =  ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 
                'AJDKSIRUXBLHWTMCQGZNPYFVOE', 
                'BDFHJLCPRTXVZNYEIWGAKMUSQO']
           #'ABCDE'
    aa = [  'BDAEC', 
            'ECDBA']


    EE = Barell()
    wh = Wheel(EnigmaI[0])
    EE + wh
    
    # processed = EE.process('B')
    a = EE.encrypt('alamaty')
    print("machine proceses to: " + a )
    EE.set_wheels()
    print("machine proceses to: " + EE.encrypt(a) )


def test2():
    pass


if __name__=="__main__":
    test1()
    print("     test ended")