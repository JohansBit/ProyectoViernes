'''rut tiene que ser formato "texto" en un input solo
   diccionario ejemplo:
   {rut :[nombre,apellidoPaterno,edad,estadoCivil,sexo, fecha_afiliacion]}'''
personas = {"nombre":"nicolas fernandez",
            "rut":"168098405",
            "apellido paterno":"fernandez",
            "edad":37,
            "estado civil":"soltero",
            "genero":"masculino",
            "fecha de afiliacion":30}
try :
     
      buscar = input("ingrese el numero de rut para verificar :\n")
     
      for peronas in personas:
         if personas["rut"] == buscar:
             print("\n---informacion del usuario encontrado---")
             print("")
             print("rut                 : ",personas["rut"])
             print("nombre              : ",personas["nombre"])
             print("edad                : ",personas["edad"])
             print("estado civil        : ",personas["estado civil"])
             print("genero              :",personas["genero"])
             print("fecha de afiliacion : ",personas["fecha de afiliacion"])
             
             break 
         
         else:
            print("debe ingresar una opcion valida ")
except ValueError:
     print("ocurrio un error al buscar a la persona")
     print ("vuelva a intenar")