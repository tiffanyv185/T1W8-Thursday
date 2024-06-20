# __repr__ method
- Special method, like __init, which is used to define a string representation for a object
- Particularly used for debugging and development because it can give detailed info about an object.

# Composition of OOP
- Design principle where a class is composed of one or more objects from other classes.
- It's an alternative to Inheritance and is often more flexible and modular.
- Avoids inheritance's pitfall: changes in base class can unintentionally affect the derived class, which may break their functionality,
- Composition does not directly affect the composed class, as the class inherits with component classes through well-defined interaces.

# Error Handling
## Taxonomy of Python Errors
- Silent Logical Errors:
- Assertion Errors: raised when 'assert' statement fails. If condition is True, nothing happens, if falce, raises AssertionError
- Syntax Errors: Errors in the written syntax, that Python interpreter cannot understand
- Exceptions - Runtine errors, occurs during program execution. Python has built-in exception to handle common errors.

# Stack Trace Interpretation
- Text that appears when Python encounters an exception, "stack trace"

# Try/ Except/ Finally
- Comprehensive way to handle exceptions
- Ensures code always runs, regardless wether an error occurs.
- 'try' block has code that may raise exceptions
- 'except' block has code that handles exceptions
- 'finally' 