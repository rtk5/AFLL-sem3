
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARRAY CLASS COMMA EQUAL FLOAT FUNCTION IDENTIFIER IF INT LBRACE LPAREN NEW NUMBER RBRACE RPAREN SEMICOLON STRING STRING_LITERAL WHILEprogram : statement\n               | program statementstatement : function_declaration\n                 | function_definition\n                 | datatype_declaration\n                 | array_declaration\n                 | selection_statement\n                 | loop_construct\n                 | class_definition\n                 | object_creationfunction_declaration : FUNCTION IDENTIFIER LPAREN RPAREN SEMICOLONfunction_definition : FUNCTION IDENTIFIER LPAREN RPAREN LBRACE RBRACEdatatype_declaration : INT IDENTIFIER SEMICOLON\n                            | FLOAT IDENTIFIER SEMICOLON\n                            | STRING IDENTIFIER SEMICOLONarray_declaration : ARRAY IDENTIFIER EQUAL LBRACE RBRACE SEMICOLONselection_statement : IF LPAREN IDENTIFIER RPAREN LBRACE RBRACEloop_construct : WHILE LPAREN IDENTIFIER RPAREN LBRACE RBRACEclass_definition : CLASS IDENTIFIER LBRACE RBRACEobject_creation : IDENTIFIER IDENTIFIER EQUAL NEW IDENTIFIER LPAREN RPAREN SEMICOLONempty :'
    
_lr_action_items = {'FUNCTION':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[11,11,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'INT':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[13,13,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'FLOAT':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[14,14,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[15,15,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'ARRAY':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[16,16,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[17,17,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[18,18,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'CLASS':([0,1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[19,19,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'IDENTIFIER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20,27,28,32,33,34,40,44,45,51,53,54,55,57,],[12,12,-1,-3,-4,-5,-6,-7,-8,-9,-10,21,22,23,24,25,26,29,-2,36,37,-13,-14,-15,47,-19,-11,-12,-16,-17,-18,-20,]),'$end':([1,2,3,4,5,6,7,8,9,10,20,32,33,34,44,45,51,53,54,55,57,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-14,-15,-19,-11,-12,-16,-17,-18,-20,]),'LPAREN':([17,18,21,47,],[27,28,30,52,]),'EQUAL':([22,26,],[31,35,]),'SEMICOLON':([23,24,25,39,48,56,],[32,33,34,45,53,57,]),'LBRACE':([29,35,39,42,43,],[38,41,46,49,50,]),'RPAREN':([30,36,37,52,],[39,42,43,56,]),'NEW':([31,],[40,]),'RBRACE':([38,41,46,49,50,],[44,48,51,54,55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,20,]),'function_declaration':([0,1,],[3,3,]),'function_definition':([0,1,],[4,4,]),'datatype_declaration':([0,1,],[5,5,]),'array_declaration':([0,1,],[6,6,]),'selection_statement':([0,1,],[7,7,]),'loop_construct':([0,1,],[8,8,]),'class_definition':([0,1,],[9,9,]),'object_creation':([0,1,],[10,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','parser.py',6),
  ('program -> program statement','program',2,'p_program','parser.py',7),
  ('statement -> function_declaration','statement',1,'p_statement','parser.py',15),
  ('statement -> function_definition','statement',1,'p_statement','parser.py',16),
  ('statement -> datatype_declaration','statement',1,'p_statement','parser.py',17),
  ('statement -> array_declaration','statement',1,'p_statement','parser.py',18),
  ('statement -> selection_statement','statement',1,'p_statement','parser.py',19),
  ('statement -> loop_construct','statement',1,'p_statement','parser.py',20),
  ('statement -> class_definition','statement',1,'p_statement','parser.py',21),
  ('statement -> object_creation','statement',1,'p_statement','parser.py',22),
  ('function_declaration -> FUNCTION IDENTIFIER LPAREN RPAREN SEMICOLON','function_declaration',5,'p_function_declaration','parser.py',26),
  ('function_definition -> FUNCTION IDENTIFIER LPAREN RPAREN LBRACE RBRACE','function_definition',6,'p_function_definition','parser.py',30),
  ('datatype_declaration -> INT IDENTIFIER SEMICOLON','datatype_declaration',3,'p_datatype_declaration','parser.py',34),
  ('datatype_declaration -> FLOAT IDENTIFIER SEMICOLON','datatype_declaration',3,'p_datatype_declaration','parser.py',35),
  ('datatype_declaration -> STRING IDENTIFIER SEMICOLON','datatype_declaration',3,'p_datatype_declaration','parser.py',36),
  ('array_declaration -> ARRAY IDENTIFIER EQUAL LBRACE RBRACE SEMICOLON','array_declaration',6,'p_array_declaration','parser.py',40),
  ('selection_statement -> IF LPAREN IDENTIFIER RPAREN LBRACE RBRACE','selection_statement',6,'p_selection_statement','parser.py',44),
  ('loop_construct -> WHILE LPAREN IDENTIFIER RPAREN LBRACE RBRACE','loop_construct',6,'p_loop_construct','parser.py',48),
  ('class_definition -> CLASS IDENTIFIER LBRACE RBRACE','class_definition',4,'p_class_definition','parser.py',52),
  ('object_creation -> IDENTIFIER IDENTIFIER EQUAL NEW IDENTIFIER LPAREN RPAREN SEMICOLON','object_creation',8,'p_object_creation','parser.py',56),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',60),
]
