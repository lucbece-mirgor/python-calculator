class DivisionByZeroError(Exception):
    pass

class Calculator:
    def __init__(self):
        self.num1, self.num2 = self.leer_enteros()
        self.historial = []

    def leer_enteros(self):
        while True:
            try:
                num1, num2 = map(int, input("Ingrese dos numeros enteros separados por coma: ").split(','))
                return num1, num2
            except ValueError:
                print('Los numeros ingresados deben ser enteros. Intentelo nuevamente')
    
    def setear_enteros(self, num1, num2):
        self.num1, self.num2 = num1, num2

    def _leer_operacion(self):
        while True:
            operator = input('Ingrese un operador (+, -, *, /): ')
            if operator in ('+', '-', '*', '/'):
                return operator
            else:
                print(f'El operador {operator} no es valido. Intente nuevamente')

    def _guardar_historial(self, num1, num2, operator, result):
        operators_string = {
            '+': 'suma',
            '-': 'resta',
            '*': 'multiplicacion',
            '/': 'division'
        }
        operacion_string = f'La {operators_string[operator]} entre {num1} y {num2} es {result}'
        self.historial.append(operacion_string)

    def _sumar(self):
        return self.num1 + self.num2
    
    def _restar(self):
        return self.num1 - self.num2

    def _multiplicar(self):
        return self.num1 * self.num2

    def _dividir(self):
        if self.num2 == 0:
            raise DivisionByZeroError('No se puede dividir por cero')
        return self.num1 / self.num2

    def mostrar_resultado(self, resultado):
        print(resultado)

    def mostrar_historial(self):
        for historia in self.historial:
            print(f'{historia} \n')

    def realizar_operacion(self):
        operators = {
            '+': self._sumar,
            '-': self._restar,
            '*': self._multiplicar,
            '/': self._dividir
        }

        operator = self._leer_operacion()
        try:
            result = operators[operator]()
        except DivisionByZeroError as e:
            result = str(e)
        else:
            self._guardar_historial(self.num1, self.num2, operator, result)
        finally:
            self.mostrar_resultado(result)
        



