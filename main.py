import ply.lex as lex
import ply.yacc as yacc
import sys
import json
from virtualMemory import VirtualMemory

virtualMemoryManager = VirtualMemory()
cuadruplos = [[]]
pilaOperadores = []
pilaOperandos = []
pilaTipos = []
dirFuncionesDict = {}
currentDirFuncion = ''
currentVarTable = ''
currentType = ''
currentVars = []
programName = ''
pilaSaltos = []
contadorCuadruplos = 1
cubo_semantico = {
    '*': {
        'float': {
            'int': 'float',
            'float': 'float'
        },
        'int': {
            'int': 'int',
            'float': 'float'
        }
    },
    '/': {
        'float': {
            'int': 'float',
            'float': 'float'
        },
        'int': {
            'int': 'int',
            'float': 'float'
        }
    },
    '-': {
        'float': {
            'int': 'float',
            'float': 'float'
        },
        'int': {
            'int': 'int',
            'float': 'float'
        }
    },
    '+': {
        'float': {
            'int': 'float',
            'float': 'float'
        },
        'int': {
            'int': 'int',
            'float': 'float'
        }
    },
    '<': {
        'float': {
            'int': 'boolean',
            'float': 'boolean'
        },
        'int': {
            'int': 'boolean',
            'float': 'boolean'
        }
    },
    '>': {
        'float': {
            'int': 'boolean',
            'float': 'boolean'
        },
        'int': {
            'int': 'boolean',
            'float': 'boolean'
        }
    },
    '!=': {
        'float': {
            'int': 'boolean',
            'float': 'boolean'
        },
        'int': {
            'int': 'boolean',
            'float': 'boolean'
        }
    },
}

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
    r'do'
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
    global currentDirFuncion
    global programName
    dirFuncionesDict[p[-1]] = {'type': 'Program', 'scope': 'global'}
    currentDirFuncion = p[-1]
    programName = p[-1]


def p_vars(p):
    ''' vars : VAR seen_vars tipo ID seen_ID_var varsaux SEMICOLON vars
                | empty
    '''


def p_seen_vars(p):
    "seen_vars : "

    if not ('varsTable' in dirFuncionesDict[currentDirFuncion]):
        dirFuncionesDict[currentDirFuncion]['varsTable'] = {}
    if not ('size' in dirFuncionesDict[currentDirFuncion]):
        dirFuncionesDict[currentDirFuncion]['size'] = {'local': {'int': 0, 'float': 0, 'boolean': 0},
                                                       'temporal': {'int': 0, 'float': 0, 'boolean': 0, 'total': 0}}


def p_seen_vars_end(p):
    "seen_vars_end : "
    print()
    for key in dirFuncionesDict[currentDirFuncion]['varsTable']:
        if dirFuncionesDict[currentDirFuncion]['varsTable'][key]['tipo'] == 'int':
            dirFuncionesDict[currentDirFuncion]['size']['local']['int'] += 1
        elif dirFuncionesDict[currentDirFuncion]['varsTable'][key]['tipo'] == 'float':
            dirFuncionesDict[currentDirFuncion]['size']['local']['float'] += 1
        elif dirFuncionesDict[currentDirFuncion]['varsTable'][key]['tipo'] == 'boolean':
            dirFuncionesDict[currentDirFuncion]['size']['local']['boolean'] += 1
    dirFuncionesDict[currentDirFuncion]['functionStart'] = contadorCuadruplos


def p_varsaux(p):
    '''
      varsaux : COMMA ID seen_ID_var varsaux
              |
      '''


def p_seen_ID_var(p):
    " seen_ID_var : "
    currentVar = p[-1]
    try:
        if (currentVar in dirFuncionesDict[currentDirFuncion]['varsTable']):
            print('Redeclaration on variable', currentVar)
    except (NameError, AttributeError) as e:
        print(e)
        pass
    address = virtualMemoryManager.getNextAddressAvailable(
        dirFuncionesDict[currentDirFuncion]['scope'], currentType)
    dirFuncionesDict[currentDirFuncion]['varsTable'][currentVar] = {
        'tipo': currentType, 'address': address}
    dirFuncionesDict[currentDirFuncion]['size']['local'][currentType] += 1


def p_tipo(p):
    '''
      tipo : INT seen_tipo
           | FLOAT seen_tipo
           | BOOLEAN seen_tipo

      '''


def p_seen_tipo(p):
    "seen_tipo : "
    global currentType
    currentType = p[-1]


