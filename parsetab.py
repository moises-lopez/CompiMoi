
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA DIVIDE ELSE EQUALS FLOAT FLOAT_CTE FUNCTION GREATERTHAN ID IF INT INT_CTE LEFTBRACE LEFTBRACKET LEFTPARENTHESES LESSTHAN MAIN MINUS MULTIPLY NOTEQUAL NOTEQUALS PLUS PRINT PROGRAMA READ RIGHTBRACE RIGHTBRACKET RIGHTPARENTHESES SEMICOLON STRING_CTE VAR VOID\n      calc : PROGRAMA ID seen_program SEMICOLON vars modulesaux functionmain\n     \n      modulesaux : function modulesaux\n           |\n      seen_program :  vars : VAR seen_vars tipo ID seen_ID_var varsaux SEMICOLON vars\n                | empty\n    seen_vars : \n      varsaux : COMMA ID seen_ID_var varsaux\n              |\n       seen_ID_var : \n      tipo : INT seen_tipo\n           | FLOAT seen_tipo\n      seen_tipo : \n      function : FUNCTION returnfunctionaux ID seen_id_function params bloque\n      \n        seen_id_function :\n    \n      functionmain : MAIN LEFTPARENTHESES RIGHTPARENTHESES bloque\n      \n      returnfunctionaux : tipo\n                | VOID seen_void\n      \n        seen_void :\n    \n      params : LEFTPARENTHESES paramsaux RIGHTPARENTHESES\n      \n      paramsaux : ID COLON tipo\n                | ID COLON tipo COMMA paramsaux\n    \n      bloque : LEFTBRACE vars bloqueaux RIGHTBRACE\n      \n      bloqueaux : estatuto bloqueaux\n              |\n      \n      estatuto : asignacion\n              | condicion\n              | escritura\n      \n      asignacion : varcte EQUALS expresion SEMICOLON\n      \n      expresion : exp expresionaux\n      \n      expresionaux : GREATERTHAN exp\n                | LESSTHAN exp\n                | NOTEQUALS exp\n                |\n      \n      escritura : PRINT LEFTPARENTHESES escrituraaux RIGHTPARENTHESES SEMICOLON\n      \n      escrituraaux : expresion\n                  | STRING_CTE\n                  | expresion COMMA escrituraaux\n                  | STRING_CTE COMMA escrituraaux\n      \n              exp : termino seen_termino\n                  | termino seen_termino expaux\n      \n              expaux : PLUS seen_operador exp\n                  | MINUS seen_operador exp\n      \n            termino : factor seen_factor\n                  | factor seen_factor terminoaux\n      \n            terminoaux : DIVIDE seen_operador termino\n                  | MULTIPLY seen_operador termino\n      \n        condicion : IF LEFTPARENTHESES expresion RIGHTPARENTHESES bloque condicionaux\n      \n        condicionaux : ELSE bloque SEMICOLON\n                  | SEMICOLON\n      \n        factor : factoraux\n                  | factoraux2\n      \n        factoraux : LEFTPARENTHESES expresion RIGHTPARENTHESES\n      \n        factoraux2 : factoraux3 varcte\n      \n        factoraux3 : PLUS\n                    | MINUS\n                    |\n\n      \n        varcte : ID seen_ID\n                    | INT_CTE\n                    | FLOAT_CTE\n\n      seen_ID :seen_operador :seen_termino :seen_factor :\n        arrayIntDefinition : LEFTBRACKET INT_CTE RIGHTBRACKET\n    \n      empty :\n      '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,13,31,58,],[0,-1,-16,-23,]),'ID':([2,8,16,17,18,19,20,21,24,25,26,32,34,36,37,41,44,45,46,47,56,60,61,62,72,73,74,75,80,81,83,84,85,92,93,99,100,102,103,106,109,110,111,112,113,115,121,],[3,-6,23,-17,-19,-13,-13,27,-18,-11,-12,-66,40,42,51,-66,51,-26,-27,-28,-5,-57,-57,-57,-57,51,-55,-56,40,-29,-57,-57,-57,-57,-57,-62,-62,-62,-62,-35,-57,-57,-57,-57,-48,-50,-49,]),'SEMICOLON':([3,4,27,30,35,42,51,52,53,57,58,63,65,66,67,68,69,70,71,82,86,87,89,91,95,96,97,98,101,104,105,116,117,118,119,120,],[-4,5,-10,-9,41,-10,-61,-59,-60,-9,-23,-58,-8,81,-34,-63,-64,-51,-52,-30,-40,-44,-54,106,-31,-32,-33,-41,-45,-53,115,-42,-43,-46,-47,121,]),'VAR':([5,32,41,],[7,7,7,]),'FUNCTION':([5,6,8,10,38,41,56,58,],[-66,11,-6,11,-14,-66,-5,-23,]),'MAIN':([5,6,8,9,10,15,38,41,56,58,],[-66,-3,-6,14,-3,-2,-14,-66,-5,-23,]),'INT':([7,11,12,55,],[-7,19,19,19,]),'FLOAT':([7,11,12,55,],[-7,20,20,20,]),'IF':([8,32,37,41,44,45,46,47,56,81,106,113,115,121,],[-6,-66,49,-66,49,-26,-27,-28,-5,-29,-35,-48,-50,-49,]),'PRINT':([8,32,37,41,44,45,46,47,56,81,106,113,115,121,],[-6,-66,50,-66,50,-26,-27,-28,-5,-29,-35,-48,-50,-49,]),'INT_CTE':([8,32,37,41,44,45,46,47,56,60,61,62,72,73,74,75,81,83,84,85,92,93,99,100,102,103,106,109,110,111,112,113,115,121,],[-6,-66,52,-66,52,-26,-27,-28,-5,-57,-57,-57,-57,52,-55,-56,-29,-57,-57,-57,-57,-57,-62,-62,-62,-62,-35,-57,-57,-57,-57,-48,-50,-49,]),'FLOAT_CTE':([8,32,37,41,44,45,46,47,56,60,61,62,72,73,74,75,81,83,84,85,92,93,99,100,102,103,106,109,110,111,112,113,115,121,],[-6,-66,53,-66,53,-26,-27,-28,-5,-57,-57,-57,-57,53,-55,-56,-29,-57,-57,-57,-57,-57,-62,-62,-62,-62,-35,-57,-57,-57,-57,-48,-50,-49,]),'RIGHTBRACE':([8,32,37,41,43,44,45,46,47,56,59,81,106,113,115,121,],[-6,-66,-25,-66,58,-25,-26,-27,-28,-5,-24,-29,-35,-48,-50,-49,]),'VOID':([11,],[18,]),'LEFTPARENTHESES':([14,23,29,49,50,60,61,62,72,83,84,85,92,93,99,100,102,103,109,110,111,112,],[22,-15,34,61,62,72,72,72,72,72,72,72,72,72,-62,-62,-62,-62,72,72,72,72,]),'COMMA':([19,20,25,26,27,30,42,51,52,53,57,63,64,67,68,69,70,71,78,79,82,86,87,89,95,96,97,98,101,104,116,117,118,119,],[-13,-13,-11,-12,-10,36,-10,-61,-59,-60,36,-58,80,-34,-63,-64,-51,-52,92,93,-30,-40,-44,-54,-31,-32,-33,-41,-45,-53,-42,-43,-46,-47,]),'RIGHTPARENTHESES':([19,20,22,25,26,39,51,52,53,63,64,67,68,69,70,71,76,77,78,79,82,86,87,88,89,94,95,96,97,98,101,104,107,108,116,117,118,119,],[-13,-13,28,-11,-12,54,-61,-59,-60,-58,-21,-34,-63,-64,-51,-52,90,91,-36,-37,-30,-40,-44,104,-54,-22,-31,-32,-33,-41,-45,-53,-38,-39,-42,-43,-46,-47,]),'LEFTBRACE':([28,33,54,90,114,],[32,32,-20,32,32,]),'COLON':([40,],[55,]),'EQUALS':([48,51,52,53,63,],[60,-61,-59,-60,-58,]),'DIVIDE':([51,52,53,63,69,70,71,87,89,104,],[-61,-59,-60,-58,-64,-51,-52,102,-54,-53,]),'MULTIPLY':([51,52,53,63,69,70,71,87,89,104,],[-61,-59,-60,-58,-64,-51,-52,103,-54,-53,]),'PLUS':([51,52,53,60,61,62,63,68,69,70,71,72,83,84,85,86,87,89,92,93,99,100,101,102,103,104,109,110,111,112,118,119,],[-61,-59,-60,74,74,74,-58,-63,-64,-51,-52,74,74,74,74,99,-44,-54,74,74,-62,-62,-45,-62,-62,-53,74,74,74,74,-46,-47,]),'MINUS':([51,52,53,60,61,62,63,68,69,70,71,72,83,84,85,86,87,89,92,93,99,100,101,102,103,104,109,110,111,112,118,119,],[-61,-59,-60,75,75,75,-58,-63,-64,-51,-52,75,75,75,75,100,-44,-54,75,75,-62,-62,-45,-62,-62,-53,75,75,75,75,-46,-47,]),'GREATERTHAN':([51,52,53,63,67,68,69,70,71,86,87,89,98,101,104,116,117,118,119,],[-61,-59,-60,-58,83,-63,-64,-51,-52,-40,-44,-54,-41,-45,-53,-42,-43,-46,-47,]),'LESSTHAN':([51,52,53,63,67,68,69,70,71,86,87,89,98,101,104,116,117,118,119,],[-61,-59,-60,-58,84,-63,-64,-51,-52,-40,-44,-54,-41,-45,-53,-42,-43,-46,-47,]),'NOTEQUALS':([51,52,53,63,67,68,69,70,71,86,87,89,98,101,104,116,117,118,119,],[-61,-59,-60,-58,85,-63,-64,-51,-52,-40,-44,-54,-41,-45,-53,-42,-43,-46,-47,]),'ELSE':([58,105,],[-23,114,]),'STRING_CTE':([62,92,93,],[79,79,79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'seen_program':([3,],[4,]),'vars':([5,32,41,],[6,37,56,]),'empty':([5,32,41,],[8,8,8,]),'modulesaux':([6,10,],[9,15,]),'function':([6,10,],[10,10,]),'seen_vars':([7,],[12,]),'functionmain':([9,],[13,]),'returnfunctionaux':([11,],[16,]),'tipo':([11,12,55,],[17,21,64,]),'seen_void':([18,],[24,]),'seen_tipo':([19,20,],[25,26,]),'seen_id_function':([23,],[29,]),'seen_ID_var':([27,42,],[30,57,]),'bloque':([28,33,90,114,],[31,38,105,120,]),'params':([29,],[33,]),'varsaux':([30,57,],[35,65,]),'paramsaux':([34,80,],[39,94,]),'bloqueaux':([37,44,],[43,59,]),'estatuto':([37,44,],[44,44,]),'asignacion':([37,44,],[45,45,]),'condicion':([37,44,],[46,46,]),'escritura':([37,44,],[47,47,]),'varcte':([37,44,73,],[48,48,89,]),'seen_ID':([51,],[63,]),'expresion':([60,61,62,72,92,93,],[66,76,78,88,78,78,]),'exp':([60,61,62,72,83,84,85,92,93,109,110,],[67,67,67,67,95,96,97,67,67,116,117,]),'termino':([60,61,62,72,83,84,85,92,93,109,110,111,112,],[68,68,68,68,68,68,68,68,68,68,68,118,119,]),'factor':([60,61,62,72,83,84,85,92,93,109,110,111,112,],[69,69,69,69,69,69,69,69,69,69,69,69,69,]),'factoraux':([60,61,62,72,83,84,85,92,93,109,110,111,112,],[70,70,70,70,70,70,70,70,70,70,70,70,70,]),'factoraux2':([60,61,62,72,83,84,85,92,93,109,110,111,112,],[71,71,71,71,71,71,71,71,71,71,71,71,71,]),'factoraux3':([60,61,62,72,83,84,85,92,93,109,110,111,112,],[73,73,73,73,73,73,73,73,73,73,73,73,73,]),'escrituraaux':([62,92,93,],[77,107,108,]),'expresionaux':([67,],[82,]),'seen_termino':([68,],[86,]),'seen_factor':([69,],[87,]),'expaux':([86,],[98,]),'terminoaux':([87,],[101,]),'seen_operador':([99,100,102,103,],[109,110,111,112,]),'condicionaux':([105,],[113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> PROGRAMA ID seen_program SEMICOLON vars modulesaux functionmain','calc',7,'p_calc','main.py',230),
  ('modulesaux -> function modulesaux','modulesaux',2,'p_modulesaux','main.py',236),
  ('modulesaux -> <empty>','modulesaux',0,'p_modulesaux','main.py',237),
  ('seen_program -> <empty>','seen_program',0,'p_seen_program','main.py',243),
  ('vars -> VAR seen_vars tipo ID seen_ID_var varsaux SEMICOLON vars','vars',8,'p_vars','main.py',249),
  ('vars -> empty','vars',1,'p_vars','main.py',250),
  ('seen_vars -> <empty>','seen_vars',0,'p_seen_vars','main.py',256),
  ('varsaux -> COMMA ID seen_ID_var varsaux','varsaux',4,'p_varsaux','main.py',264),
  ('varsaux -> <empty>','varsaux',0,'p_varsaux','main.py',265),
  ('seen_ID_var -> <empty>','seen_ID_var',0,'p_seen_ID_var','main.py',270),
  ('tipo -> INT seen_tipo','tipo',2,'p_tipo','main.py',283),
  ('tipo -> FLOAT seen_tipo','tipo',2,'p_tipo','main.py',284),
  ('seen_tipo -> <empty>','seen_tipo',0,'p_seen_tipo','main.py',288),
  ('function -> FUNCTION returnfunctionaux ID seen_id_function params bloque','function',6,'p_function','main.py',296),
  ('seen_id_function -> <empty>','seen_id_function',0,'p_seen_id_function','main.py',302),
  ('functionmain -> MAIN LEFTPARENTHESES RIGHTPARENTHESES bloque','functionmain',4,'p_functionmain','main.py',310),
  ('returnfunctionaux -> tipo','returnfunctionaux',1,'p_returnfunctionaux','main.py',317),
  ('returnfunctionaux -> VOID seen_void','returnfunctionaux',2,'p_returnfunctionaux','main.py',318),
  ('seen_void -> <empty>','seen_void',0,'p_seen_void','main.py',324),
  ('params -> LEFTPARENTHESES paramsaux RIGHTPARENTHESES','params',3,'p_params','main.py',332),
  ('paramsaux -> ID COLON tipo','paramsaux',3,'p_paramsaux','main.py',337),
  ('paramsaux -> ID COLON tipo COMMA paramsaux','paramsaux',5,'p_paramsaux','main.py',338),
  ('bloque -> LEFTBRACE vars bloqueaux RIGHTBRACE','bloque',4,'p_bloque','main.py',344),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','main.py',350),
  ('bloqueaux -> <empty>','bloqueaux',0,'p_bloqueaux','main.py',351),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','main.py',358),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','main.py',359),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','main.py',360),
  ('asignacion -> varcte EQUALS expresion SEMICOLON','asignacion',4,'p_asignacion','main.py',367),
  ('expresion -> exp expresionaux','expresion',2,'p_expresion','main.py',374),
  ('expresionaux -> GREATERTHAN exp','expresionaux',2,'p_expresionaux','main.py',380),
  ('expresionaux -> LESSTHAN exp','expresionaux',2,'p_expresionaux','main.py',381),
  ('expresionaux -> NOTEQUALS exp','expresionaux',2,'p_expresionaux','main.py',382),
  ('expresionaux -> <empty>','expresionaux',0,'p_expresionaux','main.py',383),
  ('escritura -> PRINT LEFTPARENTHESES escrituraaux RIGHTPARENTHESES SEMICOLON','escritura',5,'p_escritura','main.py',389),
  ('escrituraaux -> expresion','escrituraaux',1,'p_escrituraaux','main.py',395),
  ('escrituraaux -> STRING_CTE','escrituraaux',1,'p_escrituraaux','main.py',396),
  ('escrituraaux -> expresion COMMA escrituraaux','escrituraaux',3,'p_escrituraaux','main.py',397),
  ('escrituraaux -> STRING_CTE COMMA escrituraaux','escrituraaux',3,'p_escrituraaux','main.py',398),
  ('exp -> termino seen_termino','exp',2,'p_exp','main.py',404),
  ('exp -> termino seen_termino expaux','exp',3,'p_exp','main.py',405),
  ('expaux -> PLUS seen_operador exp','expaux',3,'p_expaux','main.py',411),
  ('expaux -> MINUS seen_operador exp','expaux',3,'p_expaux','main.py',412),
  ('termino -> factor seen_factor','termino',2,'p_termino','main.py',418),
  ('termino -> factor seen_factor terminoaux','termino',3,'p_termino','main.py',419),
  ('terminoaux -> DIVIDE seen_operador termino','terminoaux',3,'p_terminoaux','main.py',425),
  ('terminoaux -> MULTIPLY seen_operador termino','terminoaux',3,'p_terminoaux','main.py',426),
  ('condicion -> IF LEFTPARENTHESES expresion RIGHTPARENTHESES bloque condicionaux','condicion',6,'p_condicion','main.py',432),
  ('condicionaux -> ELSE bloque SEMICOLON','condicionaux',3,'p_condicionaux','main.py',438),
  ('condicionaux -> SEMICOLON','condicionaux',1,'p_condicionaux','main.py',439),
  ('factor -> factoraux','factor',1,'p_factor','main.py',445),
  ('factor -> factoraux2','factor',1,'p_factor','main.py',446),
  ('factoraux -> LEFTPARENTHESES expresion RIGHTPARENTHESES','factoraux',3,'p_factoraux','main.py',452),
  ('factoraux2 -> factoraux3 varcte','factoraux2',2,'p_factoraux2','main.py',458),
  ('factoraux3 -> PLUS','factoraux3',1,'p_factoraux3','main.py',464),
  ('factoraux3 -> MINUS','factoraux3',1,'p_factoraux3','main.py',465),
  ('factoraux3 -> <empty>','factoraux3',0,'p_factoraux3','main.py',466),
  ('varcte -> ID seen_ID','varcte',2,'p_varcte','main.py',473),
  ('varcte -> INT_CTE','varcte',1,'p_varcte','main.py',474),
  ('varcte -> FLOAT_CTE','varcte',1,'p_varcte','main.py',475),
  ('seen_ID -> <empty>','seen_ID',0,'p_seen_ID','main.py',481),
  ('seen_operador -> <empty>','seen_operador',0,'p_seen_operador','main.py',486),
  ('seen_termino -> <empty>','seen_termino',0,'p_seen_termino','main.py',491),
  ('seen_factor -> <empty>','seen_factor',0,'p_seen_factor','main.py',509),
  ('arrayIntDefinition -> LEFTBRACKET INT_CTE RIGHTBRACKET','arrayIntDefinition',3,'p_arrayIntDefinition','main.py',531),
  ('empty -> <empty>','empty',0,'p_empty','main.py',545),
]
