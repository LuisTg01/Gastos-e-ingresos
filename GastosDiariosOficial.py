# Escribe tu código aquí :-)
## importar modulos
import time
from io import open
#########################CREADNO UN ARCHIVO EXTERNO

archivo_texto = open("registros.txt","w")
frase ="<<<<<< REGISTROS DE INGRESOS Y GASTOS >>>>>>>>\n"
archivo_texto.write(frase)
archivo_texto.close()

#DICIONARIO DE MESES
MESES = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}

#datos principales de entrada
registros = []

ingresos_gastos = [[".",".",".",".",".","."]]

#FUNCIONES
#########################
########FUNCION AGREGAR A REGISTRO
def agregandoaregistro(objeto):
    archivo_texto = open("registros.txt","a")
    archivo_texto.write(f"\n{objeto}")
    archivo_texto.close()

################ FUNCIONES PARA EXTARER INRESOS Y GASTOS
######EXTRAER SOLO INGRESOS
def ExtraerIngresos(ingresosGastos):# retorna ingresos mensuales
    ingresos = []
    anios = []

    for anio in range(len(ingresosGastos)):
        if anios == []:
            anios.append(ingresosGastos[anio][0])
        elif anios[-1]  != ingresosGastos[anio][0]:
            anios.append(ingresosGastos[anio][0])

    for anio in anios:
        for mes in MESES.values():
            ingreso = 0
            for  i in range(len(ingresosGastos)):

                if mes == ingresosGastos[i][1] and anio == ingresosGastos[i][0] and ingresosGastos[i][4] == "ingreso":
                    ingreso += float(ingresosGastos[i][3])
            if ingreso > 0:
                ingresos.append([anio, mes, ingreso])

    return ingresos


###################### EXTRAER SOLO GASTOS

def ExtraerGastos(ingresosGastos): # retorna gastos mensuales
    gastos = []
    anios = []

    for anio in range(len(ingresosGastos)):
        if anios == []:
            anios.append(ingresosGastos[anio][0])
        elif anios[-1]  != ingresosGastos[anio][0]:
            anios.append(ingresosGastos[anio][0])

    for anio in anios:
        for mes in MESES.values():
            gasto = 0
            for  i in range(len(ingresosGastos)):
                if mes == ingresosGastos[i][1] and anio == ingresosGastos[i][0] and ingresosGastos[i][4] == "gasto":
                    gasto += float(ingresosGastos[i][3])
            if gasto > 0:
                gastos.append([anio, mes, gasto])

    return gastos

######################### FUNCIONES PARA AÑADIR A REGISTRO DE LOS INGRESOS
def AgregarRegistro(gastoMensual, ingresoMensual):
    global registros
    for i in range(len(ingresoMensual)):
        existe = False
        for reg in range(len(registros)):
            if ingresoMensual[i][0] == registros[reg][1] and ingresoMensual[i][1] == registros[reg][0]:
                registros[reg][2] = ingresoMensual[i][2]
                existe = True
                break
        if not existe:
            nuevoIngresoM = [ingresoMensual[i][1],ingresoMensual[i][0],ingresoMensual[i][2], 0, ingresoMensual[i][2]]
            registros.append(nuevoIngresoM)

    for i in range(len(gastoMensual)):
        for reg in range(len(registros)):
            if gastoMensual[i][0] == registros[reg][1] and gastoMensual[i][1] == registros[reg][0]:
                registros[reg][3] = gastoMensual[i][2]
                registros[reg][4] = float(registros[reg][2]) - float(registros[reg][3])
                break






def BalanceMensual(reg):
    global balance
    saldo_anterior = 0
    for i in range(len(reg)-1):
        saldo_anterior += float(reg[i][4])

    ingreso = reg[-1][2]
    gasto = reg[-1][3]

    saldo_actual = (saldo_anterior + ingreso) - gasto

    balance = [ingreso, saldo_anterior, gasto, saldo_actual]


balance = [0, 0, 0, 0]


