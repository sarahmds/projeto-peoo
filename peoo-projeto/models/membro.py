from models import crud
import json

class Membro():
    def __init__(self, id, id_grupo, id_perfil):
        self.id = id
        self.id_grupo = id_grupo
        self.id_perfil = id_perfil

    def __str__(self):
        return f"{self.id} - {self.id_grupo} - {self.id_perfil}"

class Membros(crud.CRUD):
    @classmethod
    def salvar(cls):
        with open("membros.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("membros.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    m = Membro(obj["id"], obj["id_grupo"], obj["id_perfil"])
                    cls.objetos.append(m)
        except FileNotFoundError:
            pass