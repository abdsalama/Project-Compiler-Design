import re

class SymbolTable:
    
    TOKEN_SPECIFICATION = [
        ("COMMENT", r"//.*"),                    
        ("NUMBER", r"\b\d+(\.\d+)?\b"),          
        ("VAR", r"@[a-zA-Z_]\w*"),               
        ("FUNC", r"[a-zA-Z_]\w*"),            
        ("STRING", r'"[^"]*"'),                  
        ("KEYWORD", r"\b(?:if|elif|else|for|while|def|print|return)\b"),
        ("OP", r"==|!=|<=|>=|<|>|[+\-*/=]"),     
        ("COLON", r":"),  
        ("SYMBOL", r"[(){}\[\],]"),              
        ("NEWLINE", r"\n"),                      
        ("SKIP", r"[ \t]+"),                     
        ("MISMATCH", r"."),                      
    ]

    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.symbol_table = []

    def tokenize_code(self):
       
        code=self.code

       
        line_number = 1
        for match in re.finditer('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.TOKEN_SPECIFICATION), code):
            kind = match.lastgroup
            value = match.group()

            if kind == "SKIP" or kind == "COMMENT":
                continue
            elif kind == "NEWLINE":
                line_number += 1
                continue
            elif kind == "MISMATCH":
                raise SyntaxError(f"Unexpected token '{value}' at line {line_number}")
            self.tokens.append((kind, value, line_number))

    def build_table(self):
        
        variable_counter = 1
        variables = {}

        for i, (token_type, token_value, line_number) in enumerate(self.tokens):
            if token_type == "VAR":
                
                if token_value not in variables:
                    var_type = "Unknown"
                    next_token = self.tokens[i + 1] if i + 1 < len(self.tokens) else None

                    if next_token and next_token[0] == "OP" and next_token[1] == "=":
                        assigned_value = self.tokens[i + 2]
                        if assigned_value[0] == "NUMBER":
                            var_type = "Number"
                        elif assigned_value[0] == "STRING":
                            var_type = "String"
                        elif assigned_value[0] == "VAR":
                            var_type = "Unknown"  

                    
                    symbol_entry = {
                        "Counter": variable_counter,
                        "Variable Name": token_value,
                        "Object Address": hex(id(token_value)),
                        "Type": var_type,
                        "Dim": "1D",
                        "Line Declared": line_number,
                        "Line Reference": [line_number],
                    }
                    self.symbol_table.append(symbol_entry)
                    variables[token_value] = variable_counter
                    variable_counter += 1
                else:
                    
                    for entry in self.symbol_table:
                        if entry["Variable Name"] == token_value:
                            entry["Line Reference"].append(line_number)
                            break

    def print_table(self):
       
        print("Counter    Variable name   Object address  Type       Dim   Line declared   Line reference")
        print("================================================================================")
        for entry in self.symbol_table:
            print(f"{entry['Counter']: <10}{entry['Variable Name']: <16}{entry['Object Address']: <16}{entry['Type']: <10}{entry['Dim']: <6}{entry['Line Declared']: <15}{', '.join(map(str, entry['Line Reference']))}")

    def process(self):
        
        self.tokenize_code()
        self.build_table()
        self.print_table()


