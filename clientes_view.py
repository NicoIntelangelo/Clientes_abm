import os
import clientes_controler 

################# FUN #################

def screen_clear():
    # para macOS y  linux (os.name es "posix")
    if os.name == "posix":
        _ = os.system("clear")
    # para windows platfrom
    else:
        _ = os.system("cls")

def buscar_cliente_for_id(id_cliente):
    cliente_a_buscar = clientes_controler.cliente(id_cliente, "", "", 0, 0)#crea un cliente pasando el id a buscar como parametro
    cliente_buscado = cliente_a_buscar.obtener_cliente_x_id()
    return cliente_buscado


################# MENU #################

def menu_principal():
    try:
        retorno = 0
        while retorno!= 99 :
            screen_clear()
            print("")
            print("-----------------------------------")
            print("    --- GESTIÓN DE CLIENTES ---")
            print("-----------------------------------")
            print("   ----- Elija una opción -----")
            print("-----------------------------------")
            print("  1 - Buscar cliente con su ID -")
            print("  2 - Cargar nuevo cliente -")
            print("  3 - Mostrar todos los clientes -")
            print("  4 - Mostrar cantidad total de clientes -")
            print(" 99 - Cerrar gestión de clientes -")
            print("-----------------------------------")
            retorno = int(input("Digite la opción y luego presione ENTER: \n"))
        
            if retorno == 1:
                id_cliente_a_buscar = ingresar_id() #abre menu para ingresar num cliente
                cliente_buscado = buscar_cliente_for_id(id_cliente_a_buscar) #busca datos del cliente mediante el num ingresado anteriormente
                if cliente_buscado: #si encuentra al cliente ejecuta
                    mostrar_cliente(cliente_buscado)
                    menu_baja_modificacion(cliente_buscado)
                else:
                    cliente_no_encontrado(id_cliente_a_buscar)
                continue
            
            elif retorno == 2:
                cliente_nuevo = ingresar_datos_cliente("", "nuevo")
                guardar_cliente(cliente_nuevo)
                print("------------------------------")
                input("Presione ENTER para continuar.\n")
                continue
            
            elif retorno == 3: # tabla clientes
                mostrar_tabla_clientes()

            elif retorno == 4:
                cantidad_total_clientes()
            
            elif retorno == 99:
                cerrar_gestion()
                
            elif retorno!=99 : 
               opcion_inexistente()
    except (ValueError) as error_capturado: 
        except_error(error_capturado)
        menu_principal()

def menu_baja_modificacion(cliente_buscado):
    try:
        screen_clear()
        retorno = 0
        while retorno!=99:
            print("-----------------------------------")
            print("  --- MENÚ DE MODIFICACIONES ---  ")
            print("-----------------------------------")
            print("   ----- Elija una opción -----")
            print("-----------------------------------")
            print("     1 - Eliminar Cliente -")
            print("     2 - Modificar Cliente -")
            print("    99 - Volver al inicio -")
            print("-----------------------------------")
            retorno = int(input("Digite la opción y luego presione ENTER: \n"))
            
            if retorno == 1:
                eliminar_cliente(cliente_buscado)
                print("------------------------------")
                input("Presione ENTER para continuar.\n")
                #input("Presione ENTER para continuar.\n")
                break
            elif retorno == 2:
                cliente_modificado = ingresar_datos_cliente(cliente_buscado, "modif")
                modificar_cliente(cliente_modificado)
                print("------------------------------")
                input("Presione ENTER para continuar.\n")
                break
            
            elif retorno!=99: 
                opcion_inexistente()
    
    except (ValueError) as error_capturado: 
        except_error(error_capturado)
        menu_principal()


################# MUESTRA DATOS #################       

def mostrar_cliente(cliente):
    screen_clear()
    print("")
    print("Datos del Cliente:")
    print("-----------------")
    print("ID: {}".format(cliente.id_c))
    print("--------------------------------------------------------")
    print("Nombre: {}".format(cliente.nombre_c))
    print("--------------------------------------------------------")
    print("Apellido: {}".format(cliente.apellido_c))
    print("--------------------------------------------------------")
    print("Cuit/Cuit: {}".format(cliente.cuit_cuil_c))
    print("--------------------------------------------------------")
    print("teléfono:  {}".format(cliente.telefono_c))
    print("--------------------------------------------------------")
    input("Presione ENTER para ir al menú de modificaciones.\n")

