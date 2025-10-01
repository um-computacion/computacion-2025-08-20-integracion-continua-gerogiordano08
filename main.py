from app import Database
class Principal:
    def __init__(self) -> None:
        self.__app__ = Database()
        if not self.__app__.get("lista2"):
            self.lista2 = []
            print("Lista NO encontrada")
        else:
            self.lista2 = self.__app__.json_to_list("lista2")
            print("Lista encontrada")
        #    self.__app__.set_list("lista")
    def suma(self, a, b):
        """ La funcion suma dos argumentos y devuelve el resultado"""
        s = {a + b}
        self.lista2.append(s)
        #self.__app__.list_append("lista", s)
        return s
    def ask(self):
        print("que numeros quieres sumar?")
        pri = int(input("ingrese numero"))
        seg = int(input("ingrese numero"))
        print(self.suma(pri, seg))
    def pr_lista(self):
        """Imprime la lista"""
        print(self.lista2)
        #l = self.__app__.get_list("lista")
        #print(l, "Lista impresa.")
    def save_list(self):
        self.__app__.list_to_json('lista2', self.lista2)
        print("lista2 guardada en json con exito!")
        
if __name__ == "__main__":
    
    p = Principal()
    p.pr_lista()
    while True:
        p.ask()
        br = input("quieres ingresar otros?")
        if br == "n": break
    p.pr_lista()
    p.save_list()
    

