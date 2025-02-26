import json

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Contatos:
    contatos = []

    @classmethod
    def listar(cls):
        return cls.contatos

    @classmethod
    def abrir(cls):
        try:
            with open("contatos.json", "r") as f:
                contatos_data = json.load(f)
                for obj in contatos_data:
                    if "nome" in obj and "telefone" in obj:
                        c = Contato(obj["nome"], obj["telefone"])
                        cls.contatos.append(c)
                    else:
                        print("Erro: Dados de contato incompletos.", obj)
        except FileNotFoundError:
            print("Arquivo de contatos não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")

    @classmethod
    def inserir(cls, contato):
        cls.contatos.append(contato)  # Adiciona o novo contato na lista
        
        # Salva a lista de contatos no arquivo JSON
        cls.salvar()

    @classmethod
    def salvar(cls):
        try:
            # Converte a lista de objetos Contato em um formato que pode ser salvo em JSON
            contatos_data = [{"nome": c.nome, "telefone": c.telefone} for c in cls.contatos]
            with open("contatos.json", "w") as f:
                json.dump(contatos_data, f, indent=4)
            print("Contatos salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar os contatos: {e}")
