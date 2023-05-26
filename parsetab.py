
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA DIVIDE ELSE EQUALS FLOAT FLOAT_CTE FUNCTION GREATERTHAN ID IF INT INT_CTE LEFTBRACE LEFTBRACKET LEFTPARENTHESES LESSTHAN MAIN MINUS MULTIPLY NOTEQUAL NOTEQUALS PLUS PRINT PROGRAMA READ RIGHTBRACE RIGHTBRACKET RIGHTPARENTHESES SEMICOLON STRING_CTE VAR VOID\n      calc : PROGRAMA ID seen_program SEMICOLON vars modulesaux functionmain\n     \n      modulesaux : function modulesaux\n           |\n      seen_program :  vars : VAR seen_vars tipo ID seen_ID_var varsaux SEMICOLON vars\n                | empty\n    seen_vars : \n      varsaux : COMMA ID seen_ID_var varsaux\n              |\n       seen_ID_var : \n      tipo : INT seen_tipo\n           | FLOAT seen_tipo\n      seen_tipo : \n      function : FUNCTION returnfunctionaux ID seen_id_function params bloque\n      \n        seen_id_function :\n    \n      functionmain : MAIN LEFTPARENTHESES RIGHTPARENTHESES bloque\n      \n      returnfunctionaux : tipo\n                | VOID seen_void\n      \n        seen_void :\n    \n      params : LEFTPARENTHESES seen_params_init paramsaux RIGHTPARENTHESES\n      \n      seen_params_init :\n    \n      paramsaux : tipo ID seen_ID_var paramsaux\n                | COMMA paramsaux\n                | empty\n    \n      bloque : LEFTBRACE vars bloqueaux RIGHTBRACE\n    \n      bloqueaux : estatuto bloqueaux\n              |\n      \n      estatuto : asignacion\n              | condicion\n              | escritura\n      \n      asignacion : varcte EQUALS expresion SEMICOLON\n      \n      expresion : exp expresionaux\n      \n      expresionaux : GREATERTHAN exp\n                | LESSTHAN exp\n                | NOTEQUALS exp\n                |\n      \n      escritura : PRINT LEFTPARENTHESES escrituraaux RIGHTPARENTHESES SEMICOLON\n      \n      escrituraaux : expresion\n                  | STRING_CTE\n                  | expresion COMMA escrituraaux\n                  | STRING_CTE COMMA escrituraaux\n      \n              exp : termino seen_termino\n                  | termino seen_termino expaux\n      \n              expaux : PLUS seen_operador exp\n                  | MINUS seen_operador exp\n      \n            termino : factor seen_factor\n                  | factor seen_factor terminoaux\n      \n            terminoaux : DIVIDE seen_operador termino\n                  | MULTIPLY seen_operador termino\n      \n        condicion : IF LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_condicion bloque condicionaux\n      \n        condicionaux : ELSE seen_else bloque SEMICOLON seen_end_condicion\n                  | SEMICOLON seen_end_condicion\n      \n        seen_right_parentheses_condicion :\n      \n        seen_else :\n      \n        seen_end_condicion :\n      \n        factor : factoraux\n               | varcte\n      \n        factoraux : LEFTPARENTHESES seen_insert_fondo expresion RIGHTPARENTHESES seen_remove_fondo\n      \n        varcte : ID seen_ID\n                    | INT_CTE\n                    | FLOAT_CTE\n\n      \n        seen_insert_fondo :\n      \n        seen_remove_fondo :\n      seen_ID :seen_operador :seen_termino :seen_factor :\n        arrayIntDefinition : LEFTBRACKET INT_CTE RIGHTBRACKET\n    \n      empty :\n      '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,13,31,59,],[0,-1,-16,-25,]),'ID':([2,8,16,17,18,19,20,21,24,25,26,32,36,37,40,43,44,45,46,54,57,61,62,63,75,81,83,84,85,88,91,92,98,99,101,102,105,108,109,110,111,119,121,123,125,126,],[3,-6,23,-17,-19,-13,-13,27,-18,-11,-12,-69,41,50,-69,50,-28,-29,-30,66,-5,50,50,50,-62,-31,50,50,50,50,50,50,-65,-65,-65,-65,-37,50,50,50,50,-50,-55,-52,-55,-51,]),'SEMICOLON':([3,4,27,30,35,41,50,51,52,58,59,64,68,69,70,71,72,73,74,82,86,87,90,94,95,96,97,100,112,113,114,115,116,117,118,124,],[-4,5,-10,-9,40,-10,-64,-60,-61,-9,-25,-59,-8,-57,81,-36,-66,-67,-56,-32,-42,-46,105,-33,-34,-35,-43,-47,-63,121,-44,-45,-48,-49,-58,125,]),'VAR':([5,32,40,],[7,7,7,]),'FUNCTION':([5,6,8,10,38,40,57,59,],[-69,11,-6,11,-14,-69,-5,-25,]),'MAIN':([5,6,8,9,10,15,38,40,57,59,],[-69,-3,-6,14,-3,-2,-14,-69,-5,-25,]),'INT':([7,11,12,34,39,55,66,80,],[-7,19,19,-21,19,19,-10,19,]),'FLOAT':([7,11,12,34,39,55,66,80,],[-7,20,20,-21,20,20,-10,20,]),'IF':([8,32,37,40,43,44,45,46,57,81,105,119,121,123,125,126,],[-6,-69,48,-69,48,-28,-29,-30,-5,-31,-37,-50,-55,-52,-55,-51,]),'PRINT':([8,32,37,40,43,44,45,46,57,81,105,119,121,123,125,126,],[-6,-69,49,-69,49,-28,-29,-30,-5,-31,-37,-50,-55,-52,-55,-51,]),'INT_CTE':([8,32,37,40,43,44,45,46,57,61,62,63,75,81,83,84,85,88,91,92,98,99,101,102,105,108,109,110,111,119,121,123,125,126,],[-6,-69,51,-69,51,-28,-29,-30,-5,51,51,51,-62,-31,51,51,51,51,51,51,-65,-65,-65,-65,-37,51,51,51,51,-50,-55,-52,-55,-51,]),'FLOAT_CTE':([8,32,37,40,43,44,45,46,57,61,62,63,75,81,83,84,85,88,91,92,98,99,101,102,105,108,109,110,111,119,121,123,125,126,],[-6,-69,52,-69,52,-28,-29,-30,-5,52,52,52,-62,-31,52,52,52,52,52,52,-65,-65,-65,-65,-37,52,52,52,52,-50,-55,-52,-55,-51,]),'RIGHTBRACE':([8,32,37,40,42,43,44,45,46,57,60,81,105,119,121,123,125,126,],[-6,-69,-27,-69,59,-27,-28,-29,-30,-5,-26,-31,-37,-50,-55,-52,-55,-51,]),'VOID':([11,],[18,]),'LEFTPARENTHESES':([14,23,29,48,49,61,62,63,75,83,84,85,88,91,92,98,99,101,102,108,109,110,111,],[22,-15,34,62,63,75,75,75,-62,75,75,75,75,75,75,-65,-65,-65,-65,75,75,75,75,]),'RIGHTPARENTHESES':([22,34,39,50,51,52,53,55,56,64,66,67,69,71,72,73,74,76,77,78,79,80,82,86,87,93,94,95,96,97,100,103,106,107,112,114,115,116,117,118,],[28,-21,-69,-64,-60,-61,65,-69,-24,-59,-10,-23,-57,-36,-66,-67,-56,89,90,-38,-39,-69,-32,-42,-46,-22,-33,-34,-35,-43,-47,112,-40,-41,-63,-44,-45,-48,-49,-58,]),'COMMA':([27,30,34,39,41,50,51,52,55,58,64,66,69,71,72,73,74,78,79,80,82,86,87,94,95,96,97,100,112,114,115,116,117,118,],[-10,36,-21,55,-10,-64,-60,-61,55,36,-59,-10,-57,-36,-66,-67,-56,91,92,55,-32,-42,-46,-33,-34,-35,-43,-47,-63,-44,-45,-48,-49,-58,]),'LEFTBRACE':([28,33,65,89,104,120,122,],[32,32,-20,-53,32,-54,32,]),'EQUALS':([47,50,51,52,64,],[61,-64,-60,-61,-59,]),'DIVIDE':([50,51,52,64,69,73,74,87,112,118,],[-64,-60,-61,-59,-57,-67,-56,101,-63,-58,]),'MULTIPLY':([50,51,52,64,69,73,74,87,112,118,],[-64,-60,-61,-59,-57,-67,-56,102,-63,-58,]),'PLUS':([50,51,52,64,69,72,73,74,86,87,100,112,116,117,118,],[-64,-60,-61,-59,-57,-66,-67,-56,98,-46,-47,-63,-48,-49,-58,]),'MINUS':([50,51,52,64,69,72,73,74,86,87,100,112,116,117,118,],[-64,-60,-61,-59,-57,-66,-67,-56,99,-46,-47,-63,-48,-49,-58,]),'GREATERTHAN':([50,51,52,64,69,71,72,73,74,86,87,97,100,112,114,115,116,117,118,],[-64,-60,-61,-59,-57,83,-66,-67,-56,-42,-46,-43,-47,-63,-44,-45,-48,-49,-58,]),'LESSTHAN':([50,51,52,64,69,71,72,73,74,86,87,97,100,112,114,115,116,117,118,],[-64,-60,-61,-59,-57,84,-66,-67,-56,-42,-46,-43,-47,-63,-44,-45,-48,-49,-58,]),'NOTEQUALS':([50,51,52,64,69,71,72,73,74,86,87,97,100,112,114,115,116,117,118,],[-64,-60,-61,-59,-57,85,-66,-67,-56,-42,-46,-43,-47,-63,-44,-45,-48,-49,-58,]),'ELSE':([59,113,],[-25,120,]),'STRING_CTE':([63,91,92,],[79,79,79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'seen_program':([3,],[4,]),'vars':([5,32,40,],[6,37,57,]),'empty':([5,32,39,40,55,80,],[8,8,56,8,56,56,]),'modulesaux':([6,10,],[9,15,]),'function':([6,10,],[10,10,]),'seen_vars':([7,],[12,]),'functionmain':([9,],[13,]),'returnfunctionaux':([11,],[16,]),'tipo':([11,12,39,55,80,],[17,21,54,54,54,]),'seen_void':([18,],[24,]),'seen_tipo':([19,20,],[25,26,]),'seen_id_function':([23,],[29,]),'seen_ID_var':([27,41,66,],[30,58,80,]),'bloque':([28,33,104,122,],[31,38,113,124,]),'params':([29,],[33,]),'varsaux':([30,58,],[35,68,]),'seen_params_init':([34,],[39,]),'bloqueaux':([37,43,],[42,60,]),'estatuto':([37,43,],[43,43,]),'asignacion':([37,43,],[44,44,]),'condicion':([37,43,],[45,45,]),'escritura':([37,43,],[46,46,]),'varcte':([37,43,61,62,63,83,84,85,88,91,92,108,109,110,111,],[47,47,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'paramsaux':([39,55,80,],[53,67,93,]),'seen_ID':([50,],[64,]),'expresion':([61,62,63,88,91,92,],[70,76,78,103,78,78,]),'exp':([61,62,63,83,84,85,88,91,92,108,109,],[71,71,71,94,95,96,71,71,71,114,115,]),'termino':([61,62,63,83,84,85,88,91,92,108,109,110,111,],[72,72,72,72,72,72,72,72,72,72,72,116,117,]),'factor':([61,62,63,83,84,85,88,91,92,108,109,110,111,],[73,73,73,73,73,73,73,73,73,73,73,73,73,]),'factoraux':([61,62,63,83,84,85,88,91,92,108,109,110,111,],[74,74,74,74,74,74,74,74,74,74,74,74,74,]),'escrituraaux':([63,91,92,],[77,106,107,]),'expresionaux':([71,],[82,]),'seen_termino':([72,],[86,]),'seen_factor':([73,],[87,]),'seen_insert_fondo':([75,],[88,]),'expaux':([86,],[97,]),'terminoaux':([87,],[100,]),'seen_right_parentheses_condicion':([89,],[104,]),'seen_operador':([98,99,101,102,],[108,109,110,111,]),'seen_remove_fondo':([112,],[118,]),'condicionaux':([113,],[119,]),'seen_else':([120,],[122,]),'seen_end_condicion':([121,125,],[123,126,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> PROGRAMA ID seen_program SEMICOLON vars modulesaux functionmain','calc',7,'p_calc','main.py',234),
  ('modulesaux -> function modulesaux','modulesaux',2,'p_modulesaux','main.py',240),
  ('modulesaux -> <empty>','modulesaux',0,'p_modulesaux','main.py',241),
  ('seen_program -> <empty>','seen_program',0,'p_seen_program','main.py',247),
  ('vars -> VAR seen_vars tipo ID seen_ID_var varsaux SEMICOLON vars','vars',8,'p_vars','main.py',255),
  ('vars -> empty','vars',1,'p_vars','main.py',256),
  ('seen_vars -> <empty>','seen_vars',0,'p_seen_vars','main.py',262),
  ('varsaux -> COMMA ID seen_ID_var varsaux','varsaux',4,'p_varsaux','main.py',270),
  ('varsaux -> <empty>','varsaux',0,'p_varsaux','main.py',271),
  ('seen_ID_var -> <empty>','seen_ID_var',0,'p_seen_ID_var','main.py',276),
  ('tipo -> INT seen_tipo','tipo',2,'p_tipo','main.py',289),
  ('tipo -> FLOAT seen_tipo','tipo',2,'p_tipo','main.py',290),
  ('seen_tipo -> <empty>','seen_tipo',0,'p_seen_tipo','main.py',294),
  ('function -> FUNCTION returnfunctionaux ID seen_id_function params bloque','function',6,'p_function','main.py',302),
  ('seen_id_function -> <empty>','seen_id_function',0,'p_seen_id_function','main.py',308),
  ('functionmain -> MAIN LEFTPARENTHESES RIGHTPARENTHESES bloque','functionmain',4,'p_functionmain','main.py',316),
  ('returnfunctionaux -> tipo','returnfunctionaux',1,'p_returnfunctionaux','main.py',323),
  ('returnfunctionaux -> VOID seen_void','returnfunctionaux',2,'p_returnfunctionaux','main.py',324),
  ('seen_void -> <empty>','seen_void',0,'p_seen_void','main.py',330),
  ('params -> LEFTPARENTHESES seen_params_init paramsaux RIGHTPARENTHESES','params',4,'p_params','main.py',338),
  ('seen_params_init -> <empty>','seen_params_init',0,'p_seen_params_init','main.py',344),
  ('paramsaux -> tipo ID seen_ID_var paramsaux','paramsaux',4,'p_paramsaux','main.py',352),
  ('paramsaux -> COMMA paramsaux','paramsaux',2,'p_paramsaux','main.py',353),
  ('paramsaux -> empty','paramsaux',1,'p_paramsaux','main.py',354),
  ('bloque -> LEFTBRACE vars bloqueaux RIGHTBRACE','bloque',4,'p_bloque','main.py',360),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','main.py',366),
  ('bloqueaux -> <empty>','bloqueaux',0,'p_bloqueaux','main.py',367),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','main.py',374),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','main.py',375),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','main.py',376),
  ('asignacion -> varcte EQUALS expresion SEMICOLON','asignacion',4,'p_asignacion','main.py',383),
  ('expresion -> exp expresionaux','expresion',2,'p_expresion','main.py',390),
  ('expresionaux -> GREATERTHAN exp','expresionaux',2,'p_expresionaux','main.py',396),
  ('expresionaux -> LESSTHAN exp','expresionaux',2,'p_expresionaux','main.py',397),
  ('expresionaux -> NOTEQUALS exp','expresionaux',2,'p_expresionaux','main.py',398),
  ('expresionaux -> <empty>','expresionaux',0,'p_expresionaux','main.py',399),
  ('escritura -> PRINT LEFTPARENTHESES escrituraaux RIGHTPARENTHESES SEMICOLON','escritura',5,'p_escritura','main.py',405),
  ('escrituraaux -> expresion','escrituraaux',1,'p_escrituraaux','main.py',411),
  ('escrituraaux -> STRING_CTE','escrituraaux',1,'p_escrituraaux','main.py',412),
  ('escrituraaux -> expresion COMMA escrituraaux','escrituraaux',3,'p_escrituraaux','main.py',413),
  ('escrituraaux -> STRING_CTE COMMA escrituraaux','escrituraaux',3,'p_escrituraaux','main.py',414),
  ('exp -> termino seen_termino','exp',2,'p_exp','main.py',420),
  ('exp -> termino seen_termino expaux','exp',3,'p_exp','main.py',421),
  ('expaux -> PLUS seen_operador exp','expaux',3,'p_expaux','main.py',427),
  ('expaux -> MINUS seen_operador exp','expaux',3,'p_expaux','main.py',428),
  ('termino -> factor seen_factor','termino',2,'p_termino','main.py',434),
  ('termino -> factor seen_factor terminoaux','termino',3,'p_termino','main.py',435),
  ('terminoaux -> DIVIDE seen_operador termino','terminoaux',3,'p_terminoaux','main.py',441),
  ('terminoaux -> MULTIPLY seen_operador termino','terminoaux',3,'p_terminoaux','main.py',442),
  ('condicion -> IF LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_condicion bloque condicionaux','condicion',7,'p_condicion','main.py',448),
  ('condicionaux -> ELSE seen_else bloque SEMICOLON seen_end_condicion','condicionaux',5,'p_condicionaux','main.py',454),
  ('condicionaux -> SEMICOLON seen_end_condicion','condicionaux',2,'p_condicionaux','main.py',455),
  ('seen_right_parentheses_condicion -> <empty>','seen_right_parentheses_condicion',0,'p_seen_right_parentheses_condicion','main.py',460),
  ('seen_else -> <empty>','seen_else',0,'p_seen_else','main.py',474),
  ('seen_end_condicion -> <empty>','seen_end_condicion',0,'p_seen_end_condicion','main.py',483),
  ('factor -> factoraux','factor',1,'p_factor','main.py',490),
  ('factor -> varcte','factor',1,'p_factor','main.py',491),
  ('factoraux -> LEFTPARENTHESES seen_insert_fondo expresion RIGHTPARENTHESES seen_remove_fondo','factoraux',5,'p_factoraux','main.py',497),
  ('varcte -> ID seen_ID','varcte',2,'p_varcte','main.py',503),
  ('varcte -> INT_CTE','varcte',1,'p_varcte','main.py',504),
  ('varcte -> FLOAT_CTE','varcte',1,'p_varcte','main.py',505),
  ('seen_insert_fondo -> <empty>','seen_insert_fondo',0,'p_seen_insert_fondo','main.py',512),
  ('seen_remove_fondo -> <empty>','seen_remove_fondo',0,'p_seen_remove_fondo','main.py',518),
  ('seen_ID -> <empty>','seen_ID',0,'p_seen_ID','main.py',527),
  ('seen_operador -> <empty>','seen_operador',0,'p_seen_operador','main.py',542),
  ('seen_termino -> <empty>','seen_termino',0,'p_seen_termino','main.py',547),
  ('seen_factor -> <empty>','seen_factor',0,'p_seen_factor','main.py',568),
  ('arrayIntDefinition -> LEFTBRACKET INT_CTE RIGHTBRACKET','arrayIntDefinition',3,'p_arrayIntDefinition','main.py',590),
  ('empty -> <empty>','empty',0,'p_empty','main.py',604),
]
