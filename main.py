import ply.lex as lex
import ply.yacc as yacc
import sys
import json

cuadruplos = []
pilaOperadores = []
pilaOperandos = []
dirFuncionesDict = {}
currentDirFuncion = ''
currentVarTable = ''
currentType = ''
currentVars = []
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
}

tokens = [
    'INT_CTE',
    'FLOAT_CTE',
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
    'int': 'INT',
    'float': 'FLOAT',
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


def p_calc(p): #falta poner main
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
    dirFuncionesDict[p[-1]] = {'type': 'Program'}
    currentDirFuncion = p[-1]

def p_vars(p):
    ''' vars : VAR seen_vars varsaux
                | empty
    '''
    print('hola2?')



def p_seen_vars(p):
    "seen_vars : "

    if(not ('varsTable' in dirFuncionesDict[currentDirFuncion])):
        dirFuncionesDict[currentDirFuncion]['varsTable'] = {}



def p_varsaux(p):
    '''
      varsaux : ID seen_ID_var varsaux2 COLON tipo SEMICOLON varsaux
              |
      '''
    print('hola3?')



def p_varsaux2(p):
    '''
      varsaux2 : COMMA ID seen_ID_var varsaux2
              |
      '''


def p_seen_ID_var(p):
    " seen_ID_var : "
    currentVars.append(p[-1])



def p_tipo(p):
    '''
      tipo : INT seen_tipo
           | FLOAT seen_tipo
      '''

def p_seen_tipo(p):
    "seen_tipo : "
    global currentVars
    tipo = p[-1]
    for currentVar in currentVars:
        try:
            if(currentVar in dirFuncionesDict[currentDirFuncion]['varsTable']):
                print('Redeclaration on variable', currentVar)
        except (NameError, AttributeError) as e:
            print(e)
            pass
        dirFuncionesDict[currentDirFuncion]['varsTable'][currentVar] = {'tipo': tipo}
    currentVars=[]



def p_function(p):
    '''
      function : FUNCTION returnfunctionaux ID params bloque
      '''


def p_functionmain(p):
    '''
      functionmain : MAIN  LEFTPARENTHESES RIGHTPARENTHESES bloque
      '''



def p_returnfunctionaux(p):
    '''
      returnfunctionaux : tipo
                | VOID
      '''



def p_params(p):
    '''
      params : LEFTPARENTHESES paramsaux RIGHTPARENTHESES
      '''
    print('params?', p[-1])

def p_paramsaux(p):
    '''
      paramsaux : ID COLON tipo
                | ID COLON tipo COMMA paramsaux
    '''


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
      '''



def p_asignacion(p):
    '''
      asignacion : varcte EQUALS expresion SEMICOLON
      '''



def p_expresion(p):
    '''
      expresion : exp expresionaux
      '''


def p_expresionaux(p):
    '''
      expresionaux : GREATERTHAN exp
                | LESSTHAN exp
                | NOTEQUALS exp
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
        condicion : IF LEFTPARENTHESES expresion RIGHTPARENTHESES bloque condicionaux
      '''


def p_condicionaux(p):
    '''
        condicionaux : ELSE bloque SEMICOLON
                  | SEMICOLON
      '''


def p_factor(p):
    '''
        factor : factoraux
                  | factoraux2
      '''


def p_factoraux(p):
    '''
        factoraux : LEFTPARENTHESES expresion RIGHTPARENTHESES
      '''


def p_factoraux2(p):
    '''
        factoraux2 : factoraux3 varcte
      '''


def p_factoraux3(p):  # QUE SHOW CON ESTO
    '''
        factoraux3 : PLUS
                    | MINUS
                    |

      '''


def p_varcte(p):
    '''
        varcte : ID seen_ID
                    | INT_CTE
                    | FLOAT_CTE

      '''


def p_seen_ID(p):
    "seen_ID :"
    pilaOperandos.append(p[-1])


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
        operador = pilaOperadores.pop()
        result_type = getResultType()
        if (result_type):
            result = nextAvail()
            cuadruplos.append(generate_quad(
                operador=operador, left_operando=left_operando, right_operando=right_operando, result=result))
            pilaOperandos.append(result)
        else:
            print('ERROR MISMATCH')


def p_seen_factor(p):
    "seen_factor :"
    if (len(pilaOperadores) == 0):
        return
    #print(pilaOperadores)
    #print(pilaOperandos)

    if pilaOperadores[-1] == '*' or pilaOperadores[-1] == '/':
        right_operando = pilaOperandos.pop()
        left_operando = pilaOperandos.pop()
        operador = pilaOperadores.pop()
        result_type = getResultType()
        if (result_type):
            result = nextAvail()
            cuadruplos.append(generate_quad(
                operador=operador, left_operando=left_operando, right_operando=right_operando, result=result))
            pilaOperandos.append(result)
        else:
            print('ERROR MISMATCH')


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
    return [operador, left_operando, right_operando, result]


def nextAvail():
    return 't1'


def getResultType():
    # result_type = cubo_semantico[operador][left_operando][right_operando]
    return 'int'
# Execution
# IMPORTANT
# This version does not accept end of lines, so in order to test code please put it in one line, use this tool if you need to convert to one line
# https://lingojam.com/TexttoOneLine


print("1-Load Example from TXT")
print("2-Input code manually")
option = input("Option : ")
if option == "1":
    file = open("/Users/moiseslopez/Documents/compi2s2/CompiMoi/test.txt").read()
    # print(file)
    parser.parse(file)
    #print(pilaOperandos)
    #print(cuadruplos)
    print(dirFuncionesDict)
    #print(json.dumps(dirFuncionesDict, indent=4))
else:
    while True:
        try:
            s = input('>> ')
        except EOFError:
            break
        parser.parse(s)
