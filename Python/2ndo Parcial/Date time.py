import datetime
dia= datetime.date.today()
print(dia)
w=dia.weekday()+1
print(w)
if (w==0):
  print('feliz domingo')
elif (w==1):
  print('Es lunes, matate mejor')
elif (w==2):
  print('Es martes, porqueria de dia')
elif (w==3):
  print('Es miercoles, mitad de semana, ya no esta tan mal')
elif (w==4):
  print('Es jueves, no vayas a la escuela ')
elif (w==5):
  print('Es viernes, fiesta')
else:
  print('yahoo, es sabado')
