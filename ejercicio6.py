alumno = {}

alumno["nombre"] = input("Nombre del alumno: ")
alumno["Numero de alumno"] = input("Numero de alumno: ")
alumno["carrera"] = input("Carrera: ")
alumno["promedio"] = float(input("Promedio: "))

estado = "Aprobado" if alumno["promedio"] >= 70 else "Reprobado"

print(f"\nAlumno: {alumno['nombre']} ({alumno['Numero de alumno']})")
print(f"Carrera: {alumno['carrera']}")
print(f"Promedio: {alumno['promedio']}")
print(f"Estado: {estado}")
