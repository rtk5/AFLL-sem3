
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLASS EQUALS ID LPAREN RPAREN\n    object_declaration : ID EQUALS CLASS LPAREN RPAREN\n    '
    
_lr_action_items = {'ID':([0,],[2,]),'$end':([1,6,],[0,-1,]),'EQUALS':([2,],[3,]),'CLASS':([3,],[4,]),'LPAREN':([4,],[5,]),'RPAREN':([5,],[6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'object_declaration':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> object_declaration","S'",1,None,None,None),
  ('object_declaration -> ID EQUALS CLASS LPAREN RPAREN','object_declaration',5,'p_object_declaration','5_ObjectDeclaration.py',42),
]
