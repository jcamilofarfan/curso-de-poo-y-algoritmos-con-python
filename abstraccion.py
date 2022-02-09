class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llena_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llena_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua en {temperatura}')

    def _añadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()

# se debe pensar el tipo de interfaz para determinar que es publico y que es privado, con el fin de validar si se puede o no acceder a un metodo o atributo.

# la abstraccion es la idea de que una clase no debe ser instanciada, sino que debe ser utilizada como una plantilla para crear objetos.