def mostrar_tabla_clientes():
    screen_clear()
    print("--------------------- LISTA DE CLIENTES ---------------------")
    print("-------------------------------------------------------------")
    print (clientes_controler.tabla_de_clientes())
    print("")
    print("-------------------------------------------------------------")
    input("Presione ENTER para volver al inicio.\n")

def cantidad_total_clientes():
    screen_clear()
    print("      Total de clientes actuales      ")
    print("--------------------------------------")
    print(clientes_controler.cantidad_de_clientes_c())
    print("↑↑ Clientes")
    print("--------------------------------------")
    input("Presione ENTER para volver al inicio.\n")


################# INGRESOS ################# 

def ingresar_datos_cliente(cliente, tipo_ingreso):
    try:
        screen_clear()
        ## if para titulo del menu
        if tipo_ingreso == "nuevo":
            titulo = "Ingrese los datos del nuevo Cliente (sin simbolos) "
        elif tipo_ingreso == "modif":
            titulo = "Ingrese los datos a modificar del clienete: {} (datos sin cambios presione ENTER)".format(cliente.id_c)
        
        #MENU
        print("")
        print("---------------------------------------------------------")
        print(titulo)
        print("--------------------------------------------------------")
        val_Apellido = str(input("Apellido: ").lower())
        print("--------------------------------------------------------")
        val_Nombre = str(input("Nombre: ").lower())
        print("--------------------------------------------------------")
        val_cuit_cuil = input("cuit/cuil: ")
        if tipo_ingreso == "nuevo" and clientes_controler.validar_cuit(val_cuit_cuil) == False:
           val_cuit_cuil = validacion_cuit(tipo_ingreso)
        if tipo_ingreso == "modif" and val_cuit_cuil != "":
            val_cuit_cuil = validacion_cuit(tipo_ingreso)
        print("--------------------------------------------------------")
        val_telefono = input("Teléfono: ")
        if tipo_ingreso == "nuevo" and clientes_controler.validar_int(val_telefono) == False:
           val_telefono = validacion_int(val_telefono, tipo_ingreso)
        if tipo_ingreso == "modif" and val_telefono != "":
            val_telefono = validacion_int (val_telefono,tipo_ingreso)
        print("--------------------------------------------------------")
        print("")
        input("Presione ENTER para cargar.\n")
        
        #nuevo cliente
        if tipo_ingreso == "nuevo":
            cliente_ingresado = clientes_controler.cliente(1, val_Nombre, val_Apellido, 
                                        val_cuit_cuil, val_telefono)
        
        #modificacion cliente
        elif tipo_ingreso == "modif":
            if val_Apellido == "":
                val_Apellido = cliente.apellido_c
            if val_Nombre == "":
                val_Nombre = cliente.nombre_c
            if val_cuit_cuil == "":
                val_cuit_cuil = cliente.cuit_cuil_c
            if val_telefono == "":
                val_telefono = cliente.telefono_c
            
            cliente_ingresado = clientes_controler.cliente(cliente.id_c, val_Nombre, 
                        val_Apellido, val_cuit_cuil, val_telefono)
        
        return cliente_ingresado
    except (ValueError) as error_capturado: 
        except_error(error_capturado)
        menu_principal()

def ingresar_id(): 
    try:
        screen_clear()
        print("")
        print("--------------------------------------")
        print("--- Ingresar número de ID a buscar ---")
        print("--------------------------------------")
        id_buscado = int(input("ID: "))
        print("--------------------------------------")
        input ("Presione ENTER para buscar.\n")
        return id_buscado
    except (ValueError) as error_capturado: 
        except_error(error_capturado)
        menu_principal()


################# MENSAJES #################

def cliente_no_encontrado (ID):
    screen_clear()
    print("Búsqueda sin resultados.") 
    print("-----------------------------------")
    print("El ID de cliente", ID, "no existe.")
    print("-----------------------------------")
    input("Presione ENTER para volver al inicio.\n") 

def opcion_inexistente():
    screen_clear()
    print("  *** La opcion ingresada no existe ***")
    input("  Presione ENTER para volver a intentar\n")

def cerrar_gestion():
    screen_clear()
    print("--------------------------------")
    print(" Gestion de clientes finalizada ")
    print("--------------------------------")

