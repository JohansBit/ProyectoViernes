
try :
     
      buscar = input("ingrese el numero de rut para verificar :\n")
      if buscar in personas:
             print("\n---informacion del usuario encontrado---")
             print("")
             print("rut                 :",personas[rut])
             print("nombre              :",personas["Nombre"])
             print("edad                :",personas["edad"])
             print("estado civil        :",personas["estadoCivil"])
             print("genero              :",personas["sexo"])
             print("fecha de afiliacion :",personas["fecha_afiliacion"]) 
      else:
         print("debe ingresar una opcion valida ")
except ValueError:
     print("ocurrio un error al buscar a la persona")
     print ("vuelva a intentar")
