#  a =[1,2,3]
import ply.yacc as yacc
import ply.lex as lex

# Token definitions for Lex (adjusted for Python syntax)
tokens = (
    'ID', 'EQUALS', 'NUM', 'STRING', 'C', 'LPAREN', 'RPAREN', 'COMMA', 'BOOLEAN_MISSING', 'LSQBRACKET', 'RSQBRACKET'
)

err = 0

# Token for 'c' function
def t_C(t):
    r'c'
    return t

# Token for boolean values or 'NA'
def t_BOOLEAN_MISSING(t):
    r'TRUE|FALSE|NA'
    return t

# Token for identifiers (variable names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Token for '=' assignment operator
t_EQUALS = r'='

# Token for numbers
t_NUM = r'\d+'

# Token for strings (enclosed in double quotes)
t_STRING = r'"[^"]*"'

# Tokens for parentheses and commas
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

# Tokens for square brackets (Python-style lists)
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'

# Ignoring spaces, tabs, and newlines
t_ignore = ' \t\n'

# Error handling for lexing
def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc parser rules (adjusted for Python syntax)

def p_declaration(p):
    '''
    declaration : ID EQUALS LSQBRACKET values RSQBRACKET
    '''
    print(f"Variable '{p[1]}' assigned a list: {p[4]}")

def p_values(p):
    '''
    values  : types COMMA values
            | types
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_types(p):
    '''
    types   : ID
            | C LPAREN values RPAREN
            | STRING
            | NUM
            | BOOLEAN_MISSING
            | LSQBRACKET values RSQBRACKET
    '''
    if isinstance(p[1], str):  # STRING or BOOLEAN_MISSING
        p[0] = p[1]
    elif p[1] == 'c':
        p[0] = f"Complex function with values {p[3]}"
    elif isinstance(p[1], int):  # NUM
        p[0] = p[1]
    elif p[1] == '[':  # Python-style list
        p[0] = p[2]  # A list of values inside square brackets

# Error handling for parsing
def p_error(p):
    print("Syntax error")
    global err
    err = 1

# Create the parser
parser = yacc.yacc()

# Main loop for input
while True:
    err = 0
    try:
        s = input('Enter the list declaration statement or enter 0 to leave: ')
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
