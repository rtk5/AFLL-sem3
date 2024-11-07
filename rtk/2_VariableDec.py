# x = "hello"
import ply.yacc as yacc
import ply.lex as lex

# Python Variable Declaration Syntax:
# varname = value
# value -> varname | number | string | boolean

# Lex File:
tokens = ('ID', 'EQUALS', 'NUMBER', 'STRING', 'TRUE', 'FALSE', 'NONE')

err = 0

# Define the token rules
t_EQUALS = r'='
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'
t_TRUE = r'True'
t_FALSE = r'False'
t_NONE = r'None'

# Identifier naming rules for Python variables:
# Consists of letters, digits, and underscores.
# Must not start with a digit.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Handle whitespace and newlines
t_ignore = ' \t\n'

# To handle lexing errors when illegal characters are detected
def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc File:

# Grammar production rules for variable declaration
def p_declaration(p):
    '''
    declaration : ID EQUALS value
    '''

def p_value(p):
    '''
    value   : STRING
            | NUMBER
            | bool_value
            | NONE
            | ID
    '''

# Define the boolean values TRUE, FALSE, and NONE
def p_bool_value(p):
    '''
    bool_value : TRUE
               | FALSE
    '''

# To handle syntax errors encountered while parsing
def p_error(p):
    print("Syntax error")
    global err
    err = 1

parser = yacc.yacc()

# Main loop for parsing input
while True:
    err = 0
    try:
        s = input('Enter a Python variable declaration statement or enter 0 to leave: ')
    except EOFError:
        break
    
    if not s: 
        err = 0
        print("You entered nothing, try again!")
        continue
    
    if s == '0':
        print("Exiting program")
        break

    result = parser.parse(s)

    # If there are no syntax errors, print valid syntax
    if err == 0:
        print("Valid syntax")
