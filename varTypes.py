from enum import Enum


class VarType(str, Enum):
    INT = 'int',
    FLOAT = 'float',
    BOOLEAN = 'boolean',
    CHAR = 'char',
    VOID = 'void',

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
