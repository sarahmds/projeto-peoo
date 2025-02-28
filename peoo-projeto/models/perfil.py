import json
from models import crud

class Perfil:
    def __init__(self, id, nome=None, telefone=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Telefone: {self.telefone}"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone
        }

    def __eq__(self, other):
        return isinstance(other, Perfil) and self.id == other.id

class Perfis(crud.CRUD):
    @classmethod
    def salvar(cls):
        with open("perfis.json", mode="w") as arquivo:
            # Salva os objetos convertidos para dicionário
            json.dump([perfil.to_dict() for perfil in cls.objetos], arquivo, ensure_ascii=False, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("perfis.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    p = Perfil(obj["id"], obj.get("nome"), obj.get("telefone"))
                    cls.objetos.append(p)
        except FileNotFoundError:
            print("Arquivo 'perfis.json' não encontrado. Criando um novo arquivo.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao abrir o arquivo: {e}")

    @classmethod
    def listar(cls):
        return cls.objetos
