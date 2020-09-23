## Snow Programming Language 
### Help - Contribution

***

#### Usage
Currently under development, can only do things basic now

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
| keywords  | KEYWORD      |


#### Nodes
See core/parser/nodes.py

#### Types
See core/interpreter/types.py
