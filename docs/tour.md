# Language Tour

### Comments

You are able to use comments in Snow, by character '#'.

```python
# I am a comment
i = 1  # I am also a comment
```

### Numbers

You are able to use integers and floats in Snow.

```python
3  # an integer
3.99  # a float
3.  # a float: 3.0
```

**Snow doesn't support unary numbers until now. It will be added in a few commits.**

### Operators

You can use +-*/ operators, like in any other languages.

```python
3.8 + 2.7 / (2 - 3)
```

### Print something

##### Basic

Now, the most basic thing, you can print anything now!

```python
out 3 - 2 * 5  # out stands for console output
>>> -7
```

##### Shrink code

Since 'out' is a keyword in Snow, you don't have to put parenthesis.

```python
out(2-8)*4-1
>>> -25
```

### Comparisons

You can use comparisons as any other languages.

```python
out 3 >= 2
>>> True  # comparisons returns type 'Bool'
```

### Data types

These are all of the data types in Snow:

| Name     | About      | Callable |
|----------|------------|----------|
| Number   | any number | No       |
| Void     | Void/None  | No       |
| Bool     | True/False | No       |
| Function | Function   | Yes      |

### Variables

##### Assign Variables

```python
# Use <identifier> = <value>
i = 3
a = i + 1
i = a / (3 * 9)
i = i * i + i
```

##### Use/Access and print variables

```python
u = 4 - 3
out u
>>> 1
```

##### Advanced
###### Walrus assign - shrink your code

```python
# Use (<identifier> := <value>)
# Don't forget the parenthesis!
out(u:=4-3)  # Shorter code than the last example
>>> 1
out u  # You can still access it
>>> 1
```

### If statement

Syntax:
```python
if <statement> { <do something> } 
if <statement> { <do something> } else { <do something else> }
```

##### Basic
```python
if 1 == 2 {
  out Void  # it will never be triggered until Earth is eaten
} else {
  out True
}
>>> True

# To shrink it:
if 1==2{out Void}else{out True}
>>> True
```

##### Nested if statements
```python
if 1 == 2 {
  out Void
} else {
  out True
  if 1 != 1 {
    out False
  }
  if 1 >= 0 {
    out 1
    out 1 >= 0
  }
}
>>> True
    1
    True
```

### Loops

##### Basic loop

A basic loop in Snow means an infinite loop, using 'loop' keyword

```python
i = 0
loop {
  out i
  i = i + 1
  if i > 5 {
    break  # break out the infinite loop
  }
}
>>> 0
    1
    2
    3
    4
    5
```

##### Repeat

By using 'repeat' keyword, you can repeat some code n times.

Syntax: `repeat <int> { <do something> }`

The last example can be easier done by:
```python
i = 0
repeat 6 {
  out i
  i = i + 1
}
>>> 0
    1
    2
    3
    4
    5
```

_Note: breaking inside a repeat is also allowed_

### Functions

Syntax: `fn <name> ( <args separated by ','> ) { <do something> }`

_Note: Fonctions has their own variable tree, so you cannot access variables created inside from outer scope or another function._

```python
# fibonacci sequence in Snow
fn fib(n) {
    a = 0
    b = 1
    repeat n {
        h = b
        a = b
        b = a + h
    }
    return a
}
out (long := fib(500))
>>> (a big number)

# Shrink the code
fn f(n){a=0b=1repeat n{h=b a=b b=a+h}return a}
out (short := f(500))
>>> (the same big number)

out long == short
>>> True
```

### Errors

Errors are pretty straight forward, since it provides details on what you did wrong.

It also points out the Error char and position

### Shrink the code!

In Snow, you can make code even shorter than ruby and python.

For example, fibonacci sequence can be made by `fn f(n){a=0b=1repeat n{h=b a=b b=a+h}return a}` 😎
