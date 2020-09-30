## Snow Programming Language 
### Help - Contribution

***

#### Tokens
| Chars     | Token Type   |
|-----------|--------------|
| \d+.\d+   | INT \| FLOAT |
| A-Za-z_\d | ID           |
| (         | LPAREN       |
| )         | RPAREN       |
| =         | EQ           |
| ==        | DBEQ         |
| :         | COLON        |
| :=        | WALRUS       |
| >         | GT           |
| <         | LT           |
| >=        | GTEQ         |
| <=        | LTEQ         |
| !         | NOT          |
| !=        | NOTEQ        |
| {         | LCURLY       |
| }         | RCURLY       |
| ,         | COMMA        |
| keywords  | KEYWORD      |


#### Nodes
See core/parser/nodes.py

#### Types
See core/interpreter/types.py
