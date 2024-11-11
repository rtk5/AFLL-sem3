# def my_function(): x=5
import ply.lex as lex
import ply.yacc as yacc

# Define tokens for Python function declaration syntax
tokens = ('DEF', 'ID', 'LPAREN', 'RPAREN', 'COLON', 'COMMA', 'NUMBER', 'STRING', 'EQUALS')

# To indicate/flag if an error occurred
err = 0

# Detect "def" keyword for function declaration
def t_DEF(t):
    r'def'
    return t

# Detect identifier names (e.g., variable and function names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Detect parentheses, colon, comma, and assignment symbol
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_EQUALS = r'='
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'

# Ignore whitespace and tabs
t_ignore = ' \t'

# Handle lexing errors when illegal characters are detected
def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc file

def p_function_declaration(p):
    '''
    function_declaration : DEF ID LPAREN params RPAREN COLON statements
    '''

def p_params(p):
    '''
    params  : empty 
            | paramlist
    '''

def p_paramlist(p):
    '''
    paramlist    : ID
                 | ID COMMA paramlist
    '''

def p_statements(p):
    '''
    statements   : statement
                 | statement statements
    '''

def p_statement(p):
    '''
    statement    : var_assign
    '''

def p_var_assign(p):
    '''
    var_assign   : ID EQUALS STRING
                 | ID EQUALS NUMBER
    '''

# Non-terminal for empty or lambda production
def p_empty(p):
    '''
    empty :
    '''

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
        s = input('Enter the function declaration statement or enter 0 to leave: ')
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
