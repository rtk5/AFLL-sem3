# obj = MyClass()
import ply.lex as lex
import ply.yacc as yacc

# Define tokens for object declaration syntax
tokens = ('ID', 'CLASS', 'LPAREN', 'RPAREN', 'EQUALS')

# To indicate/flag if an error occurred
err = 0

# Detect "class" keyword (to specify class names)
def t_CLASS(t):
    r'[A-Z][a-zA-Z_0-9]*'
    return t

# Detect identifiers for object names
def t_ID(t):
    r'[a-z_][a-zA-Z_0-9]*'
    return t

# Detect parentheses, equals sign for object creation
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='

# Ignore whitespace and tabs
t_ignore = ' \t'

# Handle lexing errors when illegal characters are detected
def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc file for parsing object declaration

def p_object_declaration(p):
    '''
    object_declaration : ID EQUALS CLASS LPAREN RPAREN
    '''
    print(f"Object {p[1]} of class {p[3]} declared.")

# Handle syntax errors encountered while parsing
def p_error(p):
    print("Syntax error")
    global err
    err = 1

parser = yacc.yacc()

# Loop to take input from the user
while True:
    err = 0
    try:
        s = input('Enter the object declaration statement or enter 0 to leave: ')
    except EOFError:
        break
    
    if not s: 
        print("You entered nothing, try again!")
        continue
    
    if s == '0':
        print("Exiting program")
        break

    result = parser.parse(s)

    # If no syntax errors are found, print "Valid syntax"
    if err == 0:
        print("Valid syntax")
