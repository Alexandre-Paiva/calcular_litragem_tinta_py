from self import self


class Comodo:
    __largura: float
    __profundidade: float
    __altura: float
    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property
    def largura(self):
        return self.__largura
    @property
    def profundidade(self):
        return self.__profundidade
    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura )
        except Exception:
            print('O valor de largura informado é inválido')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
              print('O valor de profundidade informado é inválido')
              exit()

# No python, declaramos métodos mágicos com
# duplos underline no inicio é no final do nome do método:
# init é um método construtor