while True:
    print("")
    print("                        ===================================")
    print("                        |          Bienvenido a:          |")
    print("                        |   PROGRAMA DE GASTOS DIARIOS    |")
    print("                        ===================================\n")
    print("<<<<<<<Cuida los pequeños gastos, recuerda que un pequeño agujero unde a un barco>>>>>>>>>>")
    print("")
    print("--------------------------------------------------------------------------------------------")
    print("Inciando programa . . .\n")
    print("                         _________________________________")
    print("                          Balance mensual + saldo aterior")
    if len(registros) == 0:
        print(f"                             {time.asctime()[4:7]}, {time.localtime()[0]}                    ")
    else:
        print(f"                             {registros[-1][0]}, {registros[-1][1]}                  ")
    print(f"                                  Ingreso:   S/.{balance[0]:.2f}      ")
    print(f"                           Saldo anterior:   S/.{balance[1]:.2f}      ")
    print(f"                                    Gasto:   S/.{balance[2]:.2f}      ")
    print("                          |-------------------------------|")
    print(f"                              Saldo actual:   S/.{balance[3]:.2f}     ")
    print("                          |-------------------------------|\n")
    if len(ingresos_gastos) == 1:
            print("")
    else:
        print(f"  Ultimo Registro:       {ingresos_gastos[-1][2]} \ {ingresos_gastos[-1][3]} \ {ingresos_gastos[-1][4]} \ {ingresos_gastos[-1][5]}\n")
    print("<<<<<<<<<<<<")
    print("| OPCIONES |")
    print(">>>>>>>>>>>>\n")
    print("[A] Agregar Ingresos")
    print("[B] Agregar Gastos")
    print("[C] Ver Ingresos")
    print("[D] Ver Gastos")
    print("[E] Calculadora")
    print("[F] SALIR")
    Opcion = input("Escribe una opción: ").lower()

###########################################INGRESOS
    if Opcion == "a":
        print()
        CATEGORIAS = ["PRÉSTAMO", "SUELDO", "VENTAS", "OTROS"]
        datos = ["año", "mes", "día", "monto", "tipo", "categoria"]
        nuevo = []
        for dato in datos:
            if dato == "tipo": #si el dato es tipo solo continua con otra iteracion
                nuevo.append("ingreso")
                pass
            elif dato == "mes" or dato == "año" or dato == "día" :
                if dato == "mes":
                    nuevo.append(time.asctime()[4:7])
                elif dato == "año":
                    nuevo.append(str(time.localtime()[0]))
                else:
                    nuevo.append(str(time.localtime()[2]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[0]))
                pass

            elif dato == "categoria":
                print("Elige el numero de la opcion a la que pertenece tu ingreso.")
                print("\nCATEGORIAS:\n")
                for categoria in CATEGORIAS: ## recorre la lista CATEGORIAS e imprime opciones para cada una
                    print(f"[{CATEGORIAS.index(categoria) + 1}] {categoria}")
                while True:
                    try:
                        registro = int(input(f"Elija una {dato}: "))
                        registro -= 1
                        nuevo.append(CATEGORIAS[registro])
                        break
                    except ValueError:
                        print("\n<< ingrese una opcion valida >>\n")
                    except IndexError:
                        print("\n<< ingrese una opcion valida >>\n")
            elif  dato == "monto": # si el dato es ano, dia o monto ingresa en la varable registro
                while True:
                    try:
                        registro = float(input(f"ingresar {dato}: "))
                        nuevo.append(registro)
                        break
                    except ValueError:
                        print("\n<<Ingrese un monto valido!>>\n")

        agregandoaregistro(nuevo)
        ingresos_gastos.append(nuevo)
        gast = ExtraerGastos(ingresos_gastos)
        ingr = ExtraerIngresos(ingresos_gastos)
        AgregarRegistro(gast, ingr )
        BalanceMensual(registros)

