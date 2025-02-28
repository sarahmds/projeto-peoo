import json

class Contato:
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.telefone}"

class Contatos:
    objetos = []

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        return next((contato for contato in cls.objetos if contato.id == id), None)

    @classmethod
    def inserir(cls, contato):
        cls.objetos.append(contato)

    @classmethod
    def excluir(cls, contato):
        # Adicionando o método de exclusão que remove o contato pela comparação do id
        cls.objetos = [c for c in cls.objetos if c.id != contato.id]
        cls.salvar()  # Salvar após excluir

    @classmethod
    def salvar(cls):
        try:
            with open("contatos.json", mode="w") as arquivo:
                json.dump([vars(contato) for contato in cls.objetos], arquivo, indent=4)
        except Exception as e:
            print(f"Erro ao salvar os contatos: {e}")

    @classmethod
    def abrir(cls):
        cls.objetos = []  # Resetando a lista de objetos
        try:
            with open("contatos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Contato(obj["id"], obj["nome"], obj["telefone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            print("Arquivo 'contatos.json' não encontrado. Nenhum contato carregado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de contatos. O arquivo pode estar corrompido.")
        except Exception as e:
            print(f"Erro inesperado ao abrir contatos: {e}")
