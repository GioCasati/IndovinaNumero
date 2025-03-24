import random


class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 6
        self._T = self._TMax
        self._segreto = None

    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def segreto(self):
        return self._segreto

    @property
    def T(self):
        return self._T

    def reset(self):
        '''
        Il metodo reset fa il reset di tutti i parametri di gioco a valore iniziale
        :return:
        '''
        self._T = self._TMax
        self._segreto = random.randint(0, self._NMax)

    def play(self, guess):
        '''
        Il metodo confronta un tentativo con il numero da incrementare
        :param guess: user input per indovinare il numero segreto
        :return: 0 se il giocatore ha indovinato, 2 se le vite sono finite, 1 se segreto è più grande, -1 se segreto è più piccolo
        '''
        if guess == self._segreto:
            return 0
        else:
            self._T -= 1
            if self._T == 0:
                return 2
            if guess < self._segreto:
                return 1
            return -1

if __name__ == '__main__':  # in questo modo il codice qua sotto si esegue solo se il file è eseguito in maniera standalone
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(30))
