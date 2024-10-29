import ply.lex as lex

# List of token names
tokens = (
    'FUNCTION', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA', 'INT', 'FLOAT', 'STRING', 'ARRAY', 'IF', 'WHILE', 
    'CLASS', 'NEW', 'EQUAL', 'NUMBER', 'STRING_LITERAL'
)

# Regular expressions for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_EQUAL = r'='

# Reserved keywords
def t_FUNCTION(t):
    r'\bfunction\b'
    return t

def t_IF(t):
    r'\bif\b'
    return t

def t_WHILE(t):
    r'\bwhile\b'
    return t

def t_CLASS(t):
    r'\bclass\b'
    return t

def t_NEW(t):
    r'\bnew\b'
    return t

def t_INT(t):
    r'\bint\b'
    return t

def t_FLOAT(t):
    r'\bfloat\b'
    return t

def t_STRING(t):
    r'\bstring\b'
    return t

def t_ARRAY(t):
    r'\barray\b'
    return t

# Identifier, numbers, and strings
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
