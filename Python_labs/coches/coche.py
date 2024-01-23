class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.__costo = 1000

    def __secreto(self):
        print("Metodo privado")

