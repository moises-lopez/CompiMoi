from enum import Enum


class QuadOperator(str, Enum):
    GOTOF = 'GOTOF',
    GOTOT = 'GOTOT',
    GOTO = 'GOTO',
    ENDFUNC = 'ENDFUNC',
    PRINT = 'PRINT',
    ERA = 'ERA',
    PARAMETER = 'PARAMETER',
    GOSUB = 'GOSUB',
    END = 'END'
    VERIFY = 'VERIFY'
    READ = 'READ'
    PRINTMATRIX = 'PRINTMATRIX'
    SQUAREVECTOR = 'SQUAREVECTOR'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