def p_function(p):
    '''
      function : FUNCTION returnfunctionaux ID seen_id_function params bloque seen_function_end
      '''


def p_seen_id_function(p):
    '''
        seen_id_function :
    '''
    global currentDirFuncion
    dirFuncionesDict[p[-1]] = {'type': currentType, 'scope': 'local'}
    currentDirFuncion = p[-1]


def p_seen_function_end(p):
    '''
        seen_function_end :
    '''
    # dirFuncionesDict[currentDirFuncion]['varsTable'] = {} DESCOMENTAR, POR EL MOMENTO LO DEJO ASí PARA LOGGEARLO AL FINAL
    virtualMemoryManager.dumpLocalVirtualMemory()
    generate_quad(operador='ENDFUNC', left_operando='',
                  right_operando='', result='')


def p_functionmain(p):
    '''
      functionmain : MAIN seen_function_main LEFTPARENTHESES RIGHTPARENTHESES bloque
      '''


def p_seen_function_main(p):
    "seen_function_main : "
    global currentDirFuncion
    dirFuncionesDict[p[-1]] = {'type': 'Program', 'scope': 'local'}
    currentDirFuncion = p[-1]


def p_returnfunctionaux(p):
    '''
      returnfunctionaux : tipo
                | VOID seen_void
      '''


def p_seen_void(p):
    '''
        seen_void :
    '''
    global currentType
    currentType = 'void'


def p_params(p):
    '''
      params : LEFTPARENTHESES seen_params_init paramsaux RIGHTPARENTHESES
      '''


def p_seen_params_init(p):
    '''
      seen_params_init :
    '''
    if (not ('varsTable' in dirFuncionesDict[currentDirFuncion])):
        dirFuncionesDict[currentDirFuncion]['varsTable'] = {}
        dirFuncionesDict[currentDirFuncion]['paramsTable'] = []
        dirFuncionesDict[currentDirFuncion]['size'] = {'local': {'int': 0, 'float': 0, 'boolean': 0},
                                                       'temporal': {'int': 0, 'float': 0, 'boolean': 0, 'total': 0}}


def p_seen_params_end(p):
    '''
      seen_params_end :
    '''
    for key in dirFuncionesDict[currentDirFuncion]['varsTable']:
        if dirFuncionesDict[currentDirFuncion]['varsTable'][key]['tipo'] == 'int':
            dirFuncionesDict[currentDirFuncion]['size']['local']['int'] += 1
        elif dirFuncionesDict[currentDirFuncion]['varsTable'][key]['tipo'] == 'float':
            dirFuncionesDict[currentDirFuncion]['size']['local']['float'] += 1
        elif dirFuncionesDict[currentDirFuncion]['varsTable'][key]['tipo'] == 'boolean':
            dirFuncionesDict[currentDirFuncion]['size']['local']['boolean'] += 1


def p_paramsaux(p):
    '''
      paramsaux : tipo ID seen_ID_params paramsaux
                | COMMA paramsaux
                | empty
    '''


def p_seen_ID_params(p):
    " seen_ID_params : "
    currentVar = p[-1]
    try:
        if (currentVar in dirFuncionesDict[currentDirFuncion]['varsTable']):
            print('Redeclaration on variable', currentVar)
    except (NameError, AttributeError) as e:
        print(e)
        pass
    address = virtualMemoryManager.getNextAddressAvailable(
        dirFuncionesDict[currentDirFuncion]['scope'], currentType)

    dirFuncionesDict[currentDirFuncion]['varsTable'][currentVar] = {
        'tipo': currentType, 'address': address}
    dirFuncionesDict[currentDirFuncion]['paramsTable'].append(currentType)
    dirFuncionesDict[currentDirFuncion]['size']['local'][currentType] += 1


