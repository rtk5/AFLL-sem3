# if (x>5): y=10
import ply.lex as lex
import ply.yacc as yacc

# Define tokens for Python `if` statement syntax
tokens = (
    'IF', 'ELIF', 'ELSE', 'ID', 'LPAREN', 'RPAREN', 'COLON', 'NUMBER', 'STRING',
    'EQUALS', 'GT', 'LT', 'GTE', 'LTE', 'NE', 'EQ'
)

# To indicate/flag if an error occurred
err = 0

# Detect keywords (if, elif, else)
def t_IF(t):
    r'if'
    return t

def t_ELIF(t):
    r'elif'
    return t

def t_ELSE(t):
    r'else'
    return t

# Detect identifiers (e.g., variable names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Detect symbols (parentheses, colon, operators, etc.)
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_EQUALS = r'='
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_NE = r'!='
t_EQ = r'=='

# Detect numbers (integers)
t_NUMBER = r'\d+'

# Detect strings (enclosed in double quotes)
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

# Yacc file for parsing `if`, `elif`, `else` statements

def p_if_statement(p):
    '''
    if_statement : IF LPAREN condition RPAREN COLON statement
    '''

def p_condition(p):
    '''
    condition    : expression
    '''

def p_expression(p):
    '''
    expression   : ID EQUALS NUMBER
                 | ID EQUALS STRING
                 | ID GT NUMBER
                 | ID LT NUMBER
                 | ID GTE NUMBER
                 | ID LTE NUMBER
                 | ID EQ NUMBER
                 | ID NE NUMBER
    '''

def p_statement(p):
    '''
    statement    : var_assign
                | if_statement
                | elif_statement
                | else_statement
    '''

def p_var_assign(p):
    '''
    var_assign   : ID EQUALS NUMBER
                 | ID EQUALS STRING
    '''

def p_elif_statement(p):
    '''
    elif_statement : ELIF LPAREN condition RPAREN COLON statement
    '''

def p_else_statement(p):
    '''
    else_statement : ELSE COLON statement
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
        s = input('Enter the if statement or enter 0 to leave: ')
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
