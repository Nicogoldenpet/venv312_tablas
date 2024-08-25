#Fecha: 25/04/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo


#Llamando a la libreria las funciones random, time y msvcrt
from random import*
import platform
import os
import time
import msvcrt


def tablas(): #Definir la función tablas()

    resp = "Y"

#EL ERROR ESTÁ EN EL WHILEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    while resp == "Y":

        #Definir un número random de 1 a 20
        numero = randint(1, 20)
    
        print("---------------------------------------------------------------")
        print("|                                                             |")
        print("|                                                             |")
        print("|                                                             |")
        print("|             BIENVENIDO AL GENERADOR DE TABLAS               |")
        print("|          PARA INGRESAR PRESIONE CUALQUIER TECLA             |")
        print("|                                                             |")
        print("|                                                             |")
        print("|                                                             |")
        print("---------------------------------------------------------------")
        msvcrt.getch()
        
        
        #Mostrando el número de tablas a generar
        print("-------------------------------------------------------")
        print(f"Aquí están las tablas de multiplicar del 1 al {numero}")
        print("-------------------------------------------------------")
        print("")

        #Bucle for para el primer factor
        for tabla in range(1, numero + 1):

            #Mostrando la tabla de multiplicar dada por el for
            print(f"Tabla del {tabla}:")

            #Bucle for para el segundo factor
            for i in range(1, 11):

                #Definiendo el resultado de ambos factores
                res = tabla * i

                #Mostrando el resultado de las multiplicaciones de cada tabla
                print(f"{tabla} x {i} = {res}")
            print("*************************")
            
            print("Presione una tecla para continuar...")
            msvcrt.getch()
            
            #Definiendo el tiempo de espera en 1 para limpiar la pantalla
            time.sleep(0.1)
            
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
                
        #Preguntando al usuario si desea generar más tablas
        resp = None
        while resp != "Y" and resp != "N":
            print("¿Desea generar otras tablas de multiplicar? (El programa se reiniciará) (Y/N): ")
            resp = msvcrt.getwch()
                
if __name__=="__main__":
    tablas()


