from calculadora import Calculator


def main_menu():
    calculadora = Calculator()
    calculadora.realizar_operacion()

    while True:
        print('Ingrese "si" para salir del calculador ')
        print('Ingrese "historial" para ver las operaciones realizadas ')
        print('Cualquier otro input iniciara un nuevo calculo ')

        exit = input(': ')

        if exit == 'si':
            break
        elif exit == 'historial':
            calculadora.mostrar_historial()
            continue

        num1, num2 = calculadora.leer_enteros()
        calculadora.setear_enteros(num1, num2)
        calculadora.realizar_operacion()
    return


main_menu()
