from scopes import Scope

START_GLOBAL_VARS = 0
START_GLOBAL_VARS_INT = 0
END_GLOBAL_VARS_INT = 250
START_GLOBAL_VARS_FLOAT = 251
END_GLOBAL_VARS_FLOAT = 500
START_GLOBAL_VARS_BOOLEAN = 501
END_GLOBAL_VARS_BOOLEAN = 750
START_GLOBAL_VARS_CHAR = 751
END_GLOBAL_VARS_CHAR = 1000
END_GLOBAL_VARS = 1000

START_LOCAL_VARS = 1001
START_LOCAL_VARS_INT = 1001
END_LOCAL_VARS_INT = 1250
START_LOCAL_VARS_FLOAT = 1251
END_LOCAL_VARS_FLOAT = 1500
START_LOCAL_VARS_BOOLEAN = 1501
END_LOCAL_VARS_BOOLEAN = 1750
START_LOCAL_VARS_CHAR = 1751
END_LOCAL_VARS_CHAR = 2000
END_LOCAL_VARS = 2000

START_TEMPORAL_VARS = 2001
START_TEMPORAL_VARS_INT = 2001
END_TEMPORAL_VARS_INT = 2250
START_TEMPORAL_VARS_FLOAT = 2251
END_TEMPORAL_VARS_FLOAT = 2500
START_TEMPORAL_VARS_BOOLEAN = 2501
END_TEMPORAL_VARS_BOOLEAN = 2750
START_TEMPORAL_VARS_CHAR = 2751
END_TEMPORAL_VARS_CHAR = 3000
END_TEMPORAL_VARS = 3000

START_CONSTANTS = 3001
END_CONSTANTS = 4000


