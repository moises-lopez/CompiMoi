from virtualMemory import VirtualMemory
from scopes import Scope
from quadOperators import QuadOperator
from varTypes import VarType
from semanticCube import SemanticCube


class CompilerManager:
    def __init__(self):
        self.functionDirectory = {}
        self.quadruples = [[]]
        self.quadrupleCounter = 1
        self.operatorsStack = []
        self.operandsStack = []
        self.typesStack = []
        self.jumpsStack = []
        self.currentFunction = ''
        self.currentVarTable = ''
        self.currentType = ''
        self.programName = ''
        self.parameterCounter = 0
        self.functionCallStack = []
        self.isArray = False
        self.currentVarId = ''
        self.DIM = 1
        self.R = 1
        self.virtualMemoryManager = VirtualMemory()
        self.semanticCubeManager = SemanticCube()

    def addFunctionToDir(self, functionName, scope, type):
        self.functionDirectory[functionName] = {
            'type': type,
            'scope': scope,
            'varsTable': {},
            'size': {Scope.LOCAL: {'int': 0, 'float': 0, 'boolean': 0},
                     Scope.TEMPORAL: {'int': 0, 'float': 0, 'boolean': 0, 'total': 0},
                     Scope.GLOBAL: {'int': 0, 'float': 0, 'boolean': 0}
                     }
        }
        if (type == 'Program'):
            self.addQuadruple(QuadOperator.GOTO, '', '', '')

    def setCurrentFunction(self, functionName):
        self.currentFunction = functionName

    def setProgramName(self, programName):
        self.programName = programName

    def addQuadruple(self, operator, leftOperand, rightOperand, result):
        self.quadrupleCounter += 1
        self.quadruples.append([operator, leftOperand, rightOperand, result])

    def setCurrentVarId(self, varId):
        self.currentVarId = varId

    def getCurrentVarId(self):
        return self.currentVarId

    def incrementDimention(self):
        self.DIM += 1
        self.functionDirectory[self.currentFunction]['varsTable'][self.currentVarId]['dimentionNodes'].append({
        })

    def incrementDimention(self):
        self.DIM += 1
        self.functionDirectory[self.currentFunction]['varsTable'][self.currentVarId]['dimentionNodes'].append({
        })

    def setLowerLimitCurrentDimention(self, lowerLimit):
        self.functionDirectory[self.currentFunction]['varsTable'][self.currentVarId]['dimentionNodes'][self.DIM -
                                                                                                       1]['lowerLimit'] = lowerLimit

    def setUpperLimitCurrentDimention(self, upperLimit):
        lowerLimit = self.functionDirectory[self.currentFunction]['varsTable'][
            self.currentVarId]['dimentionNodes'][self.DIM - 1]['lowerLimit'] or 0

        self.functionDirectory[self.currentFunction]['varsTable'][self.currentVarId]['dimentionNodes'][self.DIM -
                                                                                                       1]['upperLimit'] = upperLimit

    def computeR(self):
        lowerLimit = self.functionDirectory[self.currentFunction]['varsTable'][
            self.currentVarId]['dimentionNodes'][self.DIM - 1]['lowerLimit'] or 0

        upperLimit = self.functionDirectory[self.currentFunction]['varsTable'][
            self.currentVarId]['dimentionNodes'][self.DIM - 1]['upperLimit']

        self.R = (upperLimit - lowerLimit + 1) * self.R

    def initArrayDeclaration(self):
        self.functionDirectory[self.currentFunction]['varsTable'][self.currentVarId]['dimentionNodes'] = [
            {}]
        self.isArray = True
        self.DIM = 1
        self.R = 1

    def endArrayDeclaration(self):
        self.DIM = 1
        offset = 0
        size = self.R
        dimentionNodes = self.functionDirectory[self.currentFunction][
            'varsTable'][self.currentVarId]['dimentionNodes']

        for dimentionNode in dimentionNodes:
            lowerLimit = dimentionNode['lowerLimit'] or 0
            upperLimit = dimentionNode['upperLimit']
            m = self.R / (upperLimit - lowerLimit + 1)
            self.functionDirectory[self.currentFunction][
                'varsTable'][self.currentVarId]['dimentionNodes'][self.DIM - 1]['m'] = m  # TODO: check if possible to use reference

            self.R = m
            offset = offset + lowerLimit * m
            self.DIM += 1
        self.K = offset
        self.functionDirectory[self.currentFunction][
            'varsTable'][self.currentVarId]['dimentionNodes'][self.DIM - 2]['m'] = self.K * -1

    def addVariableToVarTable(self, varId, isParam):
        self.currentVarId = varId
        try:
            if (self.currentVarId in self.functionDirectory[self.currentFunction]['varsTable']):
                print('Redeclaration on variable', self.currentVarId)
        except (NameError, AttributeError) as e:
            print('Redeclaration on variable', self.currentVarId)

        scope = self.functionDirectory[self.currentFunction]['scope']
        address = self.virtualMemoryManager.getNextAddressAvailable(
            scope, self.currentType)

        self.addTypeAndAddressToVar(self.currentType, address)
        self.incrementVariableCounter(scope, self.currentType)
        if (isParam):
            self.functionDirectory[self.currentFunction]['paramsTable'].append(
                self.currentType)

    def addTypeAndAddressToVar(self, type, address):
        self.functionDirectory[self.currentFunction]['varsTable'][self.currentVarId] = {
            'type': type, 'address': address}

    def incrementVariableCounter(self, scope, type):
        self.functionDirectory[self.currentFunction]['size'][scope][type] += 1

    def setCurrentType(self, type):
        self.currentType = type

    def endFunction(self):
        # dirFuncionesDict[currentFunction]['varsTable'] = {} DESCOMENTAR, POR EL MOMENTO LO DEJO ASí PARA LOGGEARLO AL FINAL
        self.virtualMemoryManager.dumpLocalVirtualMemory()

        self.addQuadruple(QuadOperator.ENDFUNC, '', '', '')

    def fillQuad(self, quadToFill, valueToFill):
        self.quadruples[quadToFill][3] = valueToFill

    def addParamsTableToCurrentFunction(self):
        self.functionDirectory[self.currentFunction]['paramsTable'] = []

    def addFunctionStartAddress(self):
        self.functionDirectory[self.currentFunction]['addressStart'] = self.quadrupleCounter

    def addOperatorToStack(self, operator):
        self.operatorsStack.append(operator)

    def createAssignationQuad(self):

        rightOperand = self.operandsStack.pop()
        leftOperand = self.operandsStack.pop()
        rightType = self.typesStack.pop()
        leftType = self.typesStack.pop()
        operator = self.operatorsStack.pop()

        if (rightType == leftType):
            self.addQuadruple(operator, rightOperand, '', leftOperand)
        else:
            print('ERROR MISMATCH')  # TODO: HANDLE ERROR

    def createPrintQuad(self):  # TODO: HANDLE TYPE
        valueToPrint = self.operandsStack.pop()
        self.addQuadruple(QuadOperator.PRINT, '', '', valueToPrint)

    def handleConditionStart(self):
        typeExpected = self.typesStack.pop()

        if (typeExpected != VarType.BOOLEAN):
            print('ERROR MISMATCH IN CONDITION')  # TODO: HANDLE ERROR
        else:
            result = self.operandsStack.pop()
            self.addQuadruple(QuadOperator.GOTOF, result, '', '')
            self.jumpsStack.append(self.quadrupleCounter - 1)

    def handleConditionElse(self):
        self.addQuadruple(QuadOperator.GOTO, '', '', '')
        false = self.jumpsStack.pop()
        self.jumpsStack.append(self.quadrupleCounter - 1)
        self.fillQuad(false, self.quadrupleCounter)

    def handleConditionEnd(self):
        end = self.jumpsStack.pop()
        self.fillQuad(end, self.quadrupleCounter)

    def handleConstant(self, constant, type):
        address = self.virtualMemoryManager.setConstantInVirtualMemory(
            str(constant))

        self.operandsStack.append(address)
        self.typesStack.append(type)

    def endOfExpresionParentheses(self):
        if (self.operandsStack[-1] != '('):  # TODO: IMPROVE
            print('Parentesis Mismatch')  # TODO: HANDLE ERROR
        else:
            self.operatorsStack.pop()

    def addVariableToStack(self, varId):
        type = ''
        if (varId in self.functionDirectory[self.currentFunction]['varsTable']):
            type = self.functionDirectory[self.currentFunction]['varsTable'][varId]['type']
        elif (varId in self.functionDirectory[self.programName]['varsTable']):
            type = self.functionDirectory[self.programName]['varsTable'][varId]['type']

        if (type == ''):
            print('no se encontró variable', varId)  # TODO: HANDLE ERROR

        self.operandsStack.append(varId)
        self.typesStack.append(type)

    def handleTermino(self):
        if (len(self.operatorsStack) == 0):
            return

        if self.operatorsStack[-1] == '+' or self.operatorsStack[-1] == '-':  # TODO: IMPROVE
            rightOperand = self.operandsStack.pop()
            leftOperand = self.operandsStack.pop()
            rightType = self.typesStack.pop()
            leftType = self.typesStack.pop()
            operator = self.operatorsStack.pop()
            resultType = self.semanticCubeManager.getResultType(
                rightType, leftType, operator)
            if (resultType):
                result = self.nextAvail(resultType)
                self.addQuadruple(operator, leftOperand, rightOperand, result)
                self.operandsStack.append(result)
                self.typesStack.append(resultType)
            else:
                print('ERROR MISMATCH')  # TODO: HANDLE ERROR

    def handleFactor(self):
        if (len(self.operatorsStack) == 0):
            return
        if self.operatorsStack[-1] == '*' or self.operatorsStack[-1] == '/':  # TODO: IMPROVE
            rightOperand = self.operandsStack.pop()
            leftOperand = self.operandsStack.pop()
            rightType = self.typesStack.pop()
            leftType = self.typesStack.pop()
            operator = self.operatorsStack.pop()
            resultType = self.semanticCubeManager.getResultType(
                rightType, leftType, operator)
            if (resultType):
                result = self.nextAvail(resultType)
                self.addQuadruple(operator, leftOperand, rightOperand, result)
                self.operandsStack.append(result)
                self.typesStack.append(resultType)
            else:
                print('ERROR MISMATCH')  # TODO: HANDLE ERROR

    def handleComparation(self):
        if (len(self.operatorsStack) == 0):
            return

        if self.operatorsStack[-1] == '>' or self.operatorsStack[-1] == '<' or self.operatorsStack[-1] == '!=' or self.operatorsStack[-1] == '==':  # TODO: IMPROVE
            rightOperand = self.operandsStack.pop()
            leftOperand = self.operandsStack.pop()
            rightType = self.typesStack.pop()
            leftType = self.typesStack.pop()
            operator = self.operatorsStack.pop()
            resultType = self.semanticCubeManager.getResultType(
                rightType, leftType, operator)
            if (resultType):
                result = self.nextAvail(resultType)
                self.addQuadruple(operator, leftOperand, rightOperand, result)
                self.operandsStack.append(result)
                self.typesStack.append(resultType)
            else:
                print('ERROR MISMATCH')  # TODO: HANDLE ERROR

    def addJumpToCurrentQuadruple(self):
        self.jumpsStack.append(self.quadrupleCounter)

    def handleWhileStart(self):
        typeExpected = self.typesStack.pop()
        if (typeExpected != VarType.BOOLEAN):
            print('ERROR MISMATCH WHILE')  # TODO: HANDLE ERRO
        else:
            result = self.operandsStack.pop()
            self.addQuadruple(QuadOperator.GOTOF, result, '', '')
            self.jumpsStack.append(self.quadrupleCounter - 1)

    def handleWhileEnd(self):
        end = self.jumpsStack.pop()
        returnQuad = self.jumpsStack.pop()
        self.addQuadruple(QuadOperator.GOTO, '', '', returnQuad)
        self.fillQuad(end, self.quadrupleCounter)

    def handleFunctionCall(self, functionName):
        if functionName not in self.functionDirectory:
            print('ERROR FUNCTION NOT DECLARED')  # TODO: HANDLE ERRO
        self.functionCallStack.append(functionName)

    def handleFunctionCallJump(self, functionName):
        self.addQuadruple(QuadOperator.ERA, '', '', functionName)

    def handleFunctionParameter(self):
        argument = self.operandsStack.pop()
        argumentType = self.typesStack.pop()
        functionCalled = self.functionCallStack[-1]
        if (len(self.functionDirectory[functionCalled]['paramsTable']) <= self.parameterCounter):
            print('ERROR TOO MANY PARAMETERS')  # TODO: HANDLE ERRO

        if (argumentType != self.functionDirectory[functionCalled]['paramsTable'][self.parameterCounter]):
            print('ERROR PARAMETER MISMATCH')  # TODO: HANDLE ERROR
        self.addQuadruple(QuadOperator.PARAMETER, '',
                          argument, self.parameterCounter)

    def incrementParameterCounter(self):
        self.parameterCounter += 1

    def checkNoParametersLeft(self):
        functionCalled = self.functionCallStack[-1]
        if (len(self.functionDirectory[functionCalled]['paramsTable']) > self.parameterCounter):
            print('ERROR NOT ALL PARAMETERS')  # TODO: HANDLE ERROR

    def handleEndOfFunctionCall(self):
        self.parameterCounter = 0
        functionCalled = self.functionCallStack.pop()
        self.addQuadruple(QuadOperator.GOSUB, functionCalled, '',
                          self.functionDirectory[functionCalled]['addressStart'])

    def nextAvail(self, type):
        self.functionDirectory[self.currentFunction]['size'][Scope.TEMPORAL][type] += 1
        self.functionDirectory[self.currentFunction]['size'][Scope.TEMPORAL]['total'] += 1
        return 't' + str(self.functionDirectory[self.currentFunction]['size'][Scope.TEMPORAL]['total'])
