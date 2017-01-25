from collections import OrderedDict
from fields import Field


class RegistryMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(clsobj, '__tablename__'):
            raise AttributeError("Models must have __tablename__ atribute!")

        if not hasattr(clsobj, '_registry'):
            clsobj._registry = set()

        if clsobj.__tablename__:
            clsobj._registry.add(clsobj)
        return clsobj


class FieldsMeta(RegistryMeta):
    def __new__(cls, name, bases, clsdict):
        fields = [(attr_name, clsdict[attr_name]) for attr_name, attr_cls in clsdict.items() if isinstance(attr_cls, Field)]

        clsdict['fields'] = OrderedDict(fields)

        return super().__new__(cls, name, bases, clsdict)
