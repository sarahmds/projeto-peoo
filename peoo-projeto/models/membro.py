import json

class Membro:
    def __init__(self, id, id_grupo, id_perfil):
        self.id = id
        self.id_grupo = id_grupo
        self.id_perfil = id_perfil

    def __str__(self):
        return f"{self.id} - Grupo: {self.id_grupo} - Perfil: {self.id_perfil}"

    def to_dict(self):
        """Converte a instância de Membro para um dicionário."""
        return {
            "id": self.id,
            "id_grupo": self.id_grupo,
            "id_perfil": self.id_perfil
        }

class Membros:
    objetos = []

    @classmethod
    def listar(cls):
        """Retorna todos os membros carregados na lista de objetos."""
        return cls.objetos

    @classmethod
    def salvar(cls):
        """Salva a lista de membros em um arquivo JSON."""
        try:
            with open("membros.json", mode="w") as arquivo:
                json.dump([membro.to_dict() for membro in cls.objetos], arquivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar os membros: {e}")

    @classmethod
    def abrir(cls):
        """Carrega os membros do arquivo JSON para a lista de objetos."""
        cls.objetos = []  # Resetando a lista de objetos
        try:
            with open("membros.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    m = Membro(obj["id"], obj["id_grupo"], obj["id_perfil"])
                    cls.objetos.append(m)
        except FileNotFoundError:
            print("Arquivo 'membros.json' não encontrado. Nenhum membro carregado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de membros. O arquivo pode estar corrompido.")
        except Exception as e:
            print(f"Erro inesperado ao abrir membros: {e}")

    @classmethod
    def gerar_id(cls):
        """Gera o próximo ID disponível baseado nos membros existentes."""
        if not cls.objetos:
            return 1
        else:
            return max(m.id for m in cls.objetos) + 1
