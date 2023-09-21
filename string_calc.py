""" string_calc.py
Module providing functions for executing basic calculator operations using String
args. Returns the String literal 'ERROR' when the string input does not represent a
float value. All operations are returned as a string literal.
"""
#Standard ERROR message
error = "ERROR"

def addition(x:str, y:str) -> str:
    """Performs addition operation where two string args can be converted to float values.
    Otherwise returns an error message.
    
    args:
        x:str -- string literal representing the first number to be added
        y:str -- string literal representing the second number to be added
        
    returns:
        Addition of args or an error message in the event of a Value Error
    """
    try:
        z = float(x) + float(y)
        return str(z)
    except ValueError:
        return error

def subtraction(x:str, y:str) -> str:
    """Performs subtraction operation where two string args can be converted to float values.
    Otherwise returns an error message.
    
    args:
        x:str -- string literal representing the number being subtracted
        y:str -- string literal representing the number subtracted from x
        
    returns:
        Subtraction of args or an error message in the event of a Value Error
    """
    try:
        z = float(x) - float(y)
        return str(z)
    except ValueError:
        return error

def divide(x:str, y:str) -> str:
    """Performs division operation where two string args can be converted to float values.
    Otherwise returns an error message.
    
    args:
        x:str -- string literal representing the number being divided
        y:str -- string literal representing the number dividing x
        
    returns:
        Division of args or an error message in the event of a Value Error or a Zero Division Error
    """
    try:
        z = float(x) / float(y)
        return str(z)
    except ValueError:
        return error
    except ZeroDivisionError:
        return "ERROR. zero division."
    
def multiply(x:str, y:str) -> str:
    """Performs multiplication operation where two string args can be converted to float values.
    Otherwise returns an error message.
    
    args:
        x:str -- string literal representing the first number to multiply
        y:str -- string literal representing the second number to multiply
        
    returns:
        Multiplication of args or an error message in the event of a Value Error
    """
    try:
        z = float(x) * float(y)
        return str(z)
    except ValueError:
        return error