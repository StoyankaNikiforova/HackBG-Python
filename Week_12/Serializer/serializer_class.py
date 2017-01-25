from filds import Field


class DeclarativeSerializerMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = {}

        for attr, value in clsdict.items():
            if not isinstance(value, Field):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_fields'] = fields

        clsobj = super().__new__(cls, name, bases, clsdict)

        return clsobj


class Serializer(metaclass=DeclarativeSerializerMeta):
    def __init__(self, instance):
        self._obj = instance
        self._called_validation = False
        super.__init__()

    def is_valid(self):
        self._called_validation = True
        for field_name, field in self._fields.items():
            if field.validate(getattr(self._obj, field_name)):
                return True
        return False

    @property
    def data(self):
        if self._called_validation:
            return {field_name: field.transform(getattr(self._obj, field_name))
                    for field_name, field in self._fields.items()}
        else:
            raise Exception('Call .is_valid() before .data')
