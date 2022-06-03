
E1=97
I1=98
M1=95
H1=93
R1=99

E2=99
I2=89
M2=98
H2=93
R2=91

E3=95
I3=99
M3=100
H3=100
R3=96


suma = E1+ E2 + E3
totalEspañol = suma / 3
print("español", totalEspañol)

suma = I1+ I2 + I3
totalInformatica = suma / 3
print("Informatica", totalInformatica)

suma = M1+ M2 + M3
totalMatematicas = suma / 3
print("Matematicas", totalMatematicas)

suma = H1+ H2 + H3
totalHistoria = suma / 3
print("Historia", totalHistoria)

suma = R1+ R2 + R3
totalRobotica = suma / 3
print("Robotica", totalRobotica)

suma = totalEspañol + totalHistoria + totalInformatica + totalMatematicas + totalRobotica
totalAño = suma / 5
print("mi promedio total del año es", totalAño)