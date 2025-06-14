'''rut tiene que ser formato "texto" en un input solo
   diccionario ejemplo:
   {rut :[nombre,apellidoPaterno,edad,estadoCivil,sexo, fecha_afiliacion]}'''
from datetime import date
from random import randint
from rutificador import Rut as validar
personas={}
sw=0

while sw==0:
    print("-"*8)
    print("Bienvenido a Vida y Salud")
    print("-"*8)
    print("1.Ingresar usuarios")
    print("2.Buscar Usuario")
    print("3.Imprimir Certificado ")
    print("4.SALIR")
    try:
        opcion=int(input("Ingrese opción: "))
        assert(opcion in range(1,5))
    except ValueError:
        print("Debe ingresar una opción válida")
        continue
    except AssertionError:
        print("Debe elegir una opcion: [1-2-3-4]")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
    if opcion==1:
        while True:
            try:
                rut=input("Ingrese su rut: (00000000-0) ")
                nombre=str(input("Ingrese su Nombre: "))
                apellidoPaterno=str(input("Ingrese su apellido paterno: "))
                edad=int(input("Ingrese su edad: "))
                estadoCivil=str(input("Ingrese su estado civil: [Soltero: S, Casado: C , Viudo: V] ")).upper().strip()
                sexo=str(input("Ingrese su género: [Masculino - Femenino] "))
                fecha_afiliacion=input("Ingrese la fecha de afiliacion (dd/mm/aaaa): ")
                assert(edad>=18)
            except ValueError:
                print("Ha ingresado informacion incorrecta ")
                continue
            except AssertionError:
                print("La edad debe ser mayor o igual a 18")
                continue
            except Exception as e:
                print("Ha ocurrido un error: ",e)
                continue
            if validar(rut):
                print(f"El rut {rut} es válido")
            else:
                print("Rut inválido")
                continue
            if estadoCivil=="C":
                estadoCivil="Casado"
            elif estadoCivil=="S":
                estadoCivil="Soltero"
            elif estadoCivil=="V":
                estadoCivil="Viudo"
            else:
                print("Debe ingresar una opcion valida para su estado civil")
                continue
            
                
            personas={rut:{"Nombre": nombre, "Apellido": apellidoPaterno,
                            "edad":edad, "estadoCivil": estadoCivil, "Sexo":sexo, "fecha_afiliacion": fecha_afiliacion}}
            print(personas[rut]["Nombre"])
            break

          
    elif opcion == "4":
        print("\n*******************************")
        print("\nGracias por usar el registro de afiliados de Isapre VIDA Y SALUD")
        print("\nIntegrantes: Nicolás Fernandez \nBenjamín Gutierrez \nJavier Valtierra \nJohans Sepulveda")
        print("\n Python:3.1 ")
        print("\n*******************************")
        break
    else:
        print("\nOpcion invalida porfavor reintente ")
    

