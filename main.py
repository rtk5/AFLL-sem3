from lexer import lexer
from parser import parser

def main():
    data = '''
    function myFunction();
    function myFunction() { }
    int x;
    array myArray = {};
    if (x) { }
    while (x) { }
    class MyClass { }
    MyClass obj = new MyClass();
    '''

    # Lexical analysis
    print("Lexical Analysis:")
    lexer.input(data)
    for token in lexer:
        print(token)

    # Parsing
    print("\nParsing:")
    result = parser.parse(data)
    if result:
        print("Parsing completed successfully.")
    else:
        print("Parsing failed.")

if __name__ == '__main__':
    main()
