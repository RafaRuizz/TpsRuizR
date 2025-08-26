fecha = input("Ingrese fecha como 'dia, DD/MM': ")  # Ya es str, no hace falta convertir

fecha2 = fecha.split(",")
dia = fecha2[0].strip()  # Eliminar espacios extra
dym = fecha2[1].strip()

# Separar día y mes
dym1 = dym.split("/")
day = int(dym1[0])  # Convertir a entero para comparar
mes = int(dym1[1])  # Convertir a entero para comparar
dia = dia.lower()

if day <= 31 and mes <= 12:
    if dia == "lunes" or dia == "martes" or dia == "miercoles":
        rta = input("Se tomaron examenes?: ")
        rta = rta.lower()
        if rta == "si":
            aprobados = int(input("Ingrese cantidad de aprobados: "))
            desaprobados = int(input("Ingrese desaprobados: "))
            porcentajeaprob = aprobados / (aprobados + desaprobados) * 100
            print("Porcentaje de aprobados: ", porcentajeaprob, "%")
    elif dia == "jueves":
        porcentaje = float(input("Ingrese porcentaje de asistencia: "))
        if porcentaje > 50.0:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
    elif dia == "viernes":
        if day == 1 and (mes == 1 or mes == 7):
            print("Comienzo del nuevo ciclo")
            alumnosnc = float(input("Ingrese cantidad de alumnos del nuevo ciclo: "))
            arancelalum = float(input("Ingrese arancel x alumno: $"))
            ingresotot = alumnosnc * arancelalum
            print("Ingreso total = $", ingresotot)
else:
    print("Dia no valido")