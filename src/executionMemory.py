from src.paramsVm import ParamsVm


class ExecutionMemory:
    def __init__(self, paramsVm: ParamsVm):
        globalMemoryContext = {}
        mainMemoryContext = {}
        for address in paramsVm.GlobalSize['arrayAddresses']:
            globalMemoryContext[address] = None

        for address in paramsVm.MainSize['arrayAddresses']:
            mainMemoryContext[address] = None

        self.globalMemory = globalMemoryContext
        self.localMemory = [mainMemoryContext]
        self.constantTable = paramsVm.Constants['constantDictionary']
        self.currentLocalMemoryPointer = 0

    def addLocalMemory(self, functionMemoryData):
        functionMemoryContext = {}
        for address in functionMemoryData['arrayAddresses']:
            functionMemoryContext[address] = None

        self.localMemory.append(functionMemoryContext)


    def setValueToAddress(self, value, address):
        if str(address).startswith('*'):
            address = self.getValueOfAddress(address[1:])
        currentFunctionContext = self.localMemory[self.currentLocalMemoryPointer]
        if address in currentFunctionContext:
            self.localMemory[self.currentLocalMemoryPointer][address] = value
            return
        self.globalMemory[address] = value

    def setValueToParameterAddress(self, value, address):
        parameterFunctionContext = self.localMemory[-1]
        if address in parameterFunctionContext:
            self.localMemory[-1][address] = value
            return
        self.globalMemory[address] = value

    def getValueOfAddress(self, address):
        if str(address).startswith('*'):
            address = self.getValueOfAddress(address[1:])
        address = int(address)
        currentFunctionContext = self.localMemory[self.currentLocalMemoryPointer]
        if address in currentFunctionContext:
            value = self.localMemory[self.currentLocalMemoryPointer][address]
        elif address in self.globalMemory:
            value = self.globalMemory[address]
        else:
            value = self.constantTable[address]
        return value

    def setFunctionParameter(self, value, parameterNumber):
        cont = 0
        targetAddress = ''
        for address in self.localMemory[-1]:
            targetAddress = address
            if(cont == parameterNumber):
                break
            cont += 1

        self.setValueToParameterAddress(value, targetAddress)

    def freeCurrentLocalMemory(self):
        self.localMemory.pop()
        self.currentLocalMemoryPointer -= 1

    def incrementCurrentLocalMemoryPointer(self):
        self.currentLocalMemoryPointer = len(self.localMemory) - 1

    def printMatrix(self, size, initialAddress):
        print("|| PRINTING MATRIX ||")
        for cont in range(size):
            value = self.getValueOfAddress(initialAddress + cont)
            print(value)
        print("|| END PRINTING MATRIX ||")

    def squareVector(self, size, initialAddress):
        for cont in range(size):
            value = self.getValueOfAddress(initialAddress + cont)
            self.setValueToAddress(value * value, initialAddress + cont)
