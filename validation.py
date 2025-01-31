from sympy import sympify, SympifyError, symbols

def validateEquation(Fn):
  try:
    x = symbols('x')
    expression = sympify(Fn)
    # Check if the expression contains only valid symbols
    if expression.free_symbols - {x}:
        return False, "Invalid symbols in the function. Only 'x' is allowed."
    return True, expression
  except SympifyError:
      return False, "Invalid function. Please enter a valid mathematical expression."
  except Exception as e:
      return False, f"An error occurred: {str(e)}"