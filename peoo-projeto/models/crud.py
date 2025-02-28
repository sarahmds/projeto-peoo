from abc import ABC, abstractmethod
import json

class CRUD(ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = max((c.id for c in cls.objetos), default=0)  
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        return next((c for c in cls.objetos if c.id == id), None)

    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c is not None:
            cls.objetos.remove(c)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c is not None:
            cls.objetos.remove(c)
            cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass
