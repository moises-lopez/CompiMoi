from aenum import Enum


class Scope(str, Enum):
    GLOBAL = 'Global',
    LOCAL = 'Local',
    TEMPORAL = 'Temporal',
    CONSTANT = 'Constant'
    MAIN = 'Main'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
