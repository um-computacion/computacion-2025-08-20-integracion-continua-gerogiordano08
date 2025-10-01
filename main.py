from app import Database
class Principal:
    def __init__(self) -> None:
        self.__lista__ = []
        self.__app__ = Database()
    def suma(self, a, b):
        """ La funcion suma dos argumentos y devuelve el resultado"""
        s = a + b
        self.__lista__ = self.__app__.get("lista")
        if self.__lista__ is not None:
            self.__lista__.append(s)
            self.__app__.set("lista", self.__lista__)
        return s
    def ask(self):
        print("que numeros quieres sumar?")
        pri = input("ingrese numero")
        seg = input("ingrese numero")
        print(self.suma(pri, seg))
    def pr_lista(self):
        """Imprime la lista"""
        self.__lista__ = self.__app__.get("lista") 
        print(self.__lista__, "Lista impresa.")
        
if __name__ == "__main__":
    
    p = Principal()
    while True:
        p.ask()
        br = input("quieres ingresar otros?")
        if br == "n": break
    p.pr_lista()

    

