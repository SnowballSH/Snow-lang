## Snow Programming Language 
### Help - Contribution

***

#### Usage
Currently under development, can only do things basic now

#### Tokens
| Chars    | Token Type   |
|----------|--------------|
| 0-9.0-9  | INT \| FLOAT |
| A-Za-z_  | ID           |
| (        | LPAREN       |
| )        | RPAREN       |
| =        | EQ           |
| ==       | DBEQ         |
| :        | COLON        |
| :=       | WALRUS       |
| >        | GT           |
| <        | LT           |
| >=       | GTEQ         |
| <=       | LTEQ         |
| !        | NOT          |
| !=       | NOTEQ        |
| keywords | KEYWORD      |


#### Nodes
See core/parser/nodes.py

#### Types
See core/interpreter/types.py
