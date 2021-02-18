# This is a sample Python script.
import re

#Pedir correo
print('Buen dia, ingrese un su electronico Ej: juan.valenzuela@curso.python.mx \n\tSu correo:')
correoin = input();
#Validar correo nombre, ., nombre, @, curso, ., python, ., mx.
if re.match ('^[\w]+[.]?[\w]+[@]{1}curso{1}[.]{1}python{1}[.]{1}mx{1}$', correoin) :
    print('Correo valido.\n')
else:
    print('Correo invalido.\n')

#Pedir numero
print('Ahora introduzca un numero telefonico Ej: 3312345678, (33)12345678, (331) 123-5678 \n\tSu numero:')
telin = input();
#Validar numero 10 digitos
if re.match ('^[\d]{10}$', str().join(re.findall('[\d]{1}', telin))):
    print('Numero valido.\n')
else:
    print('Numero invalido.\n')

#Pedir RFC
print('Ahora introduzca un su RFC Ej: IPL1302278QA \n\tSu RFC:')
rfcin = input();
#Validar RFC 3 mayusculas, 7 numeros, 2 mayusculas
if re.match ('^[A-Z]{3}[\d]{7}[A-Z]{2}$', rfcin):
    print('RFC valido.\n')
else:
    print('RFC invalido.\n')

#Pedir Curp
print('Ahora introduzca un su CURP Ej: MAHJ280603MSPRRV09 \n\tSu CURP:')
curpin = input();
#Validar CURP 4mayusculas, 6 numeros, 6 mayusculas, 2 numeros
if re.match ('^[A-Z]{4}[\d]{6}[A-Z]{6}[\d]{2}$', curpin):
    print('CURP valido.\n')
else:
    print('CURP invalido.\n')