def p_bloque(p):
    '''
      bloque : LEFTBRACE vars bloqueaux RIGHTBRACE
    '''


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

      '''


def p_asignacion(p):
    '''
      asignacion : varcte EQUALS seen_equals expresion seen_final_asignacion SEMICOLON
      '''


def p_seen_equals(p):
    '''
      seen_equals :
      '''
    pilaOperadores.append(p[-1])


def p_seen_final_asignacion(p):
    '''
      seen_final_asignacion :
      '''
    right_operando = pilaOperandos.pop()
    left_operando = pilaOperandos.pop()
    right_tipo = pilaTipos.pop()
    left_tipo = pilaTipos.pop()
    operador = pilaOperadores.pop()

    if (right_tipo == left_tipo):
        generate_quad(operador=operador, left_operando=right_operando,
                      right_operando='', result=left_operando)
    else:
        print('ERROR MISMATCH')


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
      escrituraaux : expresion
                  | STRING_CTE
                  | expresion COMMA escrituraaux
                  | STRING_CTE COMMA escrituraaux
      '''


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
    exp_type = pilaTipos.pop()

    if (exp_type != 'boolean'):
        print('ERROR MISMATCH IN CONDITION')
    else:
        result = pilaOperandos.pop()
        generate_quad(operador='GOTOF', left_operando=result,
                      right_operando='', result='')
        pilaSaltos.append(contadorCuadruplos - 1)


def p_seen_else(p):
    '''
        seen_else :
      '''
    generate_quad(operador='GOTO', left_operando='',
                  right_operando='', result='')
    false = pilaSaltos.pop()
    pilaSaltos.append(contadorCuadruplos - 1)

    fill(false, contadorCuadruplos)


def p_seen_end_condicion(p):
    '''
        seen_end_condicion :
      '''
    end = pilaSaltos.pop()
    fill(end, contadorCuadruplos)


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
    address = virtualMemoryManager.setConstantInVirtualMemory(str(constant))

    pilaOperandos.append(address)
    pilaTipos.append('int')


def p_seen_CTE_FLOAT(p):
    "seen_CTE_FLOAT :"
    constant = p[-1]
    address = virtualMemoryManager.setConstantInVirtualMemory(str(constant))

    pilaOperandos.append(address)
    pilaTipos.append('float')


def p_seen_insert_fondo(p):
    '''
        seen_insert_fondo :
      '''
    pilaOperadores.append('(')


def p_seen_remove_fondo(p):
    '''
        seen_remove_fondo :
      '''
    if (pilaOperadores[-1] != '('):
        print('Parentesis Mismatch')
    else:
        pilaOperadores.pop()


def p_seen_ID(p):
    "seen_ID :"
    varId = p[-1]
    tipo = ''
    if (varId in dirFuncionesDict[currentDirFuncion]['varsTable']):
        tipo = dirFuncionesDict[currentDirFuncion]['varsTable'][varId]['tipo']
    elif (varId in dirFuncionesDict[programName]['varsTable']):
        tipo = dirFuncionesDict[programName]['varsTable'][varId]['tipo']

    if (tipo == ''):
        print('no se encontró variable', varId)
    pilaOperandos.append(p[-1])
    pilaTipos.append(tipo)


def p_seen_operador(p):
    "seen_operador :"
    pilaOperadores.append(p[-1])


def p_seen_termino(p):
    "seen_termino :"
    if (len(pilaOperadores) == 0):
        return
    if pilaOperadores[-1] == '+' or pilaOperadores[-1] == '-':
        right_operando = pilaOperandos.pop()
        left_operando = pilaOperandos.pop()
        right_tipo = pilaTipos.pop()
        left_tipo = pilaTipos.pop()
        operador = pilaOperadores.pop()
        result_type = getResultType(
            right_tipo=right_tipo, left_tipo=left_tipo, operador=operador)
        if (result_type):
            result = nextAvail(result_type)
            generate_quad(operador=operador, left_operando=left_operando,
                          right_operando=right_operando, result=result)
            pilaOperandos.append(result)
            pilaTipos.append(result_type)
        else:
            print('ERROR MISMATCH')


def p_seen_factor(p):
    "seen_factor :"
    if (len(pilaOperadores) == 0):
        return
    if pilaOperadores[-1] == '*' or pilaOperadores[-1] == '/':
        right_operando = pilaOperandos.pop()
        left_operando = pilaOperandos.pop()
        right_tipo = pilaTipos.pop()
        left_tipo = pilaTipos.pop()
        operador = pilaOperadores.pop()
        result_type = getResultType(
            right_tipo=right_tipo, left_tipo=left_tipo, operador=operador)
        if (result_type):
            result = nextAvail(result_type)
            generate_quad(
                operador=operador, left_operando=left_operando, right_operando=right_operando, result=result)
            pilaOperandos.append(result)
            pilaTipos.append(result_type)
        else:
            print('ERROR MISMATCH')


