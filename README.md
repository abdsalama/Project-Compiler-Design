# Compiler Design Project: OFA Language

This project is part of our **Compiler Design** course and is supervised by **Dr. Heba El Hadidi**. It involves designing and implementing a compiler for a new programming language called **OFA Language**.

## Team Members
- **Abd-Elrahman Mohammed Salama Eltahrany**
- **Osama Hamed Elkayyal**
- **Fedaa Mohammed Elkanishey**

---

## Features of OFA Language
1. **Variables:** 
   - Declared using the `@` symbol.
   - Example:
     ```ofa
     @x = 15.5
     @name = "hello world"
     ```

2. **Comments:**
   - Single-line comments using `//`.

3. **Conditional Statements:**
   - Includes `if`, `elif`, and `else`.
   - Example:
     ```ofa
     if (@x > 10) {
         print("x > 10");
     } elif (@x == 10) {
         print("x == 10");
     } else {
         print("x < 10");
     }
     ```

4. **Loops:**
   - `for` and `while` loops.
   - Example:
     ```ofa
     for @i in range(1, 10, 1) {
         print(@i);
     }
     ```

5. **Functions:**
   - Declared using the `def` keyword.
   - Example:
     ```ofa
     def sum(@a, @b) {
         return (@a + @b);
     }
     ```

6. **Lists:**
   - Example:
     ```ofa
     @list = [1, 2, 3];
     print(@list[0]);
     ```

7. **Operators:**
   - Arithmetic: `+`, `-`, `*`, `/`
   - Logical: `and`, `or`, `not`
   - Relational: `==`, `!=`, `<`, `>`, `<=`, `>=`

---

## Project Structure
The project consists of the following components:
1. **Lexer** (`Lexer.py`): Performs lexical analysis and tokenizes the source code.
2. **Parser** (`parser.py`): Builds a parse tree from the tokens.
3. **Symbol Table** (`Symbol_Table.py`): Manages variable names, types, and their attributes.
4. **Syntax Documentation** (`syntax.pdf`): Defines the syntax and rules of the OFA Language.
5. **Compiler** (`compiler.py`): Combines the functionality of the lexer, parser, and symbol table into a single executable workflow for source code compilation.

---

## Installation and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/abdsalama/Project-Compiler-Design.git
   cd compiler-design-project
   ```

2. Install Python 3.10+ and required libraries (if any).

3. Run the **Lexer**:
   ```bash
   python Lexer.py
   ```

4. Run the **Parser**:
   ```bash
   python parser.py
   ```

5. Run the **Symbol Table** generator:
   ```bash
   python Symbol_Table.py
   ```

6. Compile your OFA code using the **compiler**:
   ```bash
   python compiler.py
   ```

7. Refer to `syntax.pdf` for details on the OFA Language syntax.

---

## Example Workflow
1. Create your OFA source code.
2. Run the **Lexer** to tokenize the code.
3. Use the **Parser** to validate and build the AST.
4. Analyze symbols with the **Symbol Table**.
5. Use `compiler.py` to execute the full compilation process.

---

## Screenshot
Here is a screenshot of the **compiler Output**:

[Screenshot 2024-12-23 155513](https://github.com/user-attachments/assets/da378caa-ba99-4011-ad2a-0f639526a150)

---

## Supervisor
- **Dr. Heba El Hadidi**

## License
This project is open-source and licensed under the [MIT License](LICENSE).
