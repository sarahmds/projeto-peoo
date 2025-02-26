import json
from models.crud import CRUD

class Grupo():
    def __init__(self, id, nome=None, membros=[]):
        self.id = id
        self.nome = nome
        self.membros = membros

    def __str__(self):
        return f"{self.id} - {self.nome}"

class Grupos(CRUD):
    @classmethod
    def salvar(cls):
        with open("grupos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("grupos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    g = Grupo(obj["id"], obj["nome"], obj["membros"])
                    cls.objetos.append(g)
        except FileNotFoundError:
            pass

            class Grupo:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Grupos:
    grupos = []

    @classmethod
    def listar(cls):
        return cls.grupos

    @classmethod
    def inserir(cls, grupo):
        cls.grupos.append(grupo)

    @classmethod
    def remover(cls, grupo):
        cls.grupos = [g for g in cls.grupos if g.nome != grupo.nome]
