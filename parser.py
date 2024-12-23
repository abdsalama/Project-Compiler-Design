class Parser:
    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.token_index = 0
        self.source_ast = {"main_scope": []}     #main scope

    def current_token(self):
        return self.token_stream[self.token_index] if self.token_index < len(self.token_stream) else ("EOF", "")

    def match(self, expected_type):
        token = self.current_token()
        if token[0] == expected_type:
            self.token_index += 1
            return token
        else:
            raise SyntaxError(f"Expected {expected_type} but found {token[0]} at index {self.token_index}")

    def parse(self):  #main function in our code
        while self.token_index < len(self.token_stream):
            token_type, token_value = self.current_token()

            if token_type == "variable" and self.peek_next() and self.peek_next()[0] == "operator":
                self.source_ast["main_scope"].append(self.parse_variable_declaration())
            elif token_type == "function definition" and token_value == "def":
                self.source_ast["main_scope"].append(self.parse_function())
            elif token_type == "for loop":
                self.source_ast["main_scope"].append(self.parse_for_loop())
            elif token_type == "while loop":
                self.source_ast["main_scope"].append(self.parse_while_loop())
            else:
                self.token_index += 1  # Skip comments and unrecognized tokens 
        return self.source_ast

    def parse_variable_declaration(self):
        variable_name = self.match("variable")[1]
        self.match("operator")  # Skip "="
        value = self.match(self.current_token()[0])[1]
        return {"VariableDeclaration": {"name": variable_name, "value": value}}

    def parse_function(self):
        self.match("function definition")  # Skip "def"
        function_name = self.match("function")[1]
        self.match("symbol")  # Skip "("
        parameters = []
        while self.current_token()[1] != ")":
            parameters.append(self.match("variable")[1])
            if self.current_token()[1] == ",":
                self.match("symbol")
        self.match("symbol")  # Skip ")"
        self.match("symbol")  # Skip "{"
        body = self.parse_body()
        self.match("symbol")  # Skip "}"
        return {"FunctionDeclaration": {"name": function_name, "parameters": parameters, "body": body}}

    def parse_for_loop(self):
        self.match("for loop")  # Skip "for"
        variable = self.match("variable")[1]
        self.match("function")  # Skip "in"
        self.match("function")  # Skip "range"
        self.match("symbol")  # Skip "("
        range_values = [] 
        while self.current_token()[1] != ")":
            range_values.append(self.match(self.current_token()[0])[1])
            if self.current_token()[1] == ",":      
                self.match("symbol")  #skip "," in range of for
        self.match("symbol")  # Skip ")"
        self.match("symbol")  # Skip "{"
        body = self.parse_body()
        self.match("symbol")  # Skip "}"

        return {"ForLoop": {"variable": variable, "range": range_values, "body": body}}

    def parse_while_loop(self):
        self.match("while loop")  # Skip "while"
        self.match("symbol")  # Skip "("
        condition = self.parse_condition()
        self.match("symbol")  # Skip ")"
        self.match("symbol")  # Skip "{"
        body = self.parse_body()
        self.match("symbol")  # Skip "}"

        return {"WhileLoop": {"condition": condition, "body": body}}

    def parse_body(self):
        body = []
        while self.current_token()[1] != "}":
            token_type, token_value = self.current_token()

            if token_type == "variable" and self.peek_next() and self.peek_next()[0] == "operator":
                body.append(self.parse_variable_declaration())
            elif token_type == "if statement":
                body.append(self.parse_if_statement())
            elif token_type == "output function":
                body.append(self.parse_print_statement())
            else:
                self.token_index += 1  # Skip unrecognized tokens
        return body

    def parse_if_statement(self):
        self.match("if statement")  # Skip "if"
        self.match("symbol")  # Skip "("
        condition = self.parse_condition()
        self.match("symbol")  # Skip ")"
        self.match("symbol")  # Skip "{"
        body = self.parse_body()
        self.match("symbol")  # Skip "}"

        elif_clauses = []
        while self.current_token()[0] == "else if statement":
            self.match("else if statement")  # Skip "elif"
            self.match("symbol")  # Skip "("
            elif_condition = self.parse_condition()
            self.match("symbol")  # Skip ")"
            self.match("symbol")  # Skip "{"
            elif_body = self.parse_body()
            self.match("symbol")  # Skip "}"
            elif_clauses.append({"condition": elif_condition, "body": elif_body})

        else_clause = None
        if self.current_token()[0] == "else statement":
            self.match("else statement")  # Skip "else"
            self.match("symbol")  # Skip "{"
            else_clause = self.parse_body()
            self.match("symbol")  # Skip "}"

        return {
            "IfStatement": {
                "condition": condition,
                "body": body,
                "elif": elif_clauses,
                "else": else_clause,
            }
        }

    def parse_print_statement(self):
        self.match("output function")  # Skip "print"
        self.match("symbol")  # Skip "("
        arguments = []

        while self.current_token()[1] != ")":
            arguments.append(self.match(self.current_token()[0])[1])
            if self.current_token()[1] == ",":
                self.match("symbol")
        self.match("symbol")  # Skip ")"
        
        return {"PrintStatement": {"arguments": arguments}}

    def parse_condition(self):
        condition = []
        while self.current_token()[1] != ")":
            token_type, token_value = self.current_token()
            if token_type in ["variable", "number", "string"]:
                condition.append(self.match(token_type)[1])
            elif token_type == "operator":
                condition.append(self.match("operator")[1])
            elif token_type == "symbol" and token_value in ["+", "-", "*", "/"]:
                condition.append(self.match("symbol")[1])
            else:
                self.token_index += 1  # Skip unrecognized tokens
        return " ".join(condition)

    def peek_next(self):
        if self.token_index + 1 < len(self.token_stream):
            return self.token_stream[self.token_index + 1]
        return None

    def print_ast(self, ast, indent=0):
        spacing = " " * indent
        if isinstance(ast, dict):
            print(f"{spacing}{{")
            for key, value in ast.items():
                print(f"{spacing}    '{key}': ", end="")
                self.print_ast(value, indent + 4)
            print(f"{spacing}}}")
        elif isinstance(ast, list):
            print(f"{spacing}[")
            for item in ast:
                self.print_ast(item, indent + 4)
            print(f"{spacing}]")
        else:
            print(f"{spacing}'{ast}'")