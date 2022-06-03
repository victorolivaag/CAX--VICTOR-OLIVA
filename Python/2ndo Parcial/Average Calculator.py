grade1=int(input("ingresa calificacion de materia 1:"))
grade2=int(input("ingresa calificacion de materia 1:"))
grade3=int(input("ingresa calificacion de materia 1:"))

suma=grade1+grade2+grade3
promedio=suma/3

print("tu promedio de las 3 matieras es de: ", promedio )
if(promedio<6):
  print('estas reporbado, lo siento')

if(promedio>=6 and promedio<9):
  print('has aprovado, bien hecho')

if(promedio>=9):
  print('has obtenido un bonus! felicidaes!')
