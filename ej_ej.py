#Depuración y análisis de calificaciones
notas_registradas = [5.5, 8.0, 3.2, -1.0, 6.8, 4.0, 7.5, 2.0]
notas_validas = []
 
for nota in notas_registradas:
    if 1.0 <= nota <= 7.0:
        notas_validas.append(nota)
 
print("Notas válidas:", notas_validas)
 
if len(notas_validas) > 0:
    suma_notas = 0
    for nota in notas_validas:
        suma_notas += nota
 
    promedio = suma_notas / len(notas_validas)
    print(f"Promedio: {promedio:.2f}")
 
    notas_maximas = 0
    for nota in notas_validas:
        if nota == 7.0:
            notas_maximas += 1
 
    print(f"Cantidad de notas 7.0: {notas_maximas}")
 
    nota_minima = notas_validas[0]
    for nota in notas_validas:
        if nota < nota_minima:
            nota_minima = nota
 
    notas_validas.remove(nota_minima)
    print(f"Nota más baja eliminada ({nota_minima}).")
    print("Notas finales:", notas_validas)
else:
    print("No hay notas válidas para calcular el promedio.")

#esto esta bueno no se si chao