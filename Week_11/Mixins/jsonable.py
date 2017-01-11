import json


class Jsonable:
    def to_dict(self):
        data = {
            'dict': self.__dict__,
            'classname': self.__class__.__name__
        }
        return data

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.load(xml_string)
        classname = data.get('classname', None)

        if classname != cls.__name__:
            raise ValueError('{} is not {}'.format(classname, cls.__name__))

        return cls(**data['dict'])