def p_seen_comparacion(p):
    "seen_comparacion :"
    print('comparacion')
    print('operadores here', pilaOperadores)
    if (len(pilaOperadores) == 0):
        return
    print('1operandos: ', pilaOperandos)
    print('1cuadruplos: ', cuadruplos)
    print('1directorio funciones: ', dirFuncionesDict)
    print('1pila tipos :', pilaTipos)
    if pilaOperadores[-1] == '>' or pilaOperadores[-1] == '<' or pilaOperadores[-1] == '!=':
        right_operando = pilaOperandos.pop()
        left_operando = pilaOperandos.pop()
        right_tipo = pilaTipos.pop()
        left_tipo = pilaTipos.pop()
        operador = pilaOperadores.pop()
        result_type = getResultType(
            right_tipo=right_tipo, left_tipo=left_tipo, operador=operador)
        print('testeo', right_operando, left_operando, right_tipo,
              left_tipo, operador, result_type)
        if (result_type):
            result = nextAvail(result_type)
            generate_quad(
                operador=operador, left_operando=left_operando, right_operando=right_operando, result=result)
            pilaOperandos.append(result)
            pilaTipos.append(result_type)
        else:
            print('ERROR MISMATCH')


def p_while(p):
    '''
        while : WHILE seen_while LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_while bloque SEMICOLON seen_end_while
    '''


def p_seen_while(p):
    '''
        seen_while : 
    '''
    pilaSaltos.append(contadorCuadruplos)


def p_seen_right_parentheses_while(p):
    '''
        seen_right_parentheses_while : 
    '''
    exp_type = pilaTipos.pop()
    if (exp_type != 'boolean'):
        print('ERROR MISMATCH WHILE')
    else:
        result = pilaOperandos.pop()
        generate_quad(operador='GOTOF', left_operando=result,
                      right_operando='', result='')
        pilaSaltos.append(contadorCuadruplos - 1)


def p_seen_end_while(p):
    '''
        seen_end_while : 
    '''
    end = pilaSaltos.pop()
    returnQuad = pilaSaltos.pop()
    generate_quad(operador='GOTO', left_operando='',
                  right_operando='', result=returnQuad)
    fill(numeroCuadrupASaltar=contadorCuadruplos, numeroCuadruploALlenar=end)


def p_arrayIntDefinition(p):
    '''
        arrayIntDefinition : LEFTBRACKET INT_CTE RIGHTBRACKET
    '''


# Mensaje de error sintactico


def p_error(p):
    print(p)
    print("Syntax error found!")


def p_empty(p):
    '''
      empty :
      '''


parser = yacc.yacc()


def generate_quad(operador, left_operando, right_operando, result):
    global contadorCuadruplos
    contadorCuadruplos = contadorCuadruplos + 1
    cuadruplos.append([operador, left_operando, right_operando, result])


def nextAvail(tempType):
    print(dirFuncionesDict[currentDirFuncion])
    dirFuncionesDict[currentDirFuncion]['size']['temporal'][tempType] += 1
    dirFuncionesDict[currentDirFuncion]['size']['temporal']['total'] += 1
    return 't' + str(dirFuncionesDict[currentDirFuncion]['size']['temporal']['total'])


def getResultType(right_tipo, left_tipo, operador):
    result_type = cubo_semantico[operador][left_tipo][right_tipo]
    return result_type


def fill(numeroCuadruploALlenar, numeroCuadrupASaltar):
    print('fill', numeroCuadrupASaltar, numeroCuadruploALlenar)
    print('cuadruplos fill', cuadruplos)
    print('this is the hcuadruplo', cuadruplos[3][3])
    cuadruplos[numeroCuadruploALlenar][3] = numeroCuadrupASaltar


# Execution
# IMPORTANT
# https://lingojam.com/TexttoOneLine


print("1-Load Example from TXT")
print("2-Input code manually")
option = input("Option : ")
if option == "1":
    file = open("C:/Users/Moi/Documents/GitHub/CompiMoi/test.txt").read()
    parser.parse(file)
    print('operandos: ', pilaOperandos)
    print('cuadruplos: ', cuadruplos)
    print('directorio funciones: ', dirFuncionesDict)
    print('pila tipos :', pilaTipos)
elif option == "2":
    file = open(
        "C:/Users/Moi/Documents/GitHub/CompiMoi/test2.txt").read()
    parser.parse(file)
    print('operandos: ', pilaOperandos)
    print('cuadruplos: ', cuadruplos)
    print('directorio funciones: ', dirFuncionesDict)
    print('pila tipos :', pilaTipos)
else:
    while True:
        try:
            s = input('>> ')
        except EOFError:
            break
        parser.parse(s)
