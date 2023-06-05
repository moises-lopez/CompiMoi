from virtualMemory import VirtualMemory
from scopes import Scope
from quadOperators import QuadOperator
from varTypes import VarType
from semanticCube import SemanticCube
from paramsVm import ParamsVm


class CompilerManager:
    def __init__(self):
        self.functionDirectory = {}
        self.quadruples = [[]]
        self.quadrupleCounter = 1
        self.operatorsStack = []
        self.operandsStack = []
        self.typesStack = []
        self.jumpsStack = []
        self.dimentionsStack = []
        self.currentDimentionNode = []
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
        self.paramsVm = ParamsVm()

    def addFunctionToDir(self, functionName, scope, type):
        self.functionDirectory[functionName] = {
            'type': type,
            'scope': scope,
            'varsTable': {},
            'size': {Scope.LOCAL: {'int': 0, 'float': 0, 'boolean': 0},
                     Scope.TEMPORAL: {'int': 0, 'float': 0, 'boolean': 0, 'total': 0},
                     Scope.GLOBAL: {'int': 0, 'float': 0, 'boolean': 0},
                     Scope.MAIN: {'int': 0, 'float': 0, 'boolean': 0},
                     }
        }
        if(type == 'Function'):
            self.paramsVm.initFunctionSize(functionName)
            if(self.currentType != VarType.VOID):
                self.addVariableToVarTable(functionName, False)

        if (type == 'Program'):
            self.addQuadruple(QuadOperator.GOTO, '', '', '')

    def setCurrentFunction(self, functionName):
        self.currentFunction = functionName

    def setProgramName(self, programName):
        self.programName = programName

    def addQuadruple(self, operator, leftOperand, rightOperand, result):
        self.quadrupleCounter += 1
        leftOperandAddress = self.getOperandAddress(leftOperand)
        rightOperandAddress = self.getOperandAddress(rightOperand)
        resultAddress = result
        if operator != QuadOperator.ERA:
            resultAddress = self.getOperandAddress(result)

        self.quadruples.append(
            [operator, leftOperandAddress, rightOperandAddress, resultAddress])

    def getOperandAddress(self, operand):
        if (type(operand) == int):
            return operand
        address = operand
        if operand in self.functionDirectory[self.currentFunction]['varsTable']:
            address = self.functionDirectory[self.currentFunction]['varsTable'][operand]['address']
        if operand in self.functionDirectory[self.programName]['varsTable']:
            address = self.functionDirectory[self.programName]['varsTable'][operand]['address']
        return address

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
        scope = self.functionDirectory[self.currentFunction]['scope']

        arrayAddresses = self.getAddressesOfAnArray(scope, size - 1, self.currentType)
        self.paramsVm.updateVariableFunctionSize(scope, self.currentFunction, size - 1, arrayAddresses)

    def getAddressesOfAnArray(self, scope, size, type):
        arrayAddresses = []
        for cont in range(size):
            arrayAddresses.append(self.virtualMemoryManager.getNextAddressAvailable(scope, type))
        return arrayAddresses

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
        self.paramsVm.addToFunctionSize(
            scope, self.currentFunction, 1, [address])

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

    def handleReturnFunction(self):
        type = self.typesStack.pop()
        expectedType = VarType.VOID
        if self.currentFunction in self.functionDirectory[self.programName]['varsTable']:
            expectedType = self.functionDirectory[self.programName]['varsTable'][self.currentFunction]['type']
        if expectedType == VarType.VOID:
            print('FUNCTION SHOULD NO RETURN ANYTHING')#TODO: HANDLE ERROR
        if type != expectedType:
            print('ERROR TYPE MISMATCH') #TODO: HANDLE ERROR
        leftOperand = self.operandsStack.pop()

        self.addQuadruple('=', leftOperand, '', self.currentFunction)

    def fillQuad(self, quadToFill, valueToFill):
        self.quadruples[quadToFill][3] = valueToFill

    def addParamsTableToCurrentFunction(self):
        self.functionDirectory[self.currentFunction]['paramsTable'] = []

    def addFunctionStartAddress(self):
        if 'addressStart' in self.functionDirectory[self.currentFunction]:
            return
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
        typeToPrint = self.typesStack.pop()
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
        self.paramsVm.addConstant(constant, address)

    def handleConstantNotOperand(self, constant):
        address = self.virtualMemoryManager.setConstantInVirtualMemory(
            str(constant))
        self.paramsVm.addConstant(constant, address)
        return address

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

        if self.operatorsStack[-1] == '>' or self.operatorsStack[-1] == '<' or self.operatorsStack[-1] == '!=' or self.operatorsStack[-1] == '==' or self.operatorsStack[-1] == '<=':  # TODO: IMPROVE
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
        self.operatorsStack.append('(')

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

        if(functionCalled in self.functionDirectory[self.programName]['varsTable']):
            type = self.functionDirectory[self.programName]['varsTable'][functionCalled]['type']
            result = self.nextAvail(type)
            self.operandsStack.append(result)
            self.typesStack.append(type)
            self.addQuadruple('=', functionCalled, '', result)

        if self.operatorsStack[-1] == '(':
            self.operatorsStack.pop()
        else:
            print('ERROR FUNCTION CALL') #TODO: HANDLE ERROR

    def nextAvail(self, type):
        self.functionDirectory[self.currentFunction]['size'][Scope.TEMPORAL][type] += 1
        self.functionDirectory[self.currentFunction]['size'][Scope.TEMPORAL]['total'] += 1
        scope = self.functionDirectory[self.currentFunction]['scope']

        varId = 't' + \
            str(self.functionDirectory[self.currentFunction]
                ['size'][Scope.TEMPORAL]['total'])
        self.currentVarId = varId
        address = self.virtualMemoryManager.getNextAddressAvailable(
            Scope.TEMPORAL, type)
        self.addTypeAndAddressToVar(type, address)
        self.paramsVm.addToFunctionSize(scope, self.currentFunction, 1, [address])
        return varId

    def handleEndOfProgram(self):
        self.addQuadruple(QuadOperator.END, '', '', '')

    def handleInitArrayAccessing(self):
        varId = self.operandsStack.pop()
        type = self.typesStack.pop()

        if varId not in self.functionDirectory[self.currentFunction]['varsTable'] and varId not in self.functionDirectory[self.programName]['varsTable']:
            print('NOT POSSIBLE TO ACCESS THIS ARRAY') #TODO: HANDLE ERROR
        self.DIM = 1
        self.dimentionsStack.append({'varId': varId, 'DIM': self.DIM})
        self.operatorsStack.append('(')

    def handleSeenExpresionArray(self):
        currentDimention = self.dimentionsStack[-1]['DIM']
        currentVarId = self.dimentionsStack[-1]['varId']
        currentDimentionNode = self.getArrayDimentionNode(currentVarId, currentDimention)
        lowerLimit = currentDimentionNode['lowerLimit']
        upperLimit = currentDimentionNode['upperLimit']
        m = currentDimentionNode['m']
        lowerLimitAddress = self.handleConstantNotOperand(lowerLimit)
        upperLimitAddress = self.handleConstantNotOperand(upperLimit)
        self.addQuadruple(QuadOperator.VERIFY, self.operandsStack[-1], lowerLimitAddress, upperLimitAddress)
        if not currentDimentionNode['isFinal']:
            aux = self.operandsStack.pop()
            result = self.nextAvail(VarType.INT)
            mAddress = self.handleConstantNotOperand(m)
            self.addQuadruple('*', aux, mAddress, result)
            self.operandsStack.append(result)
        if currentDimention > 1:
            aux2 = self.operandsStack.pop()
            aux1 = self.operandsStack.pop()
            result = self.nextAvail(VarType.INT)
            self.addQuadruple('+', aux1, aux2, result)
            self.operandsStack.append(result)

    def handleIncrementCurrentArrayDimention(self):
        self.dimentionsStack[-1]['DIM'] += 1

    def handleEndArrayAccessing(self):
        currentDimention = self.dimentionsStack[-1]['DIM']
        currentVarId = self.dimentionsStack[-1]['varId']
        currentDimentionNode = self.getArrayDimentionNode(currentVarId, currentDimention)
        aux1 = self.operandsStack.pop()
        result = self.nextAvail(VarType.INT)
        result2 = self.nextAvail(VarType.INT)
        K = currentDimentionNode['m']
        KAddress = self.handleConstantNotOperand(K)
        initialAddress = self.getInitialAddressOfAnArray(currentVarId)
        initialAddressAddress = self.handleConstantNotOperand(initialAddress)
        self.addQuadruple('+', aux1, KAddress, result)
        self.addQuadruple('+', result, initialAddressAddress, result2)
        result2Address = self.getOperandAddress(result2)
        self.operandsStack.append('*' + str(result2Address))

        if self.operatorsStack[-1] == '(':
            self.operatorsStack.pop()
        else:
            print('ERROR ARRAY ACCESS') #TODO: HANDLE ERROR

        self.dimentionsStack.pop()

    def getArrayDimentionNode(self, varId, dimention):
        dimention -= 1
        if varId in self.functionDirectory[self.currentFunction]['varsTable']:
            dimentionNode = self.functionDirectory[self.currentFunction]['varsTable'][varId]['dimentionNodes'][dimention]
            if len(self.functionDirectory[self.currentFunction]['varsTable'][varId]['dimentionNodes']) <= dimention + 1:
                dimentionNode['isFinal'] = True
            else:
                dimentionNode['isFinal'] = False
        else:
            dimentionNode = self.functionDirectory[self.programName]['varsTable'][varId]['dimentionNodes'][dimention]
            if len(self.functionDirectory[self.programName]['varsTable'][varId]['dimentionNodes']) <= dimention + 1:
                dimentionNode['isFinal'] = True
            else:
                dimentionNode['isFinal'] = False
        return dimentionNode

    def getInitialAddressOfAnArray(self, varId):
        if varId in self.functionDirectory[self.currentFunction]['varsTable']:
            return self.functionDirectory[self.currentFunction]['varsTable'][varId]['address']
        elif varId in self.functionDirectory[self.programName]['varsTable']:
            return self.functionDirectory[self.programName]['varsTable'][varId]['address']