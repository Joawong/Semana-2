#ejercicio 1
'''Realice  un  programa  que  dada la base y la altura de un  rectángulo,
calcule el área y el perímetro de este.'''

baseRectan = int(input("Ingrese la base del rectangulo: "))
alturaRectan = int(input("Ingrese la altura del rectangulo: "))
if(alturaRectan > baseRectan):
    print ("Error en un rectangulo la altura no puede ser mayor a la base")
elif(alturaRectan == baseRectan):
    print ('En un rectangulo la base debe ser mayor a la altura, no pueden tener el mismo valor')
    
else:
    print('El área del rectangulo es: ', baseRectan*alturaRectan)
    print('El perimetro del rectangulo es: ', (baseRectan+alturaRectan)*2)



#ejercicio 2
'''Desarrolle un programa que solicite la distancia de su casa a  la Universidad, el costo por kilómetro, la cantidad de días a la  semana que viaja a la Universidad
y que calcule el costo total  de trasladarse por cuatrimestre. Asuma que cada visite implica ida y vuelta y que el cuatrimestre tiene 15 semanas.'''

#ingreso de datos
distancia = float(input('Ingrese la distancia en kilometros que hay de su casa a la universidad: '))
costo_distancia = float(input('Ingrese el costo en colones que gasta por kilómetro: '))
cant_dias = float(input('Ingrese la cantidad de días que asiste a la universidad por semana: '))

print('El costo total por cuatrimestre que implica trasladarse a la universidad es de: ', (((distancia*2)*(cant_dias*15))*costo_distancia))


#ejercicio 3
'''Desarrolle  un  programa que solicite al usuario la edad de 5  personas
y le muestre cuál es la edad promedio'''

edad1 = int(input('Ingrese la edad de la primera persona: '))
edad2 = int(input('Ingrese la edad de la segunda persona: '))
edad3 = int(input('Ingrese la edad de la tercera persona: '))
edad4 = int(input('Ingrese la edad de la cuarta persona: '))
edad5 = int(input('Ingrese la edad de la quinta persona: '))
print('El promedio de la edad de las 5 personas es de: ', (edad1+edad2+edad3+edad4+edad5)/5)


#Ejercicio 4
'''Desarrolle un programa que solicite al usuario la cantidad de  horas semanales trabajadas,
el precio que se le paga por hora  y que calcule el salario mensual.
Considere que se debe aplicar una deducción del 10.5% por  cargas sociales y
5% por asociación solidarista Asuma que cada mes cuenta con 4.2 semanas.'''

horas_trabajadas = int(input('Ingrese la cantidad de horas semanales trabajadas: '))
remuneracion = float(input('Ingrese el precio que se le paga por hora: '))
#reducciones que hay que hacer por mes
remunaracion_neta = remuneracion*(10.5/100)+(remuneracion*(5/100))

salario_mensual = ((horas_trabajadas*remuneracion)*4.2)-remuneracion_net
print(salario_mensual)


#ejercicio 5
ingresos= float(input('Inserte la cantidad de ingresos mensuales: '))
gastos= float(input('Ingrese sus gastos mensuales: '))

porcentaje_gastos= ingresos

#porcentaje= 








            

