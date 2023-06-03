from paramsVm import ParamsVm


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
        print(self.localMemory)

    def addLocalMemory(self, functionMemoryData):
        print('before', self.localMemory)
        functionMemoryContext = {}
        for address in functionMemoryData['arrayAddresses']:
            functionMemoryContext[address] = None

        self.localMemory.append(functionMemoryContext)
        print('after', self.localMemory)
        print('/////////')


    def setValueToAddress(self, value, address):
        currentFunctionContext = self.localMemory[-1]
        if address in currentFunctionContext:
            self.localMemory[-1][address] = value
            return
        self.globalMemory[address] = value

    def getValueOfAddress(self, address):
        currentFunctionContext = self.localMemory[-1]
        if address in currentFunctionContext:
            value = self.localMemory[-1][address]
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

        self.setValueToAddress(value, targetAddress)

    def freeCurrentLocalMemory(self):
        self.localMemory.pop()