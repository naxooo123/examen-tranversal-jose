#https://github.com/naxooo123/examen-tranversal-jose.git
import random
import statistics
import math
from random import randint
from math import prod, pow

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignar_sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    return dict(zip(trabajadores, sueldos))

def clasificar_sueldos(sueldos):
    clasificacion = {}
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            categoria = "Bajo"
        elif 800000 <= sueldo <= 1500000:
            categoria = "Medio"
        else:
            categoria = "Alto"
        clasificacion[trabajador] = {"sueldo": sueldo, "clasificacion": categoria}
    return clasificacion

def ver_estadisticas(sueldos):
    valores_sueldos = list(sueldos.values())
    max_sueldo = max(valores_sueldos)
    min_sueldo = min(valores_sueldos)
    promedio_sueldo = sum(valores_sueldos) / len(valores_sueldos)
    media_geometrica = pow(prod(valores_sueldos), 1/len(valores_sueldos))
    
    return {
        "max": max_sueldo,
        "min": min_sueldo,
        "promedio": promedio_sueldo,
        "media_geometrica": media_geometrica
    }

def reporte_sueldos(sueldos):
    reporte = []
    for trabajador, sueldo in sueldos.items():
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        reporte.append(f"{trabajador}: Sueldo Base: ${sueldo}, Descuento Salud: ${descuento_salud:.2f}, Descuento AFP: ${descuento_afp:.2f}, Sueldo Líquido: ${sueldo_liquido:.2f}")
    return "\n".join(reporte)

def menu():
    sueldos = {}
    while True:
        print("\nMenu de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            sueldos = asignar_sueldos()
            print("Sueldos asignados aleatoriamente")
        elif opcion == '2':
            if not sueldos:
                print("Primero debe asignar sueldos")
                continue
            clasificaciones = clasificar_sueldos(sueldos)
            print("Clasificación de sueldos:")
            for trabajador, datos in clasificaciones.items():
                print(f"{trabajador}: ${datos['sueldo']} - {datos['clasificacion']}")
        elif opcion == '3':
            if not sueldos:
                print("Primero debe asignar sueldos")
                continue
            stats = ver_estadisticas(sueldos)
            print(f"Estadisticas:\nMaximo: ${stats['max']}\nMinimo: ${stats['min']}\nPromedio: ${stats['promedio']}\nMedia Geométrica: ${stats['media_geometrica']:.2f}")
        elif opcion == '4':
            if not sueldos:
                print("Primero debe asignar sueldos")
                continue
            print("Reporte de sueldos:")
            print(reporte_sueldos(sueldos))
        elif opcion == '5':
            print("Finalizando Programa...")
            print("Desarrolado por Jose Quintanilla")
            print("Rut: 20.974.191-1")
            break
        else:
            print("Opcion no valida. Intente nuevamente")

if __name__ == "__main__":
    menu()
            