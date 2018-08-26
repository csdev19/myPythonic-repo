class MiClase:
    def metodo(self):
        return 'metodo de instancia llamado', self
    @classmethod
    def metodoDeClase(cls):
        return 'metodo de clase llamado', cls
    @staticmethod
    def metodoEstatico():
        return 'metodo estatico llamado'



if __name__ == '__main__':
    obj = MiClase()
    print(obj.metodo())
