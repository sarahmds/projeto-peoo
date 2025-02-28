import json

class Grupo:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"{self.id} - {self.nome}"

    def to_dict(self):
        """Converte o objeto Grupo para um dicionário."""
        return {
            "id": self.id,
            "nome": self.nome
        }

class Grupos:
    objetos = []

    @classmethod
    def listar(cls):
        """Retorna todos os grupos carregados na lista de objetos."""
        return cls.objetos

    @classmethod
    def inserir(cls, grupo):
        """Adiciona um novo grupo à lista de grupos."""
        cls.objetos.append(grupo)

    @classmethod
    def excluir(cls, grupo):
        """Remove o grupo da lista de objetos."""
        cls.objetos = [g for g in cls.objetos if g.id != grupo.id]

    @classmethod
    def salvar(cls):
        """Salva a lista de grupos em um arquivo JSON."""
        try:
            with open("grupos.json", mode="w") as arquivo:
                json.dump([grupo.to_dict() for grupo in cls.objetos], arquivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar os grupos: {e}")

    @classmethod
    def abrir(cls):
        """Carrega os grupos do arquivo JSON para a lista de objetos."""
        cls.objetos = []  # Resetando a lista de objetos
        try:
            with open("grupos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    g = Grupo(obj["id"], obj["nome"])
                    cls.objetos.append(g)
        except FileNotFoundError:
            print("Arquivo 'grupos.json' não encontrado. Nenhum grupo carregado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de grupos. O arquivo pode estar corrompido.")
        except Exception as e:
            print(f"Erro inesperado ao abrir grupos: {e}")

    @classmethod
    def gerar_id(cls):
        """Gera o próximo ID disponível baseado nos grupos existentes."""
        if not cls.objetos:
            return 1
        else:
            return max(g.id for g in cls.objetos) + 1
