from code_func import *

def test1():
    EnigmaI =  ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 
                'AJDKSIRUXBLHWTMCQGZNPYFVOE', 
                'BDFHJLCPRTXVZNYEIWGAKMUSQO']

    Emachine = TheMachine()
    Emachine.board.fill_dict('aq','fd','yt','gJ','bx','ne')
    Emachine.barell.add_wheel(*EnigmaI)


    Emachine.barell.set_wheels(2,20,20)
    print(Emachine.barell.get_positions())
    a = Emachine.encrypt('alamaty 550 samoloty asaskjdaskafkwajf wakf wakfaw8wa fwakfjaw fkwaj fkwajkfjakwfjawkjfaskfj akwjf wkjf kwasj fkawsjfak sfwa')
    print(Emachine.barell.get_positions())
    print("machine proceses to: " + a + ' ' )

    Emachine.barell.set_wheels(2,20,20)
    print("machine reverses to: " + Emachine.encrypt(a) )


def test2():
    def imienne(fun):
        def pomocnicza(imie):
            return fun() + imie
        return pomocnicza

    @imienne
    def witaj():
        return "witaj "
    
    # powitanie_adama = imienne(witaj,)
    return witaj('adam')







if __name__=="__main__":
    a = test2()
    print( a, "     test ended")