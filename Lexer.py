import re

TOKEN_SPECIFICATION = [
    ("KEYWORD_IF_STATEMENT", r"\bif\b"),
    ("KEYWORD_ELIF_STATEMENT", r"\belif\b"),
    ("KEYWORD_ELSE_STATEMENT", r"\belse\b"),
    ("KEYWORD_FOR_LOOP", r"\bfor\b"),
    ("KEYWORD_WHILE_LOOP", r"\bwhile\b"),
    ("KEYWORD_DEF_FUNCTION", r"\bdef\b"),
    ("KEYWORD_PRINT_FUNCTION", r"\bprint\b"),
    ("KEYWORD_RETURN_STATEMENT", r"\breturn\b"),

    ("COMMENT", r"//.*"),  # Comments
    ("NUMBER", r"\b\d+(\.\d+)?\b"),  # Integers and decimals
    ("VAR", r"@[a-zA-Z_]\w*"),  # Variables starting with @
    ("FUNC", r"[a-zA-Z_]\w*"),  # Function or variable names
    ("STRING", r'"[^"]*"'),  # Strings enclosed in double quotes
    ("OP", r"==|!=|<=|>=|<|>|[+\-*/=]"),  # Operators
    ("SYMBOL", r"[(){}\[\],]"),  # Symbols
    ("NEWLINE", r"\n"),  # Newlines
    ("SKIP", r"[ \t]+"),  # Whitespace
    ("MISMATCH", r"."),  # Any unexpected character
]


TOKEN_DESCRIPTIONS = {
    "COMMENT": "comment",
    "NUMBER": "number",
    "VAR": "variable",
    "FUNC": "function",
    "STRING": "string",
    "KEYWORD_IF_STATEMENT": "if statement",
    "KEYWORD_ELIF_STATEMENT": "else if statement",
    "KEYWORD_ELSE_STATEMENT": "else statement",
    "KEYWORD_FOR_LOOP": "for loop",
    "KEYWORD_WHILE_LOOP": "while loop",
    "KEYWORD_DEF_FUNCTION": "function definition",
    "KEYWORD_PRINT_FUNCTION": "output function",
    "KEYWORD_RETURN_STATEMENT": "return statement",
    "OP": "operator",
    "SYMBOL": "symbol",
    "NEWLINE": "new line",
    "SKIP": "whitespace",
    "MISMATCH": "unexpected token",
}

class Lexer:
    def __init__(self):
        self.token_regex = self.token_regex()

    def token_regex(self):
        
        token_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in TOKEN_SPECIFICATION)
        return re.compile(token_regex)

    def tokenize(self, code):
        
        line_num = 1
        tokens = []
        errors = []

        for match in self.token_regex.finditer(code):
            kind = match.lastgroup
            value = match.group()

            if kind == "SKIP":
                continue
            elif kind == "NEWLINE":
                line_num += 1
            elif kind == "MISMATCH":
                errors.append(f"Error on line {line_num}: Unexpected character '{value}'")
            else:
                description = TOKEN_DESCRIPTIONS.get(kind, "unknown")
                tokens.append((description, value))

        return tokens, errors

    def lexical_analysis(self, code):
        tokens, errors = self.tokenize(code)
        
        if errors:
            print("Lexical Analysis: Errors Found\n")
            for error in errors:
                print(error)
            return ("\nPlease fix the errors to continue.")
        
        else:
            new_tokens=[]
            for token in tokens:
                if token[0]=="string":
                    new_tokens.append((token[0], token[1].strip('"')))
                else:    
                    new_tokens.append((token[0],token[1]))
            return new_tokens   

