## Snow Programming Language 
### Help - Contribution

***

#### Structure
* app - the app
   * app - the main file with threads
   
* core - main code folder
   * compiler - run the file
       * compiler.py
   * errors - all custom errors
       * error.py
       * pointer.py
   * lexer - the lexer
       * cogs - add-ons
          * identifier.py
          * keywords.json
          * numbers.py
          * operators.py
          * symbols.py
       * lexer.py
       * tokens.py
   * parser - the parser
       * parser.py
       * nodes.py
   * interpreter - the interpreter
       * interpreter.py
       * types.py
   
