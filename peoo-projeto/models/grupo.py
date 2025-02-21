from models import crud
import json
class Grupo():
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return f"{self.id}"
class Grupos(crud):
    @classmethod
    def salvar(cls):
        with open("grupos.json", mode="w") as arquivo:   
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("grupos.json", mode="r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:   
                    g = Grupo(obj["id"])
                cls.objetos.append(g)
        except FileNotFoundError:
            pass