###########################Gastos

    if Opcion == "b":
        if len(ingresos_gastos) == 1:
            print("\n<<<Imposible registrar gastos, no tiene saldo >>>\n ")

        elif len(ingresos_gastos) != 1:

            print()
            CATEGORIAS  = ["Bebidas", "Comida", "Diversión", "Educación", "Gasolina", "Hotel", "Transporte", "Personales","Salud","Ropa","Mascota","Propinas","Otros"]
            datos       = ["año", "mes", "día", "monto", "tipo", "categoria"]
            nuevo  = []
            for dato in datos:
                if dato == "tipo":
                    nuevo.append("gasto")
                    pass

                elif  dato == "monto": # si el dato es ano, dia o monto ingresa en la varable registro
                    while True:
                        try:
                            registro = float(input(f"ingresar {dato}: "))
                            nuevo.append(registro)
                            break
                        except ValueError:
                            print("\n<<Ingrese un monto valido!>>\n")

                elif dato == "mes" or dato == "año" or dato == "día":
                    if dato == "mes":
                        nuevo.append(time.asctime()[4:7])
                    elif dato == "año":
                        nuevo.append(str(time.localtime()[0]))
                    else:
                        nuevo.append(str(time.localtime()[2]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[0]))
                    pass

                elif dato == "categoria":
                    print("Elige el numero de la opcion a la que pertenece tu ingreso.")
                    print("\nCATEGORIAS:\n")
                    for categoria in CATEGORIAS: ## recorre la lista CATEGORIAS e imprime opciones para cada una
                        print(f"[{CATEGORIAS.index(categoria) + 1}] {categoria}")
                    while True:
                        try:
                            registro = int(input(f"ingresar {dato}: "))
                            registro -= 1
                            nuevo.append(CATEGORIAS[registro])
                            break
                        except ValueError:
                            print("\n<< ingrese una opcion valida >>\n")
                        except IndexError:
                            print("\n<< ingrese una opcion valida >>\n")

            agregandoaregistro(nuevo)
            ingresos_gastos.append(nuevo)
            gast = ExtraerGastos(ingresos_gastos)
            ingr = ExtraerIngresos(ingresos_gastos)
            AgregarRegistro(gast, ingr )
            BalanceMensual(registros)

############################################### VER INGRESOS
    if Opcion == "c":
        ingr = ExtraerIngresos(ingresos_gastos)
        print(ingr)
############################################## VER GASTOS
    if Opcion == "d":
        gast = ExtraerGastos(ingresos_gastos)
        print(gast)



###############################################CALCUADORA SIMPLE##################################################
    if Opcion== "e":
        while True:
            menu = """
            Calculadora de opraciones Principales
            <<<<<<<<<< ELIJA UNA OPCION >>>>>>>>>>
            A) Suma
            B) Resta
            C) Multiplicacion
            D) Division
            E) saiir
            """
            print(menu)
            ValorTeclado = input(">>> Opcion > ").lower()
            if ValorTeclado == "a":
                seguir = " "
                AcomuladorSuma = 0
                while seguir == " ":
                    Suma = float(input("Ingrese valor: "))
                    AcomuladorSuma += Suma
                    seguir = input("Desea continuar ( /no): ").lower()
                    print(f"\n << La suma es: {AcomuladorSuma} >>\n")
                    if seguir == "no":
                        break

            if ValorTeclado == "b":
                seguir = " "
                AcomuladorResta = 0
                print("Digite solo el primer numero con un signo negativo")
                while seguir == " ":

                    Resta = float(input("Ingrese valores: "))
                    AcomuladorResta -= Resta

                    seguir = input("Desea continuar ( /no): ").lower()
                    print(f"\n << La resta es: {AcomuladorResta} >>\n")
                    if seguir == "no":
                        break

            if ValorTeclado == "c":
                seguir = " "
                AcomuladorMultiplicacion = 1
                while seguir == " ":
                    Multiplicacion = float(input("Ingrese valores: "))
                    AcomuladorMultiplicacion *= Multiplicacion
                    seguir = input("Desea continuar ( /no): ").lower()
                    print(f"\n << La multiplicacion  es: {AcomuladorMultiplicacion} \n>>")
                    if seguir == "no":
                        break

            if ValorTeclado == "d":
                print("Capacidad de divir de solo dos numeros \n")
                N1 = float(input("Ingrese primer numero: "))
                N2 = float(input("Ingrese segundo numero: "))
                print(f"\n<<el resultdo de la division es: {N1/N2}>>\n")

    if Opcion== "f":
        print("<<<<<EL PROOGRAMA AH FINALIZADO>>>>>>>")
        break

