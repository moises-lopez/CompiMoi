from quadOperators import QuadOperator
from varTypes import VarType
from virtualMemory import VirtualMemory
from paramsVm import ParamsVm
from executionMemory import ExecutionMemory


class VirtualMachine:
    def __init__(self):
        self.quadruples = []
        self.instructionPointer = 0
        self.executionMemory = None
        self.paramsVM = None

    def init(self, quadruples, paramsVm: ParamsVm):
        self.quadruples = quadruples
        self.instructionPointer = 1
        self.executionMemory = ExecutionMemory(paramsVm)

    def run(self):
        endOfProgram = True
        while not endOfProgram:
            quadruple = self.quadruples[self.instructionPointer]
            operator = quadruple[0]
            leftOperand = quadruple[1]
            rightOperand = quadruple[2]
            result = self.quadruples[3]

            if operator == QuadOperator.GOTO:
                self.instructionPointer == result

            if operator == QuadOperator.GOTOF:
                if leftOperand == False:
                    self.instructionPointer == result

            if operator == QuadOperator.GOTOT:
                if leftOperand == True:
                    self.instructionPointer == result

            if operator == QuadOperator.PRINT:
                print(result)

            if operator == '+':
                tempResult = leftOperand + rightOperand
                self.virtualMemoryManager.setValueToAddress(result, tempResult)

            if operator == '-':
                tempResult = leftOperand - rightOperand
                self.virtualMemoryManager.setValueToAddress(result, tempResult)

            if operator == '*':
                tempResult = leftOperand * rightOperand
                self.virtualMemoryManager.setValueToAddress(result, tempResult)

            if operator == '/':
                tempResult = leftOperand / rightOperand
                self.virtualMemoryManager.setValueToAddress(result, tempResult)

            if operator == '>':
                tempResult = leftOperand > rightOperand
                self.virtualMemoryManager.setValueToAddress(result, tempResult)

            if operator == '<':
                tempResult = leftOperand > rightOperand
                self.virtualMemoryManager.setValueToAddress(result, tempResult)
