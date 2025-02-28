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

    def to_dict(self):
        """Converte a instância de Mensagem para um dicionário"""
        return {
            "id": self.id,
            "usuario_envia": self.usuario_envia,
            "usuario_recebe": self.usuario_recebe,
            "grupo_recebe": self.grupo_recebe,
            "texto": self.texto
        }

class Mensagens:
    mensagens = []

    @classmethod
    def listar(cls):
        return cls.mensagens

    @classmethod
    def remover(cls, mensagem):
        cls.mensagens = [m for m in cls.mensagens if m.id != mensagem.id]

    @classmethod
    def inserir(cls, mensagem):
        cls.mensagens.append(mensagem)

    @classmethod
    def abrir(cls):
        cls.mensagens = []  # Limpa a lista de mensagens
        try:
            with open("mensagens.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    m = Mensagem(
                        obj["id"], obj["usuario_envia"], obj["usuario_recebe"], obj["grupo_recebe"], obj["texto"]
                    )
                    cls.mensagens.append(m)
        except FileNotFoundError:
            print("Arquivo 'mensagens.json' não encontrado. Criando um novo arquivo.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de mensagens.")
        except Exception as e:
            print(f"Erro inesperado ao abrir mensagens: {e}")

    @classmethod
    def salvar(cls):
        try:
            # Salva as mensagens convertidas para dicionário
            with open("mensagens.json", mode="w") as arquivo:
                json.dump([m.to_dict() for m in cls.mensagens], arquivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar mensagens: {e}")

    @classmethod
    def gerar_id(cls):
        """Gera o próximo ID disponível baseado nas mensagens existentes"""
        if not cls.mensagens:
            return 1
        else:
            return max(m.id for m in cls.mensagens) + 1







           