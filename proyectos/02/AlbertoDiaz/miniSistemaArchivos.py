#!/usr/bin/python
# -*- Encoding: utf-8 -*-
#Nombre: Carlos Alberto Díaz Olivares



inicio_nombre=[]
fin_nombre=[]
inicio_archivo=[]
fin_archivo=[]
archivo = open("prueba","a+")
inicio_nombre.append(archivo.tell())
print(type(archivo.tell()))
nombre=input("Escribe el nombre del nuevo archivo")
archivo.write(nombre)
fin_nombre.append(archivo.tell())
inicio_nombre.append(archivo.tell())
nombre=input("Escribe el nombre del nuevo archivo")
archivo.write(nombre)
fin_nombre.append(archivo.tell())
archivo.seek(inicio_nombre[0])
print(archivo.read(fin_nombre[0]-inicio_nombre[0]))
archivo.seek(inicio_nombre[1])
print(archivo.read(fin_nombre[1]))
for x in inicio_nombre:
	print(x)
for x in fin_nombre:
	print(x)

