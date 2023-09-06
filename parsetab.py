
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BEGIN BREAK CLOSE_PAREN COLON COMMA COMPARE CONTINUE DIV DIVIDE DO DOT END EQUAL FUNC ID IF INT INT_DIGIT MINUS MOD MULTIPLE NOT OPEN_PAREN OR PLUS PRINT PROC PROGRAM READ REAL REAL_DIGIT RETURN SEMICOLON STR STRI STRING THEN VAR WHILEprogram : PROGRAM ID SEMICOLON declarations local_declarations body DOTdeclarations :\n                    | declarations VAR identList COLON typeidentList : ID\n                        | identList COMMA IDtype : INT\n            | REAL\n            | STRIlocal_declarations :\n                        | local_declarations local_declaration SEMICOLONlocal_declaration : subHead declarations bodysubHead : FUNC ID args RETURN type SEMICOLON\n                | PROC ID args SEMICOLON args :\n            | OPEN_PAREN paramList CLOSE_PARENparamList : identList COLON type\n                | paramList SEMICOLON identList COLON typebody : BEGIN optionalStatements ENDbodyWBC : BEGIN optionalStatementsWBC ENDoptionalStatements :\n                          | statementListoptionalStatementsWBC :\n                             | statementListWBCstatementList : statement\n                    |  statementList SEMICOLON statementstatementListWBC : statementWBC\n                        |  statementListWBC SEMICOLON statementWBCstatement : variable ASSIGN expression\n                | PRINT OPEN_PAREN string CLOSE_PAREN\n                | PRINT OPEN_PAREN ID CLOSE_PAREN\n                | READ OPEN_PAREN string CLOSE_PAREN\n                | ID OPEN_PAREN expressionListProc CLOSE_PAREN\n                | body\n                | IF expression THEN bodyWBC\n                | WHILE expression DO statement\n                statementWBC : statement\n                    | brConbrCon : BREAK\n            | CONTINUEstring : STRING STR STRINGvariable : IDexpressionListProc :\n                            | expressionList expressionList : expression\n                        | expressionList COMMA expressionexpression : simpleExpression\n                    | simpleExpression COMPARE simpleExpression\n                    | simpleExpression EQUAL simpleExpression\n                    | simpleExpression AND simpleExpression\n                    | simpleExpression OR simpleExpressionsimpleExpression : term\n                        | sign term\n                        | simpleExpression MINUS term\n                        | simpleExpression PLUS termterm : factor\n            | term MULTIPLE factor\n            | term DIV factor\n            | term MOD factor\n            | term DIVIDE factorfactor : ID\n                | ID OPEN_PAREN expressionList CLOSE_PAREN\n                | INT_DIGIT\n                | REAL_DIGIT\n                | OPEN_PAREN expression CLOSE_PAREN\n                | NOT factorsign : PLUS\n       sign : MINUS'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,16,],[0,-1,]),'ID':([2,7,10,12,13,26,27,32,34,35,36,37,42,43,44,47,50,54,71,72,73,74,75,76,77,78,79,80,82,85,94,97,113,129,],[3,15,23,29,30,46,46,60,23,46,64,46,46,-67,-66,46,46,15,46,46,46,46,46,46,46,46,46,46,46,23,46,23,15,23,]),'SEMICOLON':([3,9,19,20,25,30,33,40,41,45,46,48,49,52,55,57,58,59,61,62,81,84,87,90,91,93,95,96,98,99,100,101,102,103,104,105,106,107,109,110,111,112,118,119,120,121,122,123,124,127,128,131,132,],[4,17,34,-24,-33,-14,-18,-46,-51,-55,-60,-62,-63,-11,89,-6,-7,-8,-25,-28,-52,-65,113,-29,-30,-32,-31,-34,-47,-48,-49,-50,-53,-54,-56,-57,-58,-59,-64,-35,125,-15,129,-26,-36,-37,-38,-39,-61,-16,-19,-27,-17,]),'VAR':([4,5,11,28,56,57,58,59,89,125,],[-2,7,-2,7,-3,-6,-7,-8,-13,-12,]),'BEGIN':([4,5,6,10,11,17,28,34,56,57,58,59,70,85,89,97,125,129,],[-2,-9,10,10,-2,-10,10,10,-3,-6,-7,-8,97,10,-13,10,-12,10,]),'FUNC':([4,5,6,17,56,57,58,59,],[-2,-9,12,-10,-3,-6,-7,-8,]),'PROC':([4,5,6,17,56,57,58,59,],[-2,-9,13,-10,-3,-6,-7,-8,]),'DOT':([8,33,],[16,-18,]),'END':([10,18,19,20,25,33,40,41,45,46,48,49,61,62,81,84,90,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,117,118,119,120,121,122,123,124,128,131,],[-20,33,-21,-24,-33,-18,-46,-51,-55,-60,-62,-63,-25,-28,-52,-65,-29,-30,-32,-31,-34,-22,-47,-48,-49,-50,-53,-54,-56,-57,-58,-59,-64,-35,128,-23,-26,-36,-37,-38,-39,-61,-19,-27,]),'PRINT':([10,34,85,97,129,],[22,22,22,22,22,]),'READ':([10,34,85,97,129,],[24,24,24,24,24,]),'IF':([10,34,85,97,129,],[26,26,26,26,26,]),'WHILE':([10,34,85,97,129,],[27,27,27,27,27,]),'COLON':([14,15,60,88,126,],[31,-4,-5,114,130,]),'COMMA':([14,15,40,41,45,46,48,49,60,67,68,81,84,88,98,99,100,101,102,103,104,105,106,107,108,109,116,124,126,],[32,-4,-46,-51,-55,-60,-62,-63,-5,94,-44,-52,-65,32,-47,-48,-49,-50,-53,-54,-56,-57,-58,-59,94,-64,-45,-61,32,]),'ASSIGN':([21,23,],[35,-41,]),'OPEN_PAREN':([22,23,24,26,27,29,30,35,37,42,43,44,46,47,50,71,72,73,74,75,76,77,78,79,80,82,94,],[36,37,38,47,47,54,54,47,47,47,-67,-66,82,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'PLUS':([26,27,35,37,40,41,45,46,47,48,49,71,72,73,74,81,82,84,94,98,99,100,101,102,103,104,105,106,107,109,124,],[44,44,44,44,76,-51,-55,-60,44,-62,-63,44,44,44,44,-52,44,-65,44,76,76,76,76,-53,-54,-56,-57,-58,-59,-64,-61,]),'MINUS':([26,27,35,37,40,41,45,46,47,48,49,71,72,73,74,81,82,84,94,98,99,100,101,102,103,104,105,106,107,109,124,],[43,43,43,43,75,-51,-55,-60,43,-62,-63,43,43,43,43,-52,43,-65,43,75,75,75,75,-53,-54,-56,-57,-58,-59,-64,-61,]),'INT_DIGIT':([26,27,35,37,42,43,44,47,50,71,72,73,74,75,76,77,78,79,80,82,94,],[48,48,48,48,48,-67,-66,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'REAL_DIGIT':([26,27,35,37,42,43,44,47,50,71,72,73,74,75,76,77,78,79,80,82,94,],[49,49,49,49,49,-67,-66,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'NOT':([26,27,35,37,42,43,44,47,50,71,72,73,74,75,76,77,78,79,80,82,94,],[50,50,50,50,50,-67,-66,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'RETURN':([29,53,112,],[-14,86,-15,]),'INT':([31,86,114,130,],[57,57,57,57,]),'REAL':([31,86,114,130,],[58,58,58,58,]),'STRI':([31,86,114,130,],[59,59,59,59,]),'STRING':([36,38,92,],[65,65,115,]),'CLOSE_PAREN':([37,40,41,45,46,48,49,57,58,59,63,64,66,67,68,69,81,83,84,87,98,99,100,101,102,103,104,105,106,107,108,109,115,116,124,127,132,],[-42,-46,-51,-55,-60,-62,-63,-6,-7,-8,90,91,93,-43,-44,95,-52,109,-65,112,-47,-48,-49,-50,-53,-54,-56,-57,-58,-59,124,-64,-40,-45,-61,-16,-17,]),'THEN':([39,40,41,45,46,48,49,81,84,98,99,100,101,102,103,104,105,106,107,109,124,],[70,-46,-51,-55,-60,-62,-63,-52,-65,-47,-48,-49,-50,-53,-54,-56,-57,-58,-59,-64,-61,]),'DO':([40,41,45,46,48,49,51,81,84,98,99,100,101,102,103,104,105,106,107,109,124,],[-46,-51,-55,-60,-62,-63,85,-52,-65,-47,-48,-49,-50,-53,-54,-56,-57,-58,-59,-64,-61,]),'COMPARE':([40,41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[71,-51,-55,-60,-62,-63,-52,-65,-53,-54,-56,-57,-58,-59,-64,-61,]),'EQUAL':([40,41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[72,-51,-55,-60,-62,-63,-52,-65,-53,-54,-56,-57,-58,-59,-64,-61,]),'AND':([40,41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[73,-51,-55,-60,-62,-63,-52,-65,-53,-54,-56,-57,-58,-59,-64,-61,]),'OR':([40,41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[74,-51,-55,-60,-62,-63,-52,-65,-53,-54,-56,-57,-58,-59,-64,-61,]),'MULTIPLE':([41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[77,-55,-60,-62,-63,77,-65,77,77,-56,-57,-58,-59,-64,-61,]),'DIV':([41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[78,-55,-60,-62,-63,78,-65,78,78,-56,-57,-58,-59,-64,-61,]),'MOD':([41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[79,-55,-60,-62,-63,79,-65,79,79,-56,-57,-58,-59,-64,-61,]),'DIVIDE':([41,45,46,48,49,81,84,102,103,104,105,106,107,109,124,],[80,-55,-60,-62,-63,80,-65,80,80,-56,-57,-58,-59,-64,-61,]),'STR':([65,],[92,]),'BREAK':([97,129,],[122,122,]),'CONTINUE':([97,129,],[123,123,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([4,11,],[5,28,]),'local_declarations':([5,],[6,]),'body':([6,10,28,34,85,97,129,],[8,25,52,25,25,25,25,]),'local_declaration':([6,],[9,]),'subHead':([6,],[11,]),'identList':([7,54,113,],[14,88,126,]),'optionalStatements':([10,],[18,]),'statementList':([10,],[19,]),'statement':([10,34,85,97,129,],[20,61,110,120,120,]),'variable':([10,34,85,97,129,],[21,21,21,21,21,]),'expression':([26,27,35,37,47,82,94,],[39,51,62,68,83,68,116,]),'simpleExpression':([26,27,35,37,47,71,72,73,74,82,94,],[40,40,40,40,40,98,99,100,101,40,40,]),'term':([26,27,35,37,42,47,71,72,73,74,75,76,82,94,],[41,41,41,41,81,41,41,41,41,41,102,103,41,41,]),'sign':([26,27,35,37,47,71,72,73,74,82,94,],[42,42,42,42,42,42,42,42,42,42,42,]),'factor':([26,27,35,37,42,47,50,71,72,73,74,75,76,77,78,79,80,82,94,],[45,45,45,45,45,45,84,45,45,45,45,45,45,104,105,106,107,45,45,]),'args':([29,30,],[53,55,]),'type':([31,86,114,130,],[56,111,127,132,]),'string':([36,38,],[63,69,]),'expressionListProc':([37,],[66,]),'expressionList':([37,82,],[67,108,]),'paramList':([54,],[87,]),'bodyWBC':([70,],[96,]),'optionalStatementsWBC':([97,],[117,]),'statementListWBC':([97,],[118,]),'statementWBC':([97,129,],[119,131,]),'brCon':([97,129,],[121,121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON declarations local_declarations body DOT','program',7,'p_program','parser.py',26),
  ('declarations -> <empty>','declarations',0,'p_declarations','parser.py',31),
  ('declarations -> declarations VAR identList COLON type','declarations',5,'p_declarations','parser.py',32),
  ('identList -> ID','identList',1,'p_identList','parser.py',40),
  ('identList -> identList COMMA ID','identList',3,'p_identList','parser.py',41),
  ('type -> INT','type',1,'p_type','parser.py',49),
  ('type -> REAL','type',1,'p_type','parser.py',50),
  ('type -> STRI','type',1,'p_type','parser.py',51),
  ('local_declarations -> <empty>','local_declarations',0,'p_local_declarations','parser.py',58),
  ('local_declarations -> local_declarations local_declaration SEMICOLON','local_declarations',3,'p_local_declarations','parser.py',59),
  ('local_declaration -> subHead declarations body','local_declaration',3,'p_local_declaration','parser.py',67),
  ('subHead -> FUNC ID args RETURN type SEMICOLON','subHead',6,'p_subHead','parser.py',73),
  ('subHead -> PROC ID args SEMICOLON','subHead',4,'p_subHead','parser.py',74),
  ('args -> <empty>','args',0,'p_args','parser.py',85),
  ('args -> OPEN_PAREN paramList CLOSE_PAREN','args',3,'p_args','parser.py',86),
  ('paramList -> identList COLON type','paramList',3,'p_paramList','parser.py',95),
  ('paramList -> paramList SEMICOLON identList COLON type','paramList',5,'p_paramList','parser.py',96),
  ('body -> BEGIN optionalStatements END','body',3,'p_body','parser.py',107),
  ('bodyWBC -> BEGIN optionalStatementsWBC END','bodyWBC',3,'p_bodyWBC','parser.py',112),
  ('optionalStatements -> <empty>','optionalStatements',0,'p_optionalStatements','parser.py',117),
  ('optionalStatements -> statementList','optionalStatements',1,'p_optionalStatements','parser.py',118),
  ('optionalStatementsWBC -> <empty>','optionalStatementsWBC',0,'p_optionalStatementsWBC','parser.py',126),
  ('optionalStatementsWBC -> statementListWBC','optionalStatementsWBC',1,'p_optionalStatementsWBC','parser.py',127),
  ('statementList -> statement','statementList',1,'p_statementList','parser.py',135),
  ('statementList -> statementList SEMICOLON statement','statementList',3,'p_statementList','parser.py',136),
  ('statementListWBC -> statementWBC','statementListWBC',1,'p_statementListWBC','parser.py',144),
  ('statementListWBC -> statementListWBC SEMICOLON statementWBC','statementListWBC',3,'p_statementListWBC','parser.py',145),
  ('statement -> variable ASSIGN expression','statement',3,'p_statement','parser.py',153),
  ('statement -> PRINT OPEN_PAREN string CLOSE_PAREN','statement',4,'p_statement','parser.py',154),
  ('statement -> PRINT OPEN_PAREN ID CLOSE_PAREN','statement',4,'p_statement','parser.py',155),
  ('statement -> READ OPEN_PAREN string CLOSE_PAREN','statement',4,'p_statement','parser.py',156),
  ('statement -> ID OPEN_PAREN expressionListProc CLOSE_PAREN','statement',4,'p_statement','parser.py',157),
  ('statement -> body','statement',1,'p_statement','parser.py',158),
  ('statement -> IF expression THEN bodyWBC','statement',4,'p_statement','parser.py',159),
  ('statement -> WHILE expression DO statement','statement',4,'p_statement','parser.py',160),
  ('statementWBC -> statement','statementWBC',1,'p_statementWBC','parser.py',180),
  ('statementWBC -> brCon','statementWBC',1,'p_statementWBC','parser.py',181),
  ('brCon -> BREAK','brCon',1,'p_brCon','parser.py',186),
  ('brCon -> CONTINUE','brCon',1,'p_brCon','parser.py',187),
  ('string -> STRING STR STRING','string',3,'p_string','parser.py',192),
  ('variable -> ID','variable',1,'p_variable','parser.py',197),
  ('expressionListProc -> <empty>','expressionListProc',0,'p_procedureStatement','parser.py',202),
  ('expressionListProc -> expressionList','expressionListProc',1,'p_procedureStatement','parser.py',203),
  ('expressionList -> expression','expressionList',1,'p_expressionList','parser.py',212),
  ('expressionList -> expressionList COMMA expression','expressionList',3,'p_expressionList','parser.py',213),
  ('expression -> simpleExpression','expression',1,'p_expression','parser.py',221),
  ('expression -> simpleExpression COMPARE simpleExpression','expression',3,'p_expression','parser.py',222),
  ('expression -> simpleExpression EQUAL simpleExpression','expression',3,'p_expression','parser.py',223),
  ('expression -> simpleExpression AND simpleExpression','expression',3,'p_expression','parser.py',224),
  ('expression -> simpleExpression OR simpleExpression','expression',3,'p_expression','parser.py',225),
  ('simpleExpression -> term','simpleExpression',1,'p_simpleExpression','parser.py',233),
  ('simpleExpression -> sign term','simpleExpression',2,'p_simpleExpression','parser.py',234),
  ('simpleExpression -> simpleExpression MINUS term','simpleExpression',3,'p_simpleExpression','parser.py',235),
  ('simpleExpression -> simpleExpression PLUS term','simpleExpression',3,'p_simpleExpression','parser.py',236),
  ('term -> factor','term',1,'p_term','parser.py',249),
  ('term -> term MULTIPLE factor','term',3,'p_term','parser.py',250),
  ('term -> term DIV factor','term',3,'p_term','parser.py',251),
  ('term -> term MOD factor','term',3,'p_term','parser.py',252),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',253),
  ('factor -> ID','factor',1,'p_factor','parser.py',261),
  ('factor -> ID OPEN_PAREN expressionList CLOSE_PAREN','factor',4,'p_factor','parser.py',262),
  ('factor -> INT_DIGIT','factor',1,'p_factor','parser.py',263),
  ('factor -> REAL_DIGIT','factor',1,'p_factor','parser.py',264),
  ('factor -> OPEN_PAREN expression CLOSE_PAREN','factor',3,'p_factor','parser.py',265),
  ('factor -> NOT factor','factor',2,'p_factor','parser.py',266),
  ('sign -> PLUS','sign',1,'p_sign','parser.py',278),
  ('sign -> MINUS','sign',1,'p_sign','parser.py',279),
]