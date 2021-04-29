"""
Nombre: invertirLista
Entradas: lista
Salidas: invertir los elementos de una lista
Restricciones: si la lista está vacía devolver 0
"""
def invertirLista(lista):
    if isinstance(lista,list):
        if lista == []:
            return 0
        else:
            return invertir_aux(lista,[])
    else:
        print("Error: el parámetro de entrada debe ser una lista")

def invertir_aux(lista, invertir):
    if lista == []:
        return invertir
    else:
        return invertir_aux(lista[:-1], invertir+[lista[-1]])

#-------------------------------------------------------------------
"""
Nombre: extremosLista
Entradas: lista
Salidas: determina cual es el número menor y mayor de una lista
Restricciones: la lista no puede estar vacía
"""
def extremosLista(lista):
    if isinstance(lista,list):
        if lista == []:
            return print("Error: la lista no puede estar vacía")
        else:
            return extremos_aux(menor_aux(lista,lista[0]),mayor_aux(lista,lista[0]),[])
    else:
        return print("Error: el parámetro de entrada debe ser una lista")

def menor_aux(lista,menor):
    if lista == []:
        return menor
    else:
        if(lista[0]) < menor:
            return menor_aux(lista[1:],lista[0])
        else:
            return menor_aux(lista[1:],menor)

def mayor_aux(lista,mayor):
    if lista == []:
        return mayor
    else:
        if(lista[0]) > mayor:
            return mayor_aux(lista[1:],lista[0])
        else:
            return mayor_aux(lista[1:],mayor)

def extremos_aux(menor,mayor,resultado):
    if menor == 0 or mayor == 0:
        return resultado
    elif menor == mayor:
        return [menor]
    else:
        return extremos_aux(menor-menor,mayor-mayor,resultado+[menor]+[mayor])

#-----------------------------------------------------------------------------------
"""
Nombre: eliminarDigito
Entradas: digito, digito2
Salidas: sacar dígitos de un número
Restricciones: el número no puede ser cero
"""
def eliminarDigito(digito,digito2):
    if isinstance(digito,int) and isinstance(digito2,int):
        if( digito == 0):
            return print("Error: el número no puede ser cero")
        else:
            return eliminar_aux(digito,digito2,0,0)
    else:
        return print("Error: los parámetros de entrada deben ser enteros")

def eliminar_aux(digito,digito2,resultado,contador):
    if (digito == 0):
        return resultado
    elif digito%10== digito2:
        return eliminar_aux(digito//10,digito2,resultado,contador)
    else:
        return eliminar_aux(digito//10,digito2,resultado+(digito%10)*(10**contador),contador+1)

#------------------------------------------------------------------------------------------------
"""
Nombre: nivelesLista
Entradas: lista
Salidas: devolver de una lista de listas la cantidad de sublistas que contiene
Restricciones: el parámetro de entrada debe ser una lista
"""
def nivelesLista(lista):
    if isinstance(lista,list):
        return niveles_aux(lista,[])
    else:
        print("Error: el parámetro de entrada debe ser una lista")

def niveles_aux(lista,resultado):
    if lista == []:
        return resultado
    elif isinstance(lista[0],list):
        return niveles_aux(lista[1:],resultado+[contarLista(lista[0],1)])
    else:
        return niveles_aux(lista[1:],resultado+[0])

def contarLista(lista,contador):
    if lista == []:
        return contador
    elif isinstance(lista[0],list):
        return contarLista(lista[0],contador+1)
    else:
        return contador

#----------------------------------------------------------------------------
"""
Nombre: obtenerIndicesListaVectores
Entradas: vector1, vector2, vector3
Salidas: devolver los índices de una lista de vectores cuyo valores sean cero o un número negativo
Restricciones: los vectores deben tener el mismo tamaño y sus datos deben ser números enteros
"""
def obtenerIndicesListaVectores(vector1,vector2,vector3):
    if isinstance(vector1,list) and isinstance(vector2,list) and isinstance(vector3,list):
        enteros = auxiliar(vector1)
        if enteros == True:
            enteros = auxiliar(vector2)
            if enteros == True:
                enteros = auxiliar(vector3)
                if enteros == True:
                    tamaño = Tamaño(vector1,0)
                    tamaño2 = Tamaño(vector2,0)
                    tamaño3 = Tamaño(vector3,0)
                    if tamaño == tamaño2 == tamaño3:
                        return [indice_aux(vector1,0,[])]+ [indice_aux(vector2,0,[])]+[indice_aux(vector3,0,[])]
                    else:
                        return print("Los vectores no tienen el mismo tamaño")
                else:
                    return print("Los datos del vector3 no son enteros")
            else:
                return print("Los datos del vector2 no son enteros")
        else:
            return print("Los datos del vector1 no son enteros")
    else:
        return print("Los datos de los vectores deben ser una lista")

def auxiliar(vector):
    if vector == []:
        return True
    elif isinstance(vector[0],int):
        return auxiliar(vector[1:])
    else:
        return False

def Tamaño(vector,contador):
    if vector == []:
        return contador
    else:
        return Tamaño(vector[1:],contador+1)

def indice_aux(dato1,indice,ubicacion):
    if dato1 == []:
        return ubicacion
    elif dato1[0] <= 0:
        return indice_aux(dato1[1:],indice+1,ubicacion+[indice])
    else:
        return indice_aux(dato1[1:],indice+1,ubicacion)
