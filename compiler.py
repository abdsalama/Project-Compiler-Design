from Lexer import Lexer
from parser import Parser
from Symbol_Table import SymbolTable

def main():
    print("""
    
░█████╗░███████╗░█████╗░  ████████╗███████╗░█████╗░███╗░░░███╗
██╔══██╗██╔════╝██╔══██╗  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
██║░░██║█████╗░░███████║  ░░░██║░░░█████╗░░███████║██╔████╔██║
██║░░██║██╔══╝░░██╔══██║  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
╚█████╔╝██║░░░░░██║░░██║  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░╚════╝░╚═╝░░░░░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
                                                                                
                      Welcome to compiler code!
                                                                                
                        Created by: OFA Team
Choose an option:
1. Read from the file (test.txt)
2. Provide the path of the file
3. Enter the code manually""")
    
    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))
    except ValueError:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    if choice == 1:
        file_path = "test.txt"
        with open(file_path, "r") as file:
            code = file.read()
    elif choice == 2:
        file_path = input("Enter the file path: ").strip()
        try:
            with open(file_path, "r") as file:
                code = file.read()
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
            return
    elif choice == 3:
        print("Enter your code (press Enter twice to finish):")
        code_lines = []
        while True:
            line = input()
            if line == "":
                break
            code_lines.append(line)
        code = "\n".join(code_lines)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    
    lexer = Lexer()
    tokens = lexer.lexical_analysis(code)

    if tokens == "\nPlease fix the errors to continue.":
        print(tokens)
        return
    else:
        print("\nTokens:")
        print(tokens)

    
    print("\nSymbol Table:")
    symbol_table = SymbolTable(code)
    symbol_table.process()

    
    parser = Parser(tokens)
    ast = parser.parse()

    print("\nAbstract Syntax Tree (AST):")
    parser.print_ast(ast)

main()