class VirtualMemory:
    def __init__(self):
        self.virtualMemoryObject = {Scope.GLOBAL: {},
                                    Scope.LOCAL: {}, Scope.TEMPORAL: {}, Scope.CONSTANT: {}}
        self.virtualMemoryArray = [4000]

        self.globalIntCounter = 0
        self.globalFloatCounter = 0
        self.globalBooleanCounter = 0
        self.globalCharCounter = 0

        self.localIntCounter = 0
        self.localFloatCounter = 0
        self.localBooleanCounter = 0
        self.localCharCounter = 0

        self.temporalIntCounter = 0
        self.temporalFloatCounter = 0
        self.temporalBooleanCounter = 0
        self.temporalCharCounter = 0

        self.constantCounter = 0

    def setConstantInVirtualMemory(self, constantId):
        if constantId in self.virtualMemoryObject[Scope.CONSTANT]:
            return self.virtualMemoryObject[Scope.CONSTANT][constantId]
        address = self.getNextAddressAvailable(Scope.CONSTANT, '')
        self.virtualMemoryObject[Scope.CONSTANT][constantId] = address
        return address

    def setVarInVirtualMemory(self, varId, scope, type):
        address = self.getNextAddressAvailable(scope, type)

        self.virtualMemoryObject[scope][varId] = address
        return address

    def getConstantOfAddress(self, constantId):
        address = None
        address = self.virtualMemoryObject[Scope.LOCAL][constantId]
        if (not address):
            address = self.virtualMemoryObject[Scope.GLOBAL][constantId]
        return address

    def getValueOfAddress(self, address):
        scope = ''
        if (address >= START_GLOBAL_VARS & address <= END_GLOBAL_VARS):
            return Scope.GLOBAL
        elif (address >= START_LOCAL_VARS & address <= END_LOCAL_VARS):
            return Scope.LOCAL
        elif (address >= START_TEMPORAL_VARS & address <= END_TEMPORAL_VARS):
            return Scope.TEMPORAL
        elif (address >= START_CONSTANTS & address <= END_CONSTANTS):
            return Scope.CONSTANT

        return self.virtualMemoryArray[address]

    def getAddressOfConstant(self, constantId):
        return self.virtualMemoryObject[Scope.CONSTANT][constantId]

    def dumpLocalVirtualMemory(self):
        self.virtualMemoryObject[Scope.LOCAL] = {}
        self.virtualMemoryObject[Scope.TEMPORAL] = {}
        self.localIntCounter = 0
        self.localFloatCounter = 0
        self.localBooleanCounter = 0
        self.localCharCounter = 0

        self.temporalIntCounter = 0
        self.temporalFloatCounter = 0
        self.temporalBooleanCounter = 0
        self.temporalCharCounter = 0

    def getNextAddressAvailable(self, scope, type):
        if scope == Scope.GLOBAL:
            if type == 'int':
                address = START_GLOBAL_VARS_INT + self.globalIntCounter
                self.globalIntCounter += 1
                return address
            elif type == 'float':
                address = START_GLOBAL_VARS_FLOAT + self.globalFloatCounter
                self.globalFloatCounter += 1
                return address
            elif type == 'boolean':
                address = START_GLOBAL_VARS_BOOLEAN + self.globalBooleanCounter
                self.globalBooleanCounter += 1
                return address
            elif type == 'char':
                address = START_GLOBAL_VARS_CHAR + self.globalCharCounter
                self.globalCharCounter += 1
                return address
        elif scope == Scope.LOCAL or scope == Scope.MAIN:
            if type == 'int':
                address = START_LOCAL_VARS_INT + self.localIntCounter
                self.localIntCounter += 1
                return address
            elif type == 'float':
                address = START_LOCAL_VARS_FLOAT + self.localFloatCounter
                self.localFloatCounter += 1
                return address
            elif type == 'boolean':
                address = START_LOCAL_VARS_BOOLEAN + self.localBooleanCounter
                self.localBooleanCounter += 1
                return address
            elif type == 'char':
                address = START_LOCAL_VARS_CHAR + self.localCharCounter
                self.localCharCounter += 1
                return address
        elif scope == Scope.TEMPORAL:
            if type == 'int':
                address = START_TEMPORAL_VARS_INT + self.temporalIntCounter
                self.temporalIntCounter += 1
                return address
            elif type == 'float':
                address = START_TEMPORAL_VARS_FLOAT + self.temporalFloatCounter
                self.temporalFloatCounter += 1
                return address
            elif type == 'boolean':
                address = START_TEMPORAL_VARS_BOOLEAN + self.temporalBooleanCounter
                self.temporalBooleanCounter += 1
                return address
            elif type == 'char':
                address = START_TEMPORAL_VARS_CHAR + self.temporalCharCounter
                self.temporalCharCounter += 1
                return address
        elif scope == Scope.CONSTANT:
            address = START_CONSTANTS + self.constantCounter
            self.constantCounter += 1
            return address

    def setValueToAddress(self, address, value):
        self.virtualMemoryArray[address] = value

    def getValueOfAddress(self, address, value):
        return self.virtualMemoryArray[address]


def getConstantStartOfAddresses(type, scope):
    if scope == Scope.GLOBAL:
        if type == 'int':
            return START_GLOBAL_VARS_INT
        elif type == 'float':
            return START_GLOBAL_VARS_FLOAT
        elif type == 'boolean':
            return START_GLOBAL_VARS_BOOLEAN
        elif type == 'char':
            return START_GLOBAL_VARS_CHAR
    elif scope == Scope.LOCAL:
        if type == 'int':
            return START_LOCAL_VARS_INT
        elif type == 'float':
            return START_LOCAL_VARS_FLOAT
        elif type == 'boolean':
            return START_LOCAL_VARS_BOOLEAN
        elif type == 'char':
            return START_LOCAL_VARS_CHAR
    elif scope == Scope.TEMPORAL:
        if type == 'int':
            return START_TEMPORAL_VARS_INT
        elif type == 'float':
            return START_TEMPORAL_VARS_FLOAT
        elif type == 'boolean':
            return START_TEMPORAL_VARS_BOOLEAN
        elif type == 'char':
            return START_TEMPORAL_VARS_CHAR
    elif scope == Scope.CONSTANT:
        return START_CONSTANTS
