from quadOperators import QuadOperator
from varTypes import VarType
from virtualMemory import VirtualMemory
from scopes import Scope


class ParamsVm:
    def __init__(self):
        self.GlobalSize = {'size': 0, 'arrayDirecciones': []}
        self.FunctionsSize = {}
        self.Constants = {'size': 0, 'constantDictionary': {}}

    def addConstant(self, value, address):
        self.Constants['constantDictionary'][address] = value
        self.Constants['size'] += 1

    def initFunctionSize(self, functionName):
        self.FunctionsSize[functionName] = {'size': 0, 'arrayDirecciones': []}

    def addToFunctionSize(self, scope, functionName, size, addresses):
        if (scope == Scope.GLOBAL):
            self.GlobalSize['size'] += size
            self.GlobalSize['arrayDirecciones'].extend(addresses)
        else:
            self.FunctionsSize[functionName]['size'] += size
            self.FunctionsSize[functionName]['arrayDirecciones'].extend(
                addresses)

    def printParamsVm(self):
        print('GlobalSize', self.GlobalSize)
        print('FunctionsSize', self.FunctionsSize)
        print('Constants', self.Constants)
