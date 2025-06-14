'''rut tiene que ser formato "texto" en un input solo
   diccionario ejemplo:
   {rut :[nombre,apellidoPaterno,edad,estadoCivil,sexo, fecha_afiliacion]}'''
from datetime import date
from random import randint as random
#Mi pc me pidio declarar randint as random, no se porque de otra forma no funcionaba
#from rutificador import rut as validar

personas={}
sw=0

while sw==0:
    print("-"*25)
    print("Bienvenido a Vida y Salud")
    print("-"*25)
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
            
            #En mi pc no pude instalar rutificador, por lo que no puedo validar el rut
            
            '''if validar(rut):
                print(f"El rut {rut} es válido")
            else:
                print("Rut inválido")
                continue'''
                
            if sexo.lower() not in ["masculino", "femenino"]:
                print("Debe ingresar un género válido (Masculino o Femenino)")
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
            
                
            personas={rut:{"nombre": nombre, "apellidoPaterno": apellidoPaterno,
                            "edad":edad, "estadoCivil": estadoCivil, "Sexo":sexo, "fecha_afiliacion": fecha_afiliacion}}
            if rut in personas:
                print("Registro exitoso")
            break
        
        #Opcion 1 creada por: Johans Sepulveda
        
    elif opcion==2:
        try :
     
            buscar = input("ingrese el numero de rut para verificar :\n")
     
            if buscar in personas:
                    print("\n---informacion del usuario encontrado---\n")
                    print("rut                 : ",personas[buscar]["rut"])
                    print("nombre              : ",personas[buscar]["nombre"])
                    print("edad                : ",personas[buscar]["edad"])
                    print("estado civil        : ",personas[buscar]["estadoCivil"])
                    print("genero              : ",personas[buscar]["Sexo"])
                    print("fecha de afiliacion : ",personas[buscar]["fecha_afiliacion"])
                    break 
            else:
                print("No se encontró el rut indicado")
                
        except ValueError:
            print("ocurrio un error al buscar a la persona")
            print ("vuelva a intentar")
            continue
            #Opcion 2 creada por: Nicolás Fernández
            
    elif opcion == 3:

        fecha = date.today()
        valor_certificado = random(1000,1500)
        solicitud = input("Ingrese el rut que desea solicitar el certificado: ")
        
        if solicitud in personas:
            if personas[solicitud]["Sexo"] == "masculino":
                genero = "el señor"
            elif personas[solicitud]["Sexo"] == "femenino":
                genero = "la señorita"
            
            print("*****Certificado de afiliación*****")
            print(f"Con fecha {fecha}\nLa persona {personas[solicitud]["nombre"]} {personas[solicitud]["apellidoPaterno"]}, a la edad de {personas[solicitud]["edad"]}, del Sexo {personas[solicitud]["Sexo"]}, Estado civil {personas[solicitud]["estadoCivil"]}, por un precio de ${valor_certificado} queda asociado a la isapre *Vida y Salud*")
        else:
            print("No se encuentra el rut indicado")
            continue
                
                #Opcion 3 creada por: Benjamín Gutierrez
                
    elif opcion == 4:
        print("\n****************************************************************")
        print("\nGracias por usar el registro de afiliados de Isapre VIDA Y SALUD")
        print("\nIntegrantes: \nNicolás Fernandez \nBenjamín Gutierrez \nJavier Valtierra \nJohans Sepulveda")
        print("\nPython:3.1 \nSoftware: 1.0\n")
        print("*"*64)
        sw=1
        
        #Opcion 4 creada por: Javier Valtierra
  
    

