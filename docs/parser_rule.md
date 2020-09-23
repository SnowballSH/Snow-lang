## The Parser Rules

##### Used in Parser:

* **Expr**
    * Keywords
        * Out
            * get _Expr_
        * If
            * get _Comp_
            * {
            * loop until eof or } :
                * get _Expr_
            * }
            
    * return get Comp

* **Comp**
    * get _Layer 1_ as "left"
    * if current is comparison
        * loop until eof or current is not comparison :
            * get _Layer 1_
        * left = CompList of these comparisons
    * return "left"
    
* **Layer 1**
    * get _Layer 2_ as "left"
    * loop until eof or current is not in (+, -) :
        * get _Layer 2_
    * return "left"
    
* **Layer 2**
    * get _Factor_ as "left"
    * loop until eof or current is not in (*, /) :
        * get _Factor_
    * return "left"
    
* **Factor** 
    * ()
        * return get _Expr_
    * INT, FLOAT
        * return INT or FLOAT
    * ID
        * Nothing
            * return VarAccessNode
        * EQ
            * get _Expr_
            * return VarAssignNode
        * WALRUS
            * get _Expr_
            * return WalrusVarAssignNode