

#Agregar mas funciones lambda

import os
from peewee import *

#database
db = SqliteDatabase('Administracion.db')
class Empresa(Model):
    id=CharField()
    nombre = CharField()
    class Meta:
        database = db

class Empleado(Model):
    id = CharField()
    nombre = CharField() 
    empresa = ForeignKeyField(Empresa, backref='empleados')
    class Meta:
        database = db




#menus
cls = lambda: os.system('cls')
res = 0
def menu_principal():
    cls()
    print("\n**PROGRAMA ADMINISTRADOR DE EMPRESAS Y EMPLEADOS**")
    print("Seleccione la tabla que desee manipular (para dar de alta a un empleado, debe existir por lo menos una empresa)")
    print("1) Empresas")
    print("2) Empleados")
    print("3) Salir")

def menu_empresas():
    cls()
    print("\n**EMPRESAS**")
    print("Seleccione una opcion")
    print("1) Alta\n2) Baja\n3) Cambios\n4) Ver tabla\n5) Regresar")

def menu_empleados():
    cls()
    print("\n**EMPLEADOS**")
    print("Seleccione una opcion")
    print("1) Alta\n2) Baja\n3) Cambios\n4) Ver tabla\n5) Regresar")

def alta_empresas():
    cls()
    print("\n** ALTAS DE EMPRESAS ** ")
    while True:
      print("ID de la empresa: ")
      ID=input()
      search = Empresa.select().where(Empresa.id == ID)
      if search.exists() == False:
        break
      print("El ID ya existe")
    print("Nombre de la empresa: ")
    nombre=input()

    empresa=Empresa.create(id=ID,nombre=nombre)

def alta_empleados():
    cls()
    print("\n** ALTAS DE EMPLEADOS ** ")
    while True:
      print("ID del empleado: ")
      ID=input()
      search = Empleado.select().where(Empleado.id == ID)
      if search.exists() == False:
        break
      print("El ID ya existe")
     
    print("Nombre del empleado: ")
    nombre=input()

    print("\n**DATOS DE EMPRESAS ** ")
    print("ID    \tNombre      ")

    query=Empresa.select()
    for empresa in query:
        print(empresa.id + "\t"+empresa.nombre)
    try:     
          print("\nID Empresa para la cual trabaja:")
          ID_empresa=input()
          search = Empresa.select().where(Empresa.id == ID_empresa)
          empleado=Empleado.create(id=ID,nombre=nombre,empresa=search)
    except: 
          print("\n¡Error!          Empresa no registrada")
          input()
            
            

      

def baja_empresas():
    cls()
    print("\n** BAJAS DE EMPRESAS ** ")
    try:
      print("ID de la empresa: ")
      ID=input()
      search = Empresa.select().where(Empresa.id == ID).get()
      search.delete_instance()
      print("\nRegistro eliminado con exito")
    except: 
      print("\n¡Error!          Empresa no registrada")
    
    


def baja_empleados():
    cls()
    print("\n** BAJAS DE EMPLEADOS ** ")
    try:
      print("ID del empleado: ")
      ID=input()
      search = Empleado.select().where(Empleado.id == ID).get()
      search.delete_instance()
      print("\nRegistro eliminado con exito")
    except:
      print("\n¡Error!          Empleado no registrado")



def cambio_empresas():
    cls()
    print("\n** CAMBIO DE DATOS DE EMPRESAS ** ")
    try:
      print("ID de la empresa que quiere cambiar datos: ")
      ID=input()
      search = Empresa.select().where(Empresa.id == ID).get()
      print("\nEmpresa encontrada: "+search.nombre)    
      cls()
      print("Escriba el nuevo nombre: ")
      string=input()
      search.nombre=string
      search.save()
      print("Registro actualizado")
    except:
      print("\n¡Error!          Empresa no registrada")


def cambio_empleados():
    cls()
    print("\n** CAMBIO DE DATOS DE EMPLEADOS ** ")
    try:
      print("ID del empleado que quiere cambiar datos: ")
      ID=input()
      search = Empleado.select().where(Empleado.id == ID).get()
      print("\nEmpleado encontrado: "+search.nombre)
      print("\n¿Que campo desea cambiar?\n")
      print("1) Nombre")
      print("2) Empresa donde labora")
      op=input()
      if op=='1':
          cls()
          print("Escriba el nuevo nombre")
          string=input()
          search.nombre=string
          search.save()
          print("Registro actualizado")

      elif op=='2':
          cls()
          print("Escriba el ID de la empresa donde labora: ")
          string_id=input()
          query_empresa= Empresa.select().where(Empresa.id == string_id)
          search.empresa=query_empresa
          search.save()
          print("Registro actualizado")
    except:
      print("\n¡Error!          El dato no coincide con algun registro")
      

def ver_empresas():
    cls()
    print("\n** VER DATOS DE EMPRESAS ** ")
    print("ID    \tNombre      ")

    query=Empresa.select()
    for empresa in query:
        print(empresa.id + "\t"+empresa.nombre)

    input()
        

def ver_empleados():
    cls()
    print("\n** VER DATOS DE EMPLEADOS ** ")
    print("ID    \tNombre      \tEmpresa")
    query=Empleado.select(Empleado,Empresa).join(Empresa)
    for empleado in query:
        print(empleado.id+"\t"+empleado.nombre+"\t"+empleado.empresa.nombre) 
    
    input() 
 


#database connection
db.connect()
db.create_tables([Empresa, Empleado]) 

operaciones = lambda x,y,z: x+y+z
a,b,c=0,0,0
while True :
  menu_principal()
  op = input()
  if op == '1':
    while True :
      menu_empresas()
      op = input()
      if op=='1':
        alta_empresas()
        a=a+1
      if op=='2':
        baja_empresas()
        b=b+1
        input()
      if op=='3':
        cambio_empresas()
        c=c+1
        input()
      if op=='4':
        ver_empresas()
      if op=='5':
        break
  if op=='2':
    while True :
     menu_empleados()
     op=input()
     if op=='1':
        alta_empleados()
        a=a+1
     if op=='2':
        baja_empleados()
        b=b+1
        input()
     if op=='3':
        cambio_empleados()
        c=c+1
        input()
     if op=='4':
        ver_empleados()
     if op=='5':
        break
  if op == '3':
      break

cls()      
operaciones(a,b,c)
print("Se hicieron un total de "+str(operaciones(a,b,c))+" manipulaciones de datos")    
db.close()