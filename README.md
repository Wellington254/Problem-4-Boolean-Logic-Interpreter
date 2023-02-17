# Problem-4-Boolean-Logic-Interpreter
A simple parser for evaluating Boolean expressions is implemented in Python. 
It takes an input expression and builds a simple Abstract Syntax Tree. The syntax for the simple language is as follows:
T  represents True
F represents False
.  represents the and operator
+ represents the or operator
~ represents the not operator
= is used to assign a boolean value to a variable (not implemented yet).
For example:
  T.T will return True
  T.F False
  ~T.T will return False
Single upper case letters other than T or F can be used as variables(implementation not complete).

In a complete implementation the Abstract Syntax Tree can be used with the Terminal and Non-terminal classes to solve boolean expressions. The implementation is however not complete. 
