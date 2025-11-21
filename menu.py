def datos_usuario():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    carrera = input("Carrera: ")
    print(f"Hola {nombre}, estudias {carrera} y tienes {edad} años.")

def evaluar_numero():
    try:
        n = float(input("Número: "))
        print("Positivo" if n > 0 else "Negativo" if n < 0 else "Cero")
        print("Par" if n % 2 == 0 else "Impar")
    except:
        print("Entrada inválida.")

def suma_promedio():
    try:
        n = int(input("¿Cuántos números?: "))
        nums = [float(input(f"{i+1}: ")) for i in range(n)]
        print("Cantidad:", n)
        print("Suma total:", sum(nums))
        print("Promedio:", sum(nums)/n)
    except:
        print("Entrada inválida.")

def lista_estudiantes():
    lista = [input(f"Nombre {i+1}: ") for i in range(5)]
    print("Lista original:", lista)
    print("Primer elemento:", lista[0])
    print("Último elemento:", lista[-1])
    print("Lista ordenada:", sorted(lista))

def area_rectangulo():
    try:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", b * h)
    except:
        print("Entrada inválida.")

def info_alumno():
    nombre = input("Nombre: ")
    matricula = input("Matrícula: ")
    carrera = input("Carrera: ")
    try:
        prom = float(input("Promedio: "))
        estado = "Aprobado" if prom >= 7 else "Reprobado"
        print(f"\nAlumno: {nombre} ({matricula})")
        print("Carrera:", carrera)
        print("Promedio:", prom)
        print("Estado:", estado)
    except:
        print("Entrada inválida.")

def mostrar_todo():
    print("DATOS ALMACENADOS.")

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Datos del usuario")
        print("2. Evaluar número")
        print("3. Suma y promedio")
        print("4. Lista de estudiantes")
        print("5. Área de rectángulo")
        print("6. Información del alumno")
        print("7. Mostrar todos los datos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if   opcion == "1": datos_usuario()
        elif opcion == "2": evaluar_numero()
        elif opcion == "3": suma_promedio()
        elif opcion == "4": lista_estudiantes()
        elif opcion == "5": area_rectangulo()
        elif opcion == "6": info_alumno()
        elif opcion == "7": mostrar_todo()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

menu()