def guardar_cliente(cliente_nuevo):
    screen_clear()
    cliente_guardado = cliente_nuevo.guardar_cliente() #trabaja sobre un objeto de class cliente
    if cliente_guardado:
        print("Cliente " + cliente_guardado.apellido_c + ', ' + 
                cliente_guardado.nombre_c + " (ID de cliente: "+ 
                str(cliente_guardado.id_c) + ") ha sido guardado/a exitosamente")
        
    else: 
        print("Cliente ID: "+ str(cliente_nuevo.id_c)) + " no pudo ser guardado/a"
        print("Intente nuevamente")

def eliminar_cliente(cliente_baja):
    screen_clear()
    if cliente_baja.eliminar_cliente():
        print("Cliente " + cliente_baja.apellido_c+ ', ' + 
                cliente_baja.nombre_c + " (ID de cliente: " + 
                str(cliente_baja.id_c) + ") ha sido eliminado/a exitosamente")
        
    else: 
        print("Cliente ID: "+ str(cliente_baja.id_c)) + " no pudo ser elimimado/a"
        print("Intente nuevamente")

def modificar_cliente(cliente_modificado):
    screen_clear()
    if cliente_modificado.modificar_cliente():
        print("Cliente " + cliente_modificado.apellido_c + ', ' + 
                cliente_modificado.nombre_c + " (ID de cliente: " + 
                str(cliente_modificado.id_c) + ") ha sido modficado/a exitosamente")
        
    else: 
        print("Cliente ID: "+ str(cliente_modificado.id_c) + " no pudo ser modificado/a")
        print("Intente nuevamente")


################# VALIDACIONES #################

def validacion_int(numero,tipo_ingreso):
    if tipo_ingreso == "nuevo":
        while clientes_controler.validar_int(numero) == False:
            screen_clear()
            print("   ############### ATENCIÓN ###############   ")
            print("     El dato ingresado debe ser 'Numerico'    ")
            print("----------------------------------------------")
            print("*Para volver al menu pricipal ingresar 000  ")
            print("")
            numero = input("Teléfono: ")
            
            if numero == "000":
                exit(menu_principal()) #sale al menu pricipal
            
            elif clientes_controler.validar_int(numero) == False: 
                continue
            
            return numero
    
    elif tipo_ingreso == "modif":
        while clientes_controler.validar_int(numero) == False and numero != "": #para poder modificar ya que puede quedar libre
            screen_clear()
            print("   ############### ATENCIÓN ###############   ")
            print("     El dato ingresado debe ser 'Numerico'    ")
            print("----------------------------------------------")
            print("*Para volver al menu pricipal ingresar 000  ")
            print("")
            numero = input("Teléfono: ")
            
            if numero == "000":
                exit(menu_principal()) #sale al menu pricipal
            
            elif clientes_controler.validar_int(numero) == False: 
                continue
            
            return numero

def validacion_cuit (tipo_ingreso):
    if tipo_ingreso == "nuevo":
        cuit = "0"
        
        while clientes_controler.validar_cuit(cuit) == False: #el !="" sirve para cuando se esta modificando
            screen_clear()
            print("   ############### ATENCIÓN ###############   ")
            print("El cuit/cuil es invalido, vuelve a ingresarlo.")
            print("----------------------------------------------")
            print("*Para volver al menu pricipal ingresar 000  ")
            print("")
            cuit = str(input("cuit/cuil: "))
            
            if cuit == "000":
                exit(menu_principal())#sale al menu pricipal
            
            elif clientes_controler.validar_cuit(cuit) == False: 
                continue
            return cuit
    
    elif tipo_ingreso == "modif":
        cuit = "0"
        
        while clientes_controler.validar_cuit(cuit) == False and cuit != "": #el !="" sirve para cuando se esta modificando
            screen_clear()
            print("   ############### ATENCIÓN ###############   ")
            print("El cuit/cuil es invalido, vuelve a ingresarlo.")
            print("----------------------------------------------")
            print("*Para volver al menu pricipal ingresar 000  ")
            print("")
            cuit = str(input("cuit/cuil: "))
            
            if cuit == "000":
                exit(menu_principal())#sale al menu pricipal
            
            elif clientes_controler.validar_cuit(cuit) == False: 
                continue
           
            return cuit


################# EXEPT ################# 

def except_error(error_capturado):
    screen_clear()
    print("----------------------------------------------------")
    print("Ocurrió el error:(", error_capturado, ")")
    print("----------------------------------------------------")
    input("Presione ENTER para volver a intentar.\n")





############################## EJECUCIÓN ##############################


menu_principal() 