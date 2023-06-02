from paramsVm import ParamsVm
import numpy as np


class ExecutionMemory:
    def __init__(self, paramsVm: ParamsVm):
        print('///////')

        print(paramsVm.GlobalSize['size'])
        self.globalMemory = np.empty([paramsVm.GlobalSize['size']])
        print('global memory', self.globalMemory)
        self.localMemory = []

        for function in paramsVm.FunctionsSize:
            self.localMemory.extend(
                np.empty(paramsVm.FunctionsSize[function]['size']))

        self.constantTable = paramsVm.Constants['constantDictionary']
        print(len(self.globalMemory), len(self.localMemory), self.constantTable)

    def initGlobalMemory(self, globalMemoryVariables):
        print()
