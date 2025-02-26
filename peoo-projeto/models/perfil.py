from models import crud
import json

class Perfil():
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id}"

class Perfis(crud.CRUD):
    @classmethod
    def salvar(cls):
        with open("perfis.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("perfis.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    p = Perfil(obj["id"])
                    cls.objetos.append(p)
        except FileNotFoundError:
            pass