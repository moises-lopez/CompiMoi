import ply.lex as lex
import ply.yacc as yacc
import sys
import json
from virtualMemory import VirtualMemory
from compilerManager import CompilerManager
from scopes import Scope
from varTypes import VarType
from virtualMachine import VirtualMachine

virtualMemoryManager = VirtualMemory()
compilerManager = CompilerManager()
virtualMachineManager = VirtualMachine()

tokens = [
    'INT_CTE',
    'FLOAT_CTE',
    'BOOLEAN_CTE',
    'STRING_CTE',
    'ID',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'LEFTPARENTHESES',
    'RIGHTPARENTHESES',
    'LEFTBRACE',
    'RIGHTBRACE',
    'LEFTBRACKET',
    'RIGHTBRACKET',
    'LESSTHAN',
    'GREATERTHAN',
    'NOTEQUAL',
    'THREEDOTS'
]

reserved = {
    'Programa': 'PROGRAMA',
    'void': 'VOID',
    'Main': 'MAIN',
    'Function': 'FUNCTION',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'boolean': 'BOOLEAN',
    'read': 'READ',
    'print': 'PRINT',
    '<>': 'NOTEQUALS',
    'call': 'CALL'
}

tokens += reserved.values()

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_LEFTPARENTHESES = r'\('
t_RIGHTPARENTHESES = r'\)'
t_LEFTBRACE = r'\{'
t_RIGHTBRACE = r'\}'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_THREEDOTS = r'\.\.\.'
t_ignore = ' \n'


def t_FLOAT_CTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT_CTE(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_BOOLEAN_CTE(t):
    r'\b(true|false)\b'
    return t


def t_STRING_CTE(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t


def t_PROGRAMA(t):
    r'Programa'
    return t


def t_VOID(t):
    r'void'
    return t


def t_MAIN(t):
    r'Main'
    return t


def t_FUNCTION(t):
    r'Function'
    return t


def t_VAR(t):
    r'var'
    return t


def t_IF(t):
    r'if'
    return t


def t_FOR(t):
    r'for'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_THEN(t):
    r'then'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_DO(t):
    r'\b(do)\b'
    return t


def t_CALL(t):
    r'\b(call)\b'
    return t


def t_TO(t):
    r'to'
    return t


def t_INT(t):
    r'int'
    return t


def t_FLOAT(t):
    r'float'
    return t


def t_BOOLEAN(t):
    r'boolean'
    return t


def t_READ(t):
    r'read'
    return t


def t_PRINT(t):
    r'print'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t


# Mensaje de error en caso de error lexico
def t_error(t):
    print(t)
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()


# Aqui se define la gramatica
# Los reglas de gramatica usan los tokens definidos en la parte de arriba
# Esta gramatica se basa en la actividad pasada con algunas modificaciones


def p_calc(p):  # falta poner main
    '''
      calc : PROGRAMA ID seen_program SEMICOLON vars modulesaux functionmain
     '''
    print('No syntax errors found :)')


def p_modulesaux(p):
    '''
      modulesaux : function modulesaux
           |
      '''


def p_seen_program(p):
    "seen_program : "
    programName = p[-1]
    compilerManager.setProgramName(programName)
    compilerManager.setCurrentFunction(programName)
    compilerManager.addFunctionToDir(programName, Scope.GLOBAL, 'Program')


def p_vars(p):
    ''' vars : VAR seen_vars tipo varsAuxDeclaration SEMICOLON vars 
                | empty
    '''


def p_varsAuxDeclaration(p):
    '''
        varsAuxDeclaration : idOrArrayDeclaration seen_end_declaration COMMA varsAuxDeclaration
                        | idOrArrayDeclaration seen_end_declaration
    '''


def p_seen_end_declaration(p):
    '''
        seen_end_declaration : 
    '''
    compilerManager.setCurrentVarId('')


def p_idOrArrayDeclaration(p):
    '''
        idOrArrayDeclaration : ID seen_ID_var
                            | ID seen_ID_var LEFTBRACKET seen_lBracket_array arrayDimesionAux RIGHTBRACKET seen_rBracket_array
    '''


def p_arrayDimesionAux(p):
    '''
        arrayDimesionAux : INT_CTE seen_lim_inf INT_CTE seen_lim_sup
                  |  INT_CTE seen_lim_inf INT_CTE seen_lim_sup COMMA seen_extra_dimension_array arrayDimesionAux
    '''


def p_seen_extra_dimension_array(p):
    '''
        seen_extra_dimension_array : 
    '''
    compilerManager.incrementDimention()


def p_seen_lim_inf(p):
    '''
        seen_lim_inf : 
    '''
    lowerLimit = p[-1]
    compilerManager.setLowerLimitCurrentDimention(lowerLimit)


def p_seen_lim_sup(p):
    '''
        seen_lim_sup : 
    '''
    upperLimit = p[-1]
    compilerManager.setUpperLimitCurrentDimention(upperLimit)
    compilerManager.computeR()


def p_seen_lBracket_array(p):
    '''
        seen_lBracket_array : 
    '''
    compilerManager.initArrayDeclaration()


def p_seen_rBracket_array(p):
    '''
        seen_rBracket_array : 
    '''
    compilerManager.endArrayDeclaration()


def p_seen_vars(p):
    "seen_vars : "
    # TODO: MAYBE NEEDED
    # if not ('varsTable' in dirFuncionesDict[currentDirFuncion]):
    #    dirFuncionesDict[currentDirFuncion]['varsTable'] = {}
    # if not ('size' in dirFuncionesDict[currentDirFuncion]):
    #    dirFuncionesDict[currentDirFuncion]['size'] = {'local': {'int': 0, 'float': 0, 'boolean': 0},
    #                                                   'temporal': {'int': 0, 'float': 0, 'boolean': 0, 'total': 0}}


def p_varsaux(p):
    '''
      varsaux : COMMA ID seen_ID_var varsaux
              |
      '''


def p_seen_ID_var(p):
    " seen_ID_var : "

    varId = p[-1]
    compilerManager.addVariableToVarTable(varId, False)


def p_tipo(p):
    '''
      tipo : INT seen_tipo
           | FLOAT seen_tipo
           | BOOLEAN seen_tipo

      '''


def p_seen_tipo(p):
    "seen_tipo : "

    currentType = p[-1]
    compilerManager.setCurrentType(currentType)


def p_function(p):
    '''
      function : FUNCTION returnfunctionaux ID seen_id_function params bloque seen_function_end
      '''


def p_seen_id_function(p):
    '''
        seen_id_function :
    '''
    functionName = p[-1]
    compilerManager.addFunctionToDir(functionName, Scope.LOCAL, 'Function')
    compilerManager.setCurrentFunction(functionName)


def p_seen_function_end(p):
    '''
        seen_function_end :
    '''
    compilerManager.endFunction()


def p_functionmain(p):
    '''
      functionmain : MAIN seen_function_main LEFTPARENTHESES RIGHTPARENTHESES bloque
      '''


def p_seen_function_main(p):
    "seen_function_main : "
    programName = p[-1]
    compilerManager.setCurrentFunction(programName)
    compilerManager.addFunctionToDir(programName, Scope.LOCAL, 'Main')
    compilerManager.fillQuad(1, compilerManager.quadrupleCounter)


def p_returnfunctionaux(p):
    '''
      returnfunctionaux : tipo
                | VOID seen_void
      '''


def p_seen_void(p):
    '''
        seen_void :
    '''
    compilerManager.setCurrentType(VarType.VOID)


def p_params(p):
    '''
      params : LEFTPARENTHESES seen_params_init paramsaux RIGHTPARENTHESES
      '''


def p_seen_params_init(p):
    '''
      seen_params_init :
    '''
    compilerManager.addParamsTableToCurrentFunction()


def p_paramsaux(p):
    '''
      paramsaux : tipo ID seen_ID_params paramsaux
                | COMMA paramsaux
                | empty
    '''


def p_seen_ID_params(p):
    " seen_ID_params : "
    varId = p[-1]
    compilerManager.addVariableToVarTable(varId, True)

    # try: TODO: MAYBE NEEDED
    #    if (currentVar in dirFuncionesDict[currentDirFuncion]['varsTable']):
    #        print('Redeclaration on variable', currentVar)
    # except (NameError, AttributeError) as e:
    #    print(e)
    #    pass
    # address = virtualMemoryManager.getNextAddressAvailable(
    #    dirFuncionesDict[currentDirFuncion]['scope'], currentType)

    # dirFuncionesDict[currentDirFuncion]['varsTable'][currentVar] = {
    #    'tipo': currentType, 'address': address}
    # dirFuncionesDict[currentDirFuncion]['paramsTable'].append(currentType)
    # dirFuncionesDict[currentDirFuncion]['size']['local'][currentType] += 1


def p_bloque(p):
    '''
      bloque : LEFTBRACE vars seen_start_bloqueaux bloqueaux RIGHTBRACE
    '''


def p_seen_start_bloqueaux(p):
    '''
      seen_start_bloqueaux : 
    '''
    compilerManager.addFunctionStartAddress()


def p_bloqueaux(p):
    '''
      bloqueaux : estatuto bloqueaux
              |
      '''


def p_estatuto(p):
    '''
      estatuto : asignacion
              | condicion
              | escritura
              | while
              | functionCall

      '''


def p_asignacion(p):
    '''
      asignacion : varcte EQUALS seen_equals expresion seen_final_asignacion SEMICOLON
      '''


def p_seen_equals(p):
    '''
      seen_equals :
      '''
    operator = p[-1]
    compilerManager.addOperatorToStack(operator)


def p_seen_final_asignacion(p):
    '''
      seen_final_asignacion :
      '''
    compilerManager.createAssignationQuad()


def p_expresion(p):
    '''
      expresion : exp seen_comparacion
                | exp seen_comparacion expresionaux exp seen_comparacion
      '''


def p_expresionaux(p):
    '''
      expresionaux : GREATERTHAN seen_operador
                | LESSTHAN seen_operador
                | NOTEQUALS seen_operador
                |
      '''


def p_escritura(p):
    '''
      escritura : PRINT LEFTPARENTHESES escrituraaux RIGHTPARENTHESES SEMICOLON
      '''


def p_escrituraaux(p):
    '''
      escrituraaux : escrituraaux2
                  | escrituraaux2 COMMA escrituraaux
      '''


def p_escrituraaux2(p):
    '''
      escrituraaux2 : expresion seen_print_cuadruplo
                    | STRING_CTE seen_print_cuadruplo
      '''


def p_seen_print_cuadruplo(p):
    '''
      seen_print_cuadruplo : 
      '''
    compilerManager.createPrintQuad()


def p_exp(p):
    '''
              exp : termino seen_termino
                  | termino seen_termino expaux
      '''


def p_expaux(p):
    '''
              expaux : PLUS seen_operador exp
                  | MINUS seen_operador exp
      '''


def p_termino(p):
    '''
            termino : factor seen_factor
                  | factor seen_factor terminoaux
      '''


def p_terminoaux(p):
    '''
            terminoaux : DIVIDE seen_operador termino
                  | MULTIPLY seen_operador termino
      '''


def p_condicion(p):
    '''
        condicion : IF LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_condicion bloque condicionaux
      '''


def p_condicionaux(p):
    '''
        condicionaux : ELSE seen_else bloque SEMICOLON seen_end_condicion
                  | SEMICOLON seen_end_condicion
      '''


def p_seen_right_parentheses_condicion(p):
    '''
        seen_right_parentheses_condicion :
      '''
    compilerManager.handleConditionStart()


def p_seen_else(p):
    '''
        seen_else :
      '''
    compilerManager.handleConditionElse()


def p_seen_end_condicion(p):
    '''
        seen_end_condicion :
      '''
    compilerManager.handleConditionEnd()


def p_factor(p):
    '''
        factor : factoraux
               | varcte
      '''


def p_factoraux(p):
    '''
        factoraux : LEFTPARENTHESES seen_insert_fondo expresion RIGHTPARENTHESES seen_remove_fondo
      '''


def p_varcte(p):
    '''
        varcte : ID seen_ID
                    | INT_CTE seen_CTE_INT
                    | FLOAT_CTE seen_CTE_FLOAT

      '''


def p_seen_CTE_INT(p):
    "seen_CTE_INT :"
    constant = p[-1]
    compilerManager.handleConstant(constant, VarType.INT)


def p_seen_CTE_FLOAT(p):
    "seen_CTE_FLOAT :"
    constant = p[-1]
    compilerManager.handleConstant(constant, VarType.FLOAT)


def p_seen_insert_fondo(p):
    '''
        seen_insert_fondo :
      '''
    compilerManager.addOperatorToStack('(')  # TODO: IMPROVE


def p_seen_remove_fondo(p):
    '''
        seen_remove_fondo :
      '''


def p_seen_ID(p):
    "seen_ID :"
    varId = p[-1]
    compilerManager.addVariableToStack(varId)


def p_seen_operador(p):
    "seen_operador :"
    operator = p[-1]
    compilerManager.addOperatorToStack(operator)


def p_seen_termino(p):
    "seen_termino :"
    compilerManager.handleTermino()


def p_seen_factor(p):
    "seen_factor :"
    compilerManager.handleFactor()


def p_seen_comparacion(p):
    "seen_comparacion :"
    compilerManager.handleComparation()


def p_while(p):
    '''
        while : WHILE seen_while LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_while bloque SEMICOLON seen_end_while
    '''


def p_seen_while(p):
    '''
        seen_while : 
    '''
    compilerManager.addJumpToCurrentQuadruple()


def p_seen_right_parentheses_while(p):
    '''
        seen_right_parentheses_while : 
    '''
    compilerManager.handleWhileStart()


def p_seen_end_while(p):
    '''
        seen_end_while : 
    '''
    compilerManager.handleWhileEnd()


def p_functionCall(p):
    '''
        functionCall : ID seen_fCall_id LEFTPARENTHESES seen_leftp_fCall paramsFunctionCall seen_end_paramsFCall RIGHTPARENTHESES seen_rightp_fCall SEMICOLON
    '''


def p_seen_fCall_id(p):
    '''
        seen_fCall_id : 
    '''
    functionName = p[-1]
    compilerManager.handleFunctionCall(functionName)


def p_seen_leftp_fCall(p):
    '''
        seen_leftp_fCall : 
    '''
    functionName = p[-3]
    compilerManager.handleFunctionCallJump(functionName)


def p_paramsFunctionCall(p):
    '''
        paramsFunctionCall : expresion seen_parameter_fCall COMMA seen_comma_params_fCall paramsFunctionCall 
                        | expresion seen_parameter_fCall seen_comma_params_fCall
    '''


def p_seen_parameter_fCall(p):
    '''
        seen_parameter_fCall : 
    '''
    compilerManager.handleFunctionParameter()


def p_seen_comma_params_fCall(p):
    '''
        seen_comma_params_fCall : 
    '''
    compilerManager.incrementParameterCounter()


def p_seen_end_paramsFCall(p):
    '''
        seen_end_paramsFCall : 
    '''
    compilerManager.checkNoParametersLeft()


def p_seen_rightp_fCall(p):
    '''
        seen_rightp_fCall : 
    '''
    compilerManager.handleEndOfFunctionCall()


# Mensaje de error sintactico


def p_error(p):
    print(p)
    print("Syntax error found!")


def p_empty(p):
    '''
      empty :
      '''


parser = yacc.yacc()


print("1-Load Example from TXT")
print("2-Input code manually")
print('sCOPE', Scope.GLOBAL)
option = input("Option : ")
if option == "1":
    file = open("C:/Users/Moi/Documents/GitHub/CompiMoi/test.txt").read()
    parser.parse(file)
    print('operandos: ', compilerManager.operandsStack)
    print('compilerManager.quadruples: ', compilerManager.quadruples)
    print('directorio funciones: ', compilerManager.functionDirectory)
    print('pila tipos :', compilerManager.typesStack)
elif option == "2":
    file = open(
        "C:/Users/Moi/Documents/GitHub/CompiMoi/test2.txt").read()
    parser.parse(file)
    print('operandos: ', compilerManager.operandsStack)
    print('compilerManager.quadruples: ', compilerManager.quadruples)
    print('directorio funciones: ', compilerManager.functionDirectory)
    print('pila tipos :', compilerManager.typesStack)
elif option == "3":
    file = open(
        "C:/Users/Moi/Documents/GitHub/CompiMoi/test3.txt").read()
    parser.parse(file)
    print('operandos: ', compilerManager.operandsStack)
    cont = 0
    for cuadruplo in compilerManager.quadruples:
        print(cont, cuadruplo)
        cont += 1
    print('compilerManager.quadruples: ', compilerManager.quadruples)
    print('directorio funciones: ', compilerManager.functionDirectory)
    print('pila tipos :', compilerManager.typesStack)
    compilerManager.paramsVm.printParamsVm()
    virtualMachineManager.init(
        compilerManager.quadruples, compilerManager.paramsVm)

else:
    while True:
        try:
            s = input('>> ')
        except EOFError:
            break
        parser.parse(s)
