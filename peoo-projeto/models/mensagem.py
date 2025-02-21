from models import crud
import json
class Mensagem():
    def __init__(self, id, usuario_envia, usuario_recebe, grupo_recebe):
        self.id = id
        self.usuario_envia = usuario_envia
        self.usuario_recebe = usuario_recebe
        self.grupo_recebe = grupo_recebe
    def __str__(self):
        return f"{self.id} - {self.usuario_envia} - {self.usuario_recebe} - {self.grupo_recebe}"
class Mensagens(crud):
    @classmethod
    def salvar(cls):
        with open("mensagens.json", mode="w") as arquivo:   
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("mensagens.json", mode="r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:   
                    m = Mensagem(obj["id"], obj["usuario_envia"], obj["usuario_recebe"], obj["usuario_recebe"], obj["grupo_recebe"])
                cls.objetos.append(m)
        except FileNotFoundError:
            pass