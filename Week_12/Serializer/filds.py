from validate_email import validate_email


class Field:
    def tarnform(self, value):
        return value

    def validate(self, value):
        return False


class EmailField(Field):
    def validate(self, value):
        return valitate_email(value)


class CharlField(Field):
    def transform(self, value):
        return str(value)

    def validate(self, value):
        return True


class DateTimeField:
    def transform(self, value):
        return value.isoformat()

    def validate(self, value):
        return True
