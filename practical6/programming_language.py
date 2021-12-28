class ProgrammingLanguage:
    def __init__(self, field, dynamic, reflection, year):
        self.dynamic = dynamic
        self.field = field
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {}, {}, first appeared in {}".format(self.field, self.dynamic, self.reflection, self.year)

    def is_dynamic(self):
        return self.dynamic == "Dynamic"


