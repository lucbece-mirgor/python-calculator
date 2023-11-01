class DivisionByZeroError(Exception):
    pass

class Calculator:
    def __init__(self):
        self.num1, self.num2 = self.leer_enteros()
        self.historial = []

    def leer_enteros(self):
        # Lee y retorna dos numeros enteros
        while True:
            try:
                num1, num2 = map(int, input("Ingrese dos numeros enteros separados por coma: ").split(','))
                return num1, num2
            except ValueError:
                print('Los numeros ingresados deben ser enteros. Intentelo nuevamente')
    
    def setear_enteros(self, num1, num2):
        # Setea los enteros num1 y num2 como atributos de la clase
        self.num1, self.num2 = num1, num2

    def _leer_operacion(self):
        # Lee un string para definir la operacion a realizar
        while True:
            operator = input('Ingrese un operador (+, -, *, /): ')
            if operator in ('+', '-', '*', '/'):
                return operator
            else:
                print(f'El operador {operator} no es valido. Intente nuevamente')

    def _guardar_historial(self, num1, num2, operator, result):
        # Guarda el resultado de una operacion en el atributo historial
        operators_string = {
            '+': 'suma',
            '-': 'resta',
            '*': 'multiplicacion',
            '/': 'division'
        }
        operacion_string = f'La {operators_string[operator]} entre {num1} y {num2} es {result}'
        self.historial.append(operacion_string)

    def _sumar(self):
        # Suma y retorna dos numeros enteros
        return self.num1 + self.num2
    
    def _restar(self):
        # Resta y retorna dos numeros enteros
        return self.num1 - self.num2

    def _multiplicar(self):
        # Multiplica y retorna dos numeros enteros
        return self.num1 * self.num2

    def _dividir(self):
        # Divide y retorna dos numeros enteros
        if self.num2 == 0:
            raise DivisionByZeroError('No se puede dividir por cero')
        return self.num1 / self.num2

    def mostrar_resultado(self, resultado):
        # Imprime en pantalla el resultado de una operacion
        print(resultado)

    def mostrar_historial(self):
        # Imprime en pantalla las operaciones realizadas
        for historia in self.historial:
            print(f'{historia} \n')

    def realizar_operacion(self):
        # Dados dos numeros enteros y un operador, realiza la operacion, la guarda en el historial y la muestra en pantalla
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
        



