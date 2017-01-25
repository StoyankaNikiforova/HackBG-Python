from validate_email import validate_email


class Field:
    def tarnform(self, value):
        return value

    def validate(self, value):
        return False


class TextColumn(Field):
    def __init__(self, max_length=100):
        self.max_length = max_length

    def validate(self, value):
        return valitate_email(value)


class IntegerColumn(Field):
    def __init__(self, number=1):
        self.number = number

    def transform(self, value):
        return str(value)

    def validate(self, value):
        return True


class PKColumn:
    def transform(self, value):
        return value.isoformat()

    def validate(self, value):
        return True
