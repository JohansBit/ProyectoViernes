


if opcion == 3:

    fecha = date.today()
    valor_certificado = random.randint(1000,1500)

    if sexo == "masculino":
        genero = "el señor"
    elif sexo == "femenino":
        genero = "la señorita"

    solicitud = input("Ingrese el rut que desea solicitar el certificado: ")

    if solicitud in personas:
      print("*****Certificado de afiliación*****")
      print(f"Con fecha {fecha}, la persona " ,personas[solicitud]["nombre"] ,personas[solicitud]["apellidoPaterno"] ,", a la edad de ",personas[solicitud]["edad"]," / "personas[solicitud]["esatdoCivil"], ", a la edad de ",personas[solicitud]["edad"]" por un precio de ${valor_certificado} queda asociado a la isapre *Vida y Salud*")
    else:
      print("No se encuentra el rut indicado")


      
