import json

class Mensagem:
    def __init__(self, id, usuario_envia, usuario_recebe, grupo_recebe, texto):
        self.id = id
        self.usuario_envia = usuario_envia
        self.usuario_recebe = usuario_recebe
        self.grupo_recebe = grupo_recebe
        self.texto = texto

    def __str__(self):
        return f"{self.id} - {self.usuario_envia} - {self.usuario_recebe} - {self.grupo_recebe}"

class Mensagens:
    mensagens = []

    @classmethod
    def listar(cls):
        return cls.mensagens

    @classmethod
    def remover(cls, mensagem):
        # Remover a mensagem pela ID
        cls.mensagens = [m for m in cls.mensagens if m.id != mensagem.id]

    @classmethod
    def inserir(cls, mensagem):
        # Inserir uma nova mensagem na lista de mensagens
        cls.mensagens.append(mensagem)

    @classmethod
    def abrir(cls):
        # Limpar a lista de objetos antes de carregar novas mensagens
        cls.mensagens = []  # Limpar a lista antes de adicionar novas mensagens
        try:
            with open("mensagens.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    m = Mensagem(obj["id"], obj["usuario_envia"], obj["usuario_recebe"], obj["grupo_recebe"], obj["texto"])
                    cls.mensagens.append(m)  # Adicionar à lista de mensagens
        except FileNotFoundError:
            pass







           