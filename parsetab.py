
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNATION AT BOOLEAN BOOLEAN_CTE CALL COLON COMMA DIVIDE ELSE EQUALS FLOAT FLOAT_CTE FUNCTION GREATERTHAN ID IF INT INT_CTE LEFTBRACE LEFTBRACKET LEFTPARENTHESES LESSTHAN MAIN MINUS MULTIPLY NOTEQUAL NOTEQUALS PLUS PRINT PROGRAMA READ RETURN RIGHTBRACE RIGHTBRACKET RIGHTPARENTHESES SEMICOLON STRING_CTE THREEDOTS VAR VOID WHILE\n      calc : PROGRAMA ID seen_program SEMICOLON vars modulesaux functionmain\n     \n      modulesaux : function modulesaux\n           |\n      seen_program :  vars : VAR seen_vars tipo varsAuxDeclaration SEMICOLON vars \n                | empty\n    \n        varsAuxDeclaration : idOrArrayDeclaration seen_end_declaration COMMA varsAuxDeclaration\n                        | idOrArrayDeclaration seen_end_declaration\n    \n        seen_end_declaration : \n    \n        idOrArrayDeclaration : ID seen_ID_var\n                            | ID seen_ID_var LEFTBRACKET seen_lBracket_array arrayDimesionAux RIGHTBRACKET seen_rBracket_array\n    \n        arrayDimesionAux : INT_CTE seen_lim_inf INT_CTE seen_lim_sup\n                  |  INT_CTE seen_lim_inf INT_CTE seen_lim_sup COMMA seen_extra_dimension_array arrayDimesionAux\n    \n        seen_extra_dimension_array : \n    \n        seen_lim_inf : \n    \n        seen_lim_sup : \n    \n        seen_lBracket_array : \n    \n        seen_rBracket_array : \n    seen_vars : \n      varsaux : COMMA ID seen_ID_var varsaux\n              |\n       seen_ID_var : \n      tipo : INT seen_tipo\n           | FLOAT seen_tipo\n           | BOOLEAN seen_tipo\n\n      seen_tipo : \n      function : FUNCTION returnfunctionaux ID seen_id_function params bloque seen_function_end\n      \n        seen_id_function :\n    \n        seen_function_end :\n    \n      functionmain : MAIN seen_function_main LEFTPARENTHESES RIGHTPARENTHESES bloque seen_end_program\n      seen_end_program : seen_function_main : \n      returnfunctionaux : tipo\n                | VOID seen_void\n      \n        seen_void :\n    \n      params : LEFTPARENTHESES seen_params_init paramsaux RIGHTPARENTHESES\n      \n      seen_params_init :\n    \n      paramsaux : tipo ID seen_ID_params paramsaux\n                | COMMA paramsaux\n                | empty\n     seen_ID_params : \n      bloque : LEFTBRACE seen_start_bloqueaux vars bloqueaux returnaux RIGHTBRACE\n    \n      returnaux : RETURN expresion seen_return_function SEMICOLON\n                |\n    \n      seen_return_function :\n    \n      seen_start_bloqueaux : \n    \n      bloqueaux : estatuto bloqueaux\n              |\n      \n      estatuto : asignacion\n              | condicion\n              | escritura\n              | while\n              | functionCall\n\n      \n      asignacion : varcte ASIGNATION seen_equals expresion seen_final_asignacion SEMICOLON\n      \n      seen_equals :\n      \n      seen_final_asignacion :\n      \n      expresion : exp seen_comparacion\n                | exp seen_comparacion expresionaux exp seen_comparacion\n      \n      expresionaux : GREATERTHAN seen_operador\n                | LESSTHAN seen_operador\n                | NOTEQUALS seen_operador\n                | EQUALS seen_operador\n                |\n      \n      escritura : PRINT LEFTPARENTHESES escrituraaux RIGHTPARENTHESES SEMICOLON\n      \n      escrituraaux : escrituraaux2\n                  | escrituraaux2 COMMA escrituraaux\n      \n      escrituraaux2 : expresion seen_print_cuadruplo\n                    | STRING_CTE seen_print_cuadruplo\n      \n      seen_print_cuadruplo : \n      \n              exp : termino seen_termino\n                  | termino seen_termino expaux\n      \n              expaux : PLUS seen_operador exp\n                  | MINUS seen_operador exp\n      \n            termino : factor seen_factor\n                  | factor seen_factor terminoaux\n      \n            terminoaux : DIVIDE seen_operador termino\n                  | MULTIPLY seen_operador termino\n      \n        condicion : IF LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_condicion bloque condicionaux\n      \n        condicionaux : ELSE seen_else bloque SEMICOLON seen_end_condicion\n                  | SEMICOLON seen_end_condicion\n      \n        seen_right_parentheses_condicion :\n      \n        seen_else :\n      \n        seen_end_condicion :\n      \n        factor : factoraux\n               | varcte\n      \n        factoraux : LEFTPARENTHESES seen_insert_fondo expresion RIGHTPARENTHESES seen_remove_fondo\n      \n        varcte : ID seen_ID\n                    | INT_CTE seen_CTE_INT\n                    | FLOAT_CTE seen_CTE_FLOAT\n\n      seen_CTE_INT :seen_CTE_FLOAT :\n        seen_insert_fondo :\n      \n        seen_remove_fondo :\n      seen_ID :seen_operador :seen_termino :seen_factor :seen_comparacion :\n        while : WHILE seen_while LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_while bloque SEMICOLON seen_end_while\n    \n        seen_while : \n    \n        seen_right_parentheses_while : \n    \n        seen_end_while : \n    \n        functionCall : ID seen_fCall_id LEFTPARENTHESES seen_leftp_fCall paramsFunctionCall seen_end_paramsFCall RIGHTPARENTHESES seen_rightp_fCall SEMICOLON\n    \n        seen_fCall_id : \n    \n        seen_leftp_fCall : \n    \n        paramsFunctionCall : expresion seen_parameter_fCall COMMA seen_comma_params_fCall paramsFunctionCall \n                        | expresion seen_parameter_fCall seen_comma_params_fCall\n    \n        seen_parameter_fCall : \n    \n        seen_comma_params_fCall : \n    \n        seen_end_paramsFCall : \n    \n        seen_rightp_fCall : \n    \n      empty :\n      '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,13,43,49,94,],[0,-1,-31,-30,-42,]),'ID':([2,8,16,17,18,19,20,21,22,25,26,27,28,34,40,41,44,50,53,58,65,66,67,68,69,70,76,77,82,84,85,86,89,90,91,96,97,98,99,100,101,102,103,109,110,113,114,115,116,120,124,127,128,129,130,131,132,133,134,135,136,137,141,148,149,150,151,152,153,154,155,156,157,163,164,165,166,167,168,170,173,176,177,179,181,182,184,185,],[3,-6,24,-33,-35,-26,-26,-26,31,-34,-23,-24,-25,-112,-5,31,-46,-112,60,75,75,-49,-50,-51,-52,-53,-90,-91,102,-55,102,102,-87,-88,-89,-98,-96,-97,-84,-85,-92,-94,102,102,-105,-63,-70,-74,102,102,102,102,-95,-95,-95,-95,-71,-95,-95,-75,-95,-95,-64,-59,-60,-61,-62,102,102,102,102,-93,-54,-72,-73,-76,-77,-86,-78,-83,-109,-80,-102,102,-99,-103,-83,-79,]),'SEMICOLON':([3,4,29,30,31,35,36,47,62,76,77,79,89,90,91,94,95,96,97,98,99,100,102,112,113,114,115,117,119,132,135,139,147,156,158,162,163,164,165,166,167,171,172,178,180,],[-4,5,34,-9,-22,-8,-10,-7,-18,-90,-91,-11,-87,-88,-89,-42,-45,-98,-96,-97,-84,-85,-94,126,-57,-70,-74,-56,141,-71,-75,157,-98,-93,170,-58,-72,-73,-76,-77,-86,177,-111,182,184,]),'VAR':([5,34,44,50,],[7,7,-46,7,]),'FUNCTION':([5,6,8,10,34,40,45,51,94,],[-112,11,-6,11,-112,-5,-29,-27,-42,]),'MAIN':([5,6,8,9,10,15,34,40,45,51,94,],[-112,-3,-6,14,-3,-2,-112,-5,-29,-27,-42,]),'INT':([7,11,12,39,46,54,60,78,],[-19,19,19,-37,19,19,-41,19,]),'FLOAT':([7,11,12,39,46,54,60,78,],[-19,20,20,-37,20,20,-41,20,]),'BOOLEAN':([7,11,12,39,46,54,60,78,],[-19,21,21,-37,21,21,-41,21,]),'IF':([8,34,40,44,50,58,65,66,67,68,69,70,141,157,168,170,176,177,181,182,184,185,],[-6,-112,-5,-46,-112,72,72,-49,-50,-51,-52,-53,-64,-54,-78,-83,-80,-102,-99,-103,-83,-79,]),'PRINT':([8,34,40,44,50,58,65,66,67,68,69,70,141,157,168,170,176,177,181,182,184,185,],[-6,-112,-5,-46,-112,73,73,-49,-50,-51,-52,-53,-64,-54,-78,-83,-80,-102,-99,-103,-83,-79,]),'WHILE':([8,34,40,44,50,58,65,66,67,68,69,70,141,157,168,170,176,177,181,182,184,185,],[-6,-112,-5,-46,-112,74,74,-49,-50,-51,-52,-53,-64,-54,-78,-83,-80,-102,-99,-103,-83,-79,]),'INT_CTE':([8,34,40,42,44,48,50,57,58,63,65,66,67,68,69,70,76,77,82,84,85,86,89,90,91,96,97,98,99,100,101,102,103,109,110,111,113,114,115,116,120,124,125,127,128,129,130,131,132,133,134,135,136,137,141,148,149,150,151,152,153,154,155,156,157,163,164,165,166,167,168,170,173,176,177,179,181,182,184,185,],[-6,-112,-5,-17,-46,57,-112,-15,76,80,76,-49,-50,-51,-52,-53,-90,-91,76,-55,76,76,-87,-88,-89,-98,-96,-97,-84,-85,-92,-94,76,76,-105,-14,-63,-70,-74,76,76,76,57,76,-95,-95,-95,-95,-71,-95,-95,-75,-95,-95,-64,-59,-60,-61,-62,76,76,76,76,-93,-54,-72,-73,-76,-77,-86,-78,-83,-109,-80,-102,76,-99,-103,-83,-79,]),'FLOAT_CTE':([8,34,40,44,50,58,65,66,67,68,69,70,76,77,82,84,85,86,89,90,91,96,97,98,99,100,101,102,103,109,110,113,114,115,116,120,124,127,128,129,130,131,132,133,134,135,136,137,141,148,149,150,151,152,153,154,155,156,157,163,164,165,166,167,168,170,173,176,177,179,181,182,184,185,],[-6,-112,-5,-46,-112,77,77,-49,-50,-51,-52,-53,-90,-91,77,-55,77,77,-87,-88,-89,-98,-96,-97,-84,-85,-92,-94,77,77,-105,-63,-70,-74,77,77,77,77,-95,-95,-95,-95,-71,-95,-95,-75,-95,-95,-64,-59,-60,-61,-62,77,77,77,77,-93,-54,-72,-73,-76,-77,-86,-78,-83,-109,-80,-102,77,-99,-103,-83,-79,]),'RETURN':([8,34,40,44,50,58,64,65,66,67,68,69,70,83,141,157,168,170,176,177,181,182,184,185,],[-6,-112,-5,-46,-112,-48,82,-48,-49,-50,-51,-52,-53,-47,-64,-54,-78,-83,-80,-102,-99,-103,-83,-79,]),'RIGHTBRACE':([8,34,40,44,50,58,64,65,66,67,68,69,70,81,83,126,141,157,168,170,176,177,181,182,184,185,],[-6,-112,-5,-46,-112,-48,-44,-48,-49,-50,-51,-52,-53,94,-47,-43,-64,-54,-78,-83,-80,-102,-99,-103,-83,-79,]),'VOID':([11,],[18,]),'LEFTPARENTHESES':([14,23,24,33,72,73,74,75,76,77,82,84,85,86,87,88,89,90,91,96,97,98,99,100,101,102,103,109,110,113,114,115,116,120,124,127,128,129,130,131,132,133,134,135,136,137,148,149,150,151,152,153,154,155,156,163,164,165,166,167,173,179,],[-32,32,-28,39,85,86,-100,-104,-90,-91,101,-55,101,101,109,110,-87,-88,-89,-98,-96,-97,-84,-85,-92,-94,101,101,-105,-63,-70,-74,101,101,101,101,-95,-95,-95,-95,-71,-95,-95,-75,-95,-95,-59,-60,-61,-62,101,101,101,101,-93,-72,-73,-76,-77,-86,-109,101,]),'COMMA':([30,31,35,36,39,46,54,60,62,76,77,78,79,80,89,90,91,93,96,97,98,99,100,102,106,107,108,113,114,115,121,122,132,135,145,147,156,161,162,163,164,165,166,167,],[-9,-22,41,-10,-37,54,54,-41,-18,-90,-91,54,-11,-16,-87,-88,-89,111,-98,-96,-97,-84,-85,-94,120,-69,-69,-57,-70,-74,-67,-68,-71,-75,-108,-98,-93,173,-58,-72,-73,-76,-77,-86,]),'LEFTBRACKET':([31,36,],[-22,42,]),'RIGHTPARENTHESES':([32,39,46,52,54,55,60,61,76,77,78,89,90,91,92,96,97,98,99,100,102,104,105,106,107,108,113,114,115,121,122,123,132,135,138,142,144,145,147,156,160,161,162,163,164,165,166,167,174,183,],[37,-37,-112,59,-112,-40,-41,-39,-90,-91,-112,-87,-88,-89,-38,-98,-96,-97,-84,-85,-94,118,119,-65,-69,-69,-57,-70,-74,-67,-68,143,-71,-75,156,-66,-110,-108,-98,-93,172,-109,-58,-72,-73,-76,-77,-86,-107,-106,]),'LEFTBRACE':([37,38,59,118,140,143,159,169,175,],[44,44,-36,-81,44,-101,44,-82,44,]),'RIGHTBRACKET':([56,80,93,146,],[62,-16,-12,-13,]),'ASIGNATION':([71,75,76,77,89,90,91,],[84,-94,-90,-91,-87,-88,-89,]),'DIVIDE':([76,77,89,90,91,98,99,100,102,115,156,167,],[-90,-91,-87,-88,-89,-97,-84,-85,-94,136,-93,-86,]),'MULTIPLY':([76,77,89,90,91,98,99,100,102,115,156,167,],[-90,-91,-87,-88,-89,-97,-84,-85,-94,137,-93,-86,]),'PLUS':([76,77,89,90,91,97,98,99,100,102,114,115,135,156,165,166,167,],[-90,-91,-87,-88,-89,-96,-97,-84,-85,-94,133,-74,-75,-93,-76,-77,-86,]),'MINUS':([76,77,89,90,91,97,98,99,100,102,114,115,135,156,165,166,167,],[-90,-91,-87,-88,-89,-96,-97,-84,-85,-94,134,-74,-75,-93,-76,-77,-86,]),'GREATERTHAN':([76,77,89,90,91,96,97,98,99,100,102,113,114,115,132,135,156,163,164,165,166,167,],[-90,-91,-87,-88,-89,-98,-96,-97,-84,-85,-94,128,-70,-74,-71,-75,-93,-72,-73,-76,-77,-86,]),'LESSTHAN':([76,77,89,90,91,96,97,98,99,100,102,113,114,115,132,135,156,163,164,165,166,167,],[-90,-91,-87,-88,-89,-98,-96,-97,-84,-85,-94,129,-70,-74,-71,-75,-93,-72,-73,-76,-77,-86,]),'NOTEQUALS':([76,77,89,90,91,96,97,98,99,100,102,113,114,115,132,135,156,163,164,165,166,167,],[-90,-91,-87,-88,-89,-98,-96,-97,-84,-85,-94,130,-70,-74,-71,-75,-93,-72,-73,-76,-77,-86,]),'EQUALS':([76,77,89,90,91,96,97,98,99,100,102,113,114,115,132,135,156,163,164,165,166,167,],[-90,-91,-87,-88,-89,-98,-96,-97,-84,-85,-94,131,-70,-74,-71,-75,-93,-72,-73,-76,-77,-86,]),'STRING_CTE':([86,120,],[108,108,]),'ELSE':([94,158,],[-42,169,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'seen_program':([3,],[4,]),'vars':([5,34,50,],[6,40,58,]),'empty':([5,34,46,50,54,78,],[8,8,55,8,55,55,]),'modulesaux':([6,10,],[9,15,]),'function':([6,10,],[10,10,]),'seen_vars':([7,],[12,]),'functionmain':([9,],[13,]),'returnfunctionaux':([11,],[16,]),'tipo':([11,12,46,54,78,],[17,22,53,53,53,]),'seen_function_main':([14,],[23,]),'seen_void':([18,],[25,]),'seen_tipo':([19,20,21,],[26,27,28,]),'varsAuxDeclaration':([22,41,],[29,47,]),'idOrArrayDeclaration':([22,41,],[30,30,]),'seen_id_function':([24,],[33,]),'seen_end_declaration':([30,],[35,]),'seen_ID_var':([31,],[36,]),'params':([33,],[38,]),'bloque':([37,38,140,159,175,],[43,45,158,171,180,]),'seen_params_init':([39,],[46,]),'seen_lBracket_array':([42,],[48,]),'seen_end_program':([43,],[49,]),'seen_start_bloqueaux':([44,],[50,]),'seen_function_end':([45,],[51,]),'paramsaux':([46,54,78,],[52,61,92,]),'arrayDimesionAux':([48,125,],[56,146,]),'seen_lim_inf':([57,],[63,]),'bloqueaux':([58,65,],[64,83,]),'estatuto':([58,65,],[65,65,]),'asignacion':([58,65,],[66,66,]),'condicion':([58,65,],[67,67,]),'escritura':([58,65,],[68,68,]),'while':([58,65,],[69,69,]),'functionCall':([58,65,],[70,70,]),'varcte':([58,65,82,85,86,103,109,116,120,124,127,152,153,154,155,179,],[71,71,100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'seen_ID_params':([60,],[78,]),'seen_rBracket_array':([62,],[79,]),'returnaux':([64,],[81,]),'seen_while':([74,],[87,]),'seen_fCall_id':([75,],[88,]),'seen_ID':([75,102,],[89,89,]),'seen_CTE_INT':([76,],[90,]),'seen_CTE_FLOAT':([77,],[91,]),'seen_lim_sup':([80,],[93,]),'expresion':([82,85,86,103,109,116,120,124,179,],[95,104,107,117,123,138,107,145,145,]),'exp':([82,85,86,103,109,116,120,124,127,152,153,179,],[96,96,96,96,96,96,96,96,147,163,164,96,]),'termino':([82,85,86,103,109,116,120,124,127,152,153,154,155,179,],[97,97,97,97,97,97,97,97,97,97,97,165,166,97,]),'factor':([82,85,86,103,109,116,120,124,127,152,153,154,155,179,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'factoraux':([82,85,86,103,109,116,120,124,127,152,153,154,155,179,],[99,99,99,99,99,99,99,99,99,99,99,99,99,99,]),'seen_equals':([84,],[103,]),'escrituraaux':([86,120,],[105,142,]),'escrituraaux2':([86,120,],[106,106,]),'seen_return_function':([95,],[112,]),'seen_comparacion':([96,147,],[113,162,]),'seen_termino':([97,],[114,]),'seen_factor':([98,],[115,]),'seen_insert_fondo':([101,],[116,]),'seen_print_cuadruplo':([107,108,],[121,122,]),'seen_leftp_fCall':([110,],[124,]),'seen_extra_dimension_array':([111,],[125,]),'expresionaux':([113,],[127,]),'expaux':([114,],[132,]),'terminoaux':([115,],[135,]),'seen_final_asignacion':([117,],[139,]),'seen_right_parentheses_condicion':([118,],[140,]),'paramsFunctionCall':([124,179,],[144,183,]),'seen_operador':([128,129,130,131,133,134,136,137,],[148,149,150,151,152,153,154,155,]),'seen_right_parentheses_while':([143,],[159,]),'seen_end_paramsFCall':([144,],[160,]),'seen_parameter_fCall':([145,],[161,]),'seen_remove_fondo':([156,],[167,]),'condicionaux':([158,],[168,]),'seen_comma_params_fCall':([161,173,],[174,179,]),'seen_else':([169,],[175,]),'seen_end_condicion':([170,184,],[176,185,]),'seen_rightp_fCall':([172,],[178,]),'seen_end_while':([177,],[181,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> PROGRAMA ID seen_program SEMICOLON vars modulesaux functionmain','calc',7,'p_calc','main.py',227),
  ('modulesaux -> function modulesaux','modulesaux',2,'p_modulesaux','main.py',234),
  ('modulesaux -> <empty>','modulesaux',0,'p_modulesaux','main.py',235),
  ('seen_program -> <empty>','seen_program',0,'p_seen_program','main.py',240),
  ('vars -> VAR seen_vars tipo varsAuxDeclaration SEMICOLON vars','vars',6,'p_vars','main.py',248),
  ('vars -> empty','vars',1,'p_vars','main.py',249),
  ('varsAuxDeclaration -> idOrArrayDeclaration seen_end_declaration COMMA varsAuxDeclaration','varsAuxDeclaration',4,'p_varsAuxDeclaration','main.py',255),
  ('varsAuxDeclaration -> idOrArrayDeclaration seen_end_declaration','varsAuxDeclaration',2,'p_varsAuxDeclaration','main.py',256),
  ('seen_end_declaration -> <empty>','seen_end_declaration',0,'p_seen_end_declaration','main.py',262),
  ('idOrArrayDeclaration -> ID seen_ID_var','idOrArrayDeclaration',2,'p_idOrArrayDeclaration','main.py',269),
  ('idOrArrayDeclaration -> ID seen_ID_var LEFTBRACKET seen_lBracket_array arrayDimesionAux RIGHTBRACKET seen_rBracket_array','idOrArrayDeclaration',7,'p_idOrArrayDeclaration','main.py',270),
  ('arrayDimesionAux -> INT_CTE seen_lim_inf INT_CTE seen_lim_sup','arrayDimesionAux',4,'p_arrayDimesionAux','main.py',276),
  ('arrayDimesionAux -> INT_CTE seen_lim_inf INT_CTE seen_lim_sup COMMA seen_extra_dimension_array arrayDimesionAux','arrayDimesionAux',7,'p_arrayDimesionAux','main.py',277),
  ('seen_extra_dimension_array -> <empty>','seen_extra_dimension_array',0,'p_seen_extra_dimension_array','main.py',283),
  ('seen_lim_inf -> <empty>','seen_lim_inf',0,'p_seen_lim_inf','main.py',290),
  ('seen_lim_sup -> <empty>','seen_lim_sup',0,'p_seen_lim_sup','main.py',298),
  ('seen_lBracket_array -> <empty>','seen_lBracket_array',0,'p_seen_lBracket_array','main.py',307),
  ('seen_rBracket_array -> <empty>','seen_rBracket_array',0,'p_seen_rBracket_array','main.py',314),
  ('seen_vars -> <empty>','seen_vars',0,'p_seen_vars','main.py',320),
  ('varsaux -> COMMA ID seen_ID_var varsaux','varsaux',4,'p_varsaux','main.py',331),
  ('varsaux -> <empty>','varsaux',0,'p_varsaux','main.py',332),
  ('seen_ID_var -> <empty>','seen_ID_var',0,'p_seen_ID_var','main.py',337),
  ('tipo -> INT seen_tipo','tipo',2,'p_tipo','main.py',345),
  ('tipo -> FLOAT seen_tipo','tipo',2,'p_tipo','main.py',346),
  ('tipo -> BOOLEAN seen_tipo','tipo',2,'p_tipo','main.py',347),
  ('seen_tipo -> <empty>','seen_tipo',0,'p_seen_tipo','main.py',353),
  ('function -> FUNCTION returnfunctionaux ID seen_id_function params bloque seen_function_end','function',7,'p_function','main.py',361),
  ('seen_id_function -> <empty>','seen_id_function',0,'p_seen_id_function','main.py',367),
  ('seen_function_end -> <empty>','seen_function_end',0,'p_seen_function_end','main.py',376),
  ('functionmain -> MAIN seen_function_main LEFTPARENTHESES RIGHTPARENTHESES bloque seen_end_program','functionmain',6,'p_functionmain','main.py',383),
  ('seen_end_program -> <empty>','seen_end_program',0,'p_seen_end_program','main.py',388),
  ('seen_function_main -> <empty>','seen_function_main',0,'p_seen_function_main','main.py',393),
  ('returnfunctionaux -> tipo','returnfunctionaux',1,'p_returnfunctionaux','main.py',402),
  ('returnfunctionaux -> VOID seen_void','returnfunctionaux',2,'p_returnfunctionaux','main.py',403),
  ('seen_void -> <empty>','seen_void',0,'p_seen_void','main.py',409),
  ('params -> LEFTPARENTHESES seen_params_init paramsaux RIGHTPARENTHESES','params',4,'p_params','main.py',416),
  ('seen_params_init -> <empty>','seen_params_init',0,'p_seen_params_init','main.py',422),
  ('paramsaux -> tipo ID seen_ID_params paramsaux','paramsaux',4,'p_paramsaux','main.py',429),
  ('paramsaux -> COMMA paramsaux','paramsaux',2,'p_paramsaux','main.py',430),
  ('paramsaux -> empty','paramsaux',1,'p_paramsaux','main.py',431),
  ('seen_ID_params -> <empty>','seen_ID_params',0,'p_seen_ID_params','main.py',436),
  ('bloque -> LEFTBRACE seen_start_bloqueaux vars bloqueaux returnaux RIGHTBRACE','bloque',6,'p_bloque','main.py',457),
  ('returnaux -> RETURN expresion seen_return_function SEMICOLON','returnaux',4,'p_returnaux','main.py',463),
  ('returnaux -> <empty>','returnaux',0,'p_returnaux','main.py',464),
  ('seen_return_function -> <empty>','seen_return_function',0,'p_seen_return_function','main.py',470),
  ('seen_start_bloqueaux -> <empty>','seen_start_bloqueaux',0,'p_seen_start_bloqueaux','main.py',477),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','main.py',484),
  ('bloqueaux -> <empty>','bloqueaux',0,'p_bloqueaux','main.py',485),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','main.py',491),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','main.py',492),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','main.py',493),
  ('estatuto -> while','estatuto',1,'p_estatuto','main.py',494),
  ('estatuto -> functionCall','estatuto',1,'p_estatuto','main.py',495),
  ('asignacion -> varcte ASIGNATION seen_equals expresion seen_final_asignacion SEMICOLON','asignacion',6,'p_asignacion','main.py',502),
  ('seen_equals -> <empty>','seen_equals',0,'p_seen_equals','main.py',508),
  ('seen_final_asignacion -> <empty>','seen_final_asignacion',0,'p_seen_final_asignacion','main.py',516),
  ('expresion -> exp seen_comparacion','expresion',2,'p_expresion','main.py',523),
  ('expresion -> exp seen_comparacion expresionaux exp seen_comparacion','expresion',5,'p_expresion','main.py',524),
  ('expresionaux -> GREATERTHAN seen_operador','expresionaux',2,'p_expresionaux','main.py',530),
  ('expresionaux -> LESSTHAN seen_operador','expresionaux',2,'p_expresionaux','main.py',531),
  ('expresionaux -> NOTEQUALS seen_operador','expresionaux',2,'p_expresionaux','main.py',532),
  ('expresionaux -> EQUALS seen_operador','expresionaux',2,'p_expresionaux','main.py',533),
  ('expresionaux -> <empty>','expresionaux',0,'p_expresionaux','main.py',534),
  ('escritura -> PRINT LEFTPARENTHESES escrituraaux RIGHTPARENTHESES SEMICOLON','escritura',5,'p_escritura','main.py',540),
  ('escrituraaux -> escrituraaux2','escrituraaux',1,'p_escrituraaux','main.py',546),
  ('escrituraaux -> escrituraaux2 COMMA escrituraaux','escrituraaux',3,'p_escrituraaux','main.py',547),
  ('escrituraaux2 -> expresion seen_print_cuadruplo','escrituraaux2',2,'p_escrituraaux2','main.py',553),
  ('escrituraaux2 -> STRING_CTE seen_print_cuadruplo','escrituraaux2',2,'p_escrituraaux2','main.py',554),
  ('seen_print_cuadruplo -> <empty>','seen_print_cuadruplo',0,'p_seen_print_cuadruplo','main.py',560),
  ('exp -> termino seen_termino','exp',2,'p_exp','main.py',567),
  ('exp -> termino seen_termino expaux','exp',3,'p_exp','main.py',568),
  ('expaux -> PLUS seen_operador exp','expaux',3,'p_expaux','main.py',574),
  ('expaux -> MINUS seen_operador exp','expaux',3,'p_expaux','main.py',575),
  ('termino -> factor seen_factor','termino',2,'p_termino','main.py',581),
  ('termino -> factor seen_factor terminoaux','termino',3,'p_termino','main.py',582),
  ('terminoaux -> DIVIDE seen_operador termino','terminoaux',3,'p_terminoaux','main.py',588),
  ('terminoaux -> MULTIPLY seen_operador termino','terminoaux',3,'p_terminoaux','main.py',589),
  ('condicion -> IF LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_condicion bloque condicionaux','condicion',7,'p_condicion','main.py',595),
  ('condicionaux -> ELSE seen_else bloque SEMICOLON seen_end_condicion','condicionaux',5,'p_condicionaux','main.py',601),
  ('condicionaux -> SEMICOLON seen_end_condicion','condicionaux',2,'p_condicionaux','main.py',602),
  ('seen_right_parentheses_condicion -> <empty>','seen_right_parentheses_condicion',0,'p_seen_right_parentheses_condicion','main.py',608),
  ('seen_else -> <empty>','seen_else',0,'p_seen_else','main.py',615),
  ('seen_end_condicion -> <empty>','seen_end_condicion',0,'p_seen_end_condicion','main.py',622),
  ('factor -> factoraux','factor',1,'p_factor','main.py',629),
  ('factor -> varcte','factor',1,'p_factor','main.py',630),
  ('factoraux -> LEFTPARENTHESES seen_insert_fondo expresion RIGHTPARENTHESES seen_remove_fondo','factoraux',5,'p_factoraux','main.py',636),
  ('varcte -> ID seen_ID','varcte',2,'p_varcte','main.py',642),
  ('varcte -> INT_CTE seen_CTE_INT','varcte',2,'p_varcte','main.py',643),
  ('varcte -> FLOAT_CTE seen_CTE_FLOAT','varcte',2,'p_varcte','main.py',644),
  ('seen_CTE_INT -> <empty>','seen_CTE_INT',0,'p_seen_CTE_INT','main.py',650),
  ('seen_CTE_FLOAT -> <empty>','seen_CTE_FLOAT',0,'p_seen_CTE_FLOAT','main.py',656),
  ('seen_insert_fondo -> <empty>','seen_insert_fondo',0,'p_seen_insert_fondo','main.py',663),
  ('seen_remove_fondo -> <empty>','seen_remove_fondo',0,'p_seen_remove_fondo','main.py',670),
  ('seen_ID -> <empty>','seen_ID',0,'p_seen_ID','main.py',675),
  ('seen_operador -> <empty>','seen_operador',0,'p_seen_operador','main.py',681),
  ('seen_termino -> <empty>','seen_termino',0,'p_seen_termino','main.py',687),
  ('seen_factor -> <empty>','seen_factor',0,'p_seen_factor','main.py',692),
  ('seen_comparacion -> <empty>','seen_comparacion',0,'p_seen_comparacion','main.py',697),
  ('while -> WHILE seen_while LEFTPARENTHESES expresion RIGHTPARENTHESES seen_right_parentheses_while bloque SEMICOLON seen_end_while','while',9,'p_while','main.py',703),
  ('seen_while -> <empty>','seen_while',0,'p_seen_while','main.py',709),
  ('seen_right_parentheses_while -> <empty>','seen_right_parentheses_while',0,'p_seen_right_parentheses_while','main.py',716),
  ('seen_end_while -> <empty>','seen_end_while',0,'p_seen_end_while','main.py',723),
  ('functionCall -> ID seen_fCall_id LEFTPARENTHESES seen_leftp_fCall paramsFunctionCall seen_end_paramsFCall RIGHTPARENTHESES seen_rightp_fCall SEMICOLON','functionCall',9,'p_functionCall','main.py',730),
  ('seen_fCall_id -> <empty>','seen_fCall_id',0,'p_seen_fCall_id','main.py',737),
  ('seen_leftp_fCall -> <empty>','seen_leftp_fCall',0,'p_seen_leftp_fCall','main.py',747),
  ('paramsFunctionCall -> expresion seen_parameter_fCall COMMA seen_comma_params_fCall paramsFunctionCall','paramsFunctionCall',5,'p_paramsFunctionCall','main.py',755),
  ('paramsFunctionCall -> expresion seen_parameter_fCall seen_comma_params_fCall','paramsFunctionCall',3,'p_paramsFunctionCall','main.py',756),
  ('seen_parameter_fCall -> <empty>','seen_parameter_fCall',0,'p_seen_parameter_fCall','main.py',762),
  ('seen_comma_params_fCall -> <empty>','seen_comma_params_fCall',0,'p_seen_comma_params_fCall','main.py',769),
  ('seen_end_paramsFCall -> <empty>','seen_end_paramsFCall',0,'p_seen_end_paramsFCall','main.py',776),
  ('seen_rightp_fCall -> <empty>','seen_rightp_fCall',0,'p_seen_rightp_fCall','main.py',783),
  ('empty -> <empty>','empty',0,'p_empty','main.py',798),
]
