# Reto-06

1. Add the required exceptions in the Reto 1 code assigments.
2. In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

```python
class OperadorInvalido(Exception):
    def __init__(self, message):
        super().__init__(message)


class Calculadora:
    def operaciones(self, a: int | float,b: int | float ,operacion: str) -> int:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los valores deben ser números.")
        else:
            # Revisa el caracter ingresado y realiza la operación correspondiente
            match operacion:
                case "+":
                    return a + b
                case "-":
                    return a - b
                case "*" | "x":
                    return a * b
                case "/" | "÷":
                    if b == 0:
                        raise ZeroDivisionError("No se puede dividir por cero.")
                    else: return a / b
                case _:
                    raise OperadorInvalido("No ingresaste un operador valido") 

try:
    calculadora = Calculadora()
    print(calculadora.operaciones(4, 3, "+"))
    print(calculadora.operaciones(4, 4, "-"))
    print(calculadora.operaciones(5, 2, "*"))
    print(calculadora.operaciones(8, 2, "x"))
    print(calculadora.operaciones(10, 0, "/"))
    print(calculadora.operaciones(12, 2, "÷"))
except (TypeError, ZeroDivisionError, OperadorInvalido) as error:
    print(f"Error: {error}")

try:
    print(calculadora.operaciones(4, 2, "´"))  # Operador inválido
except (TypeError, ZeroDivisionError, OperadorInvalido) as error:
    print(f"Error: {error}")

try:
    print(calculadora.operaciones("a", "b", "´"))  # Tipo inválido
except (TypeError, ZeroDivisionError, OperadorInvalido) as error:
    print(f"Error: {error}")

```

### Output: 
```
7
0
10
16
Error: No se puede dividir por cero.
Error: No ingresaste un operador valido
Error: Los valores deben ser números.
```
