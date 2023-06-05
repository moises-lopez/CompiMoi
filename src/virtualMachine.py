from enums.quadOperators import QuadOperator
from src.paramsVm import ParamsVm
from src.executionMemory import ExecutionMemory


class VirtualMachine:
    def __init__(self):
        self.quadruples = []
        self.instructionPointer = 0
        self.instructionPointerStack = []
        self.executionMemory = None
        self.paramsVM = None

    def init(self, quadruples, paramsVm: ParamsVm):
        self.quadruples = quadruples
        self.instructionPointer = 1
        self.executionMemory = ExecutionMemory(paramsVm)
        self.paramsVM = paramsVm

    def run(self):
        endOfProgram = False
        print('running')
        while not endOfProgram:
            quadruple = self.quadruples[self.instructionPointer]
            operator = quadruple[0]
            leftOperand = quadruple[1]
            rightOperand = quadruple[2]
            result = quadruple[3]

            self.instructionPointer += 1
            if operator == QuadOperator.GOTO:
                self.instructionPointer = result

            if operator == QuadOperator.GOTOF:
                value = self.executionMemory.getValueOfAddress(leftOperand)
                if value == False or value == 'False':
                    self.instructionPointer = result

            if operator == QuadOperator.GOTOT:
                if leftOperand == True or value == 'True':
                    self.instructionPointer = result

            if operator == QuadOperator.PRINT:
                value = self.executionMemory.getValueOfAddress(result)
                print(value)

            if operator == QuadOperator.GOSUB:
                self.instructionPointerStack.append(self.instructionPointer)
                self.executionMemory.incrementCurrentLocalMemoryPointer()
                self.instructionPointer = result

            if operator == QuadOperator.ERA:
                self.executionMemory.addLocalMemory(self.paramsVM.FunctionsSize[result])

            if operator == QuadOperator.PARAMETER:
                value = self.executionMemory.getValueOfAddress(rightOperand)
                self.executionMemory.setFunctionParameter(value, result)

            if operator == QuadOperator.ENDFUNC:
                self.executionMemory.freeCurrentLocalMemory()
                self.instructionPointer = self.instructionPointerStack.pop()

            if operator == '+':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue + rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '-':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue - rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '*':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue * rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '/':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue / rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '>':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue > rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '<':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue < rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '<=':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue <= rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '==':
                leftValue, rightValue = self.getValuesOfAddresses(leftOperand, rightOperand)
                tempResult = leftValue == rightValue
                self.executionMemory.setValueToAddress(tempResult, result)

            if operator == '=':
                value = self.executionMemory.getValueOfAddress(leftOperand)
                self.executionMemory.setValueToAddress(value, result)

            if operator == QuadOperator.READ:
                value = input()
                if value.isnumeric():
                    value = int(value)
                self.executionMemory.setValueToAddress(value, result)

            if operator == QuadOperator.PRINTMATRIX:
                self.executionMemory.printMatrix(leftOperand, rightOperand)

            if operator == QuadOperator.SQUAREVECTOR:
                self.executionMemory.squareVector(leftOperand, rightOperand)

            if operator == QuadOperator.END:
                endOfProgram = True

    def getValuesOfAddresses(self, address1, address2):
        leftValue = self.executionMemory.getValueOfAddress(address1)
        rightValue = self.executionMemory.getValueOfAddress(address2)
        return [leftValue, rightValue]