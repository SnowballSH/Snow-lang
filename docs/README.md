## Snow Programming Language 
### Help - Contribution

***

#### Usage
Snow Language version 0.5.0(Which is the first version after rewrite) will be on github and PyPi soon 😄
See docs/tour.md for language tour!

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
