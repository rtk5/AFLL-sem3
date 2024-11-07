import ply.yacc as yacc
from lexer import tokens

# Grammar rules
def p_program(p):
    '''program : statement
               | program statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# Statements
def p_statement(p):
    '''statement : function_declaration
                 | function_definition
                 | datatype_declaration
                 | array_declaration
                 | selection_statement
                 | loop_construct
                 | class_definition
                 | object_creation'''

# Function declaration
def p_function_declaration(p):
    'function_declaration : FUNCTION IDENTIFIER LPAREN RPAREN SEMICOLON'

# Function definition
def p_function_definition(p):
    'function_definition : FUNCTION IDENTIFIER LPAREN RPAREN LBRACE RBRACE'

# Simple data-type declaration
def p_datatype_declaration(p):
    '''datatype_declaration : INT IDENTIFIER SEMICOLON
                            | FLOAT IDENTIFIER SEMICOLON
                            | STRING IDENTIFIER SEMICOLON'''

# Array declaration
def p_array_declaration(p):
    'array_declaration : ARRAY IDENTIFIER EQUAL LBRACE RBRACE SEMICOLON'

# Selection statement (if)
def p_selection_statement(p):
    'selection_statement : IF LPAREN IDENTIFIER RPAREN LBRACE RBRACE'

# Looping construct (while)
def p_loop_construct(p):
    'loop_construct : WHILE LPAREN IDENTIFIER RPAREN LBRACE RBRACE'

# Class definition
def p_class_definition(p):
    'class_definition : CLASS IDENTIFIER LBRACE RBRACE'

# Object creation (similar to Java syntax)
def p_object_creation(p):
    'object_creation : IDENTIFIER IDENTIFIER EQUAL NEW IDENTIFIER LPAREN RPAREN SEMICOLON'

# Empty rule to allow optional parts
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno}, position {p.lexpos})")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
