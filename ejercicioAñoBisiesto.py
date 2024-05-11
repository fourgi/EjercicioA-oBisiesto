#Determinar si un año es o no bisiesto
#Si un año es divisible entre 4, es potencialmente bisiesto.
# Sin embargo, si el año es divisible entre 100 pero no entre 400, entonces no es bisiesto.
# Entonces, en Python, puedes escribir una función simple que implemente esta lógica utilizando operadores de división y módulo (%) para determinar si un año dado es bisiesto o no.
year = int (input("Ingresa el año que deseas evaluar: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print ("El año es bisiesto.")
else:
    print ("El año no es bisiesto.") 
