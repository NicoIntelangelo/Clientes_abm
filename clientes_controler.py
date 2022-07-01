import clientes_model_db 
from tabulate import tabulate

def validar_cuit (cuit: str) -> bool:
        
    if len(cuit)!= 11 and len(cuit)!= 12 :
        return False

    intcuit = [int(i) for i in cuit]
    
    validacion = [5,4,3,2,7,6,5,4,3,2,1]

    for i in range (len(intcuit)):
        intcuit [i] = intcuit [i]* validacion [i]

    resultado = sum(intcuit)

    if resultado % 11 == 0:
        return True #("El CUIL/CUIT:", cuit, " es valido ")
    else:
        return False#("El CUIL/CUIT:", cuit, "es incorrecto")


def validar_int(numero):
    try:
        int(numero)
        return True

    except ValueError:
        return False

def cantidad_de_clientes_c():
    cantidad_c = clientes_model_db.cantidad_de_clientes()[0]
    return cantidad_c

def tabla_de_clientes ():
    lista = clientes_model_db.lista_clientes()
    lista_tabulada = tabulate(lista, headers =["ID ", "  Nombre" , "  Apellido" , "Cuit/Cuil  " , "Teléfono  " ])
    return lista_tabulada

class cliente:
    
    def __init__(self, id_c, nombre_c, apellido_c, cuit_cuil_c, 
                    telefono_c):
        self.id_c = int(id_c)
        self.apellido_c = apellido_c
        self.nombre_c = nombre_c
        self.cuit_cuil_c = cuit_cuil_c
        self.telefono_c = int(telefono_c)
        
    def obtener_cliente_x_id(self):
        
        cliente_encontrado = clientes_model_db.buscar_cliente_por_id(self.id_c)
        
        if cliente_encontrado:
            cliente_devuelto = cliente(cliente_encontrado[0], cliente_encontrado[1], 
                                    cliente_encontrado[2], cliente_encontrado[3], 
                                    cliente_encontrado[4]) #instanciamos un cliente
    
            return cliente_devuelto 
        else:
            # si no se encuentra el cliente buscado el modelo habrá devuelto un
            # FALSE y eso es lo que devolvemos
            return cliente_encontrado

    def guardar_cliente(self):
        
        cliente_nuevo = clientes_model_db.alta_cliente((self.id_c, self.nombre_c, 
                                        self.apellido_c, self.cuit_cuil_c, 
                                        self.telefono_c))
        # con los elementos de la tupla recibida, creamos un OBJETO c
        cliente_guardado = cliente(cliente_nuevo[0], cliente_nuevo[1], cliente_nuevo[2], cliente_nuevo[3], cliente_nuevo[4])
        return cliente_guardado

    def eliminar_cliente(self):
        return clientes_model_db.baja_cliente(self.id_c)

    def modificar_cliente(self):
        cliente_modificado = (self.id_c, self.nombre_c, self.apellido_c, self.cuit_cuil_c, 
                                        self.telefono_c)
        return clientes_model_db.modificacion_cliente(cliente_modificado) 



#print (validar_cuit("3094876"))
