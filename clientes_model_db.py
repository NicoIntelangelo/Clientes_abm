import pymysql
from pymysql.err import Error


def abrir_conexion():
    try:
        conexion = pymysql.connect(host='localhost',user='root',password='1444',db='clientes_db')
        print("Base de datos conectada")
        return conexion 
    
    except (Exception, Error) as error_capturado: 
        print("Ocurrio el error:", error_capturado, "al intentar conectar la base de datos")

def cerrar_conexion (conexion):
    try:
        conexion.close() 
        print("Base de datos desconectada")
    
    except (Exception, Error) as error_capturado: 
        print("Ocurrio el error:", error_capturado, "al intentar desconectar la base de datos") 
         
def buscar_cliente_por_id(id_buscar):
    try: 
        conexion = abrir_conexion() 
        cursor =  conexion.cursor()
       
        query = 'SELECT * FROM clientes WHERE id_c = %s;' 
        #la %s va a ser reemlazada por el segundo valor del .execute()
        #las %s evita el ingreso de datos peligrosos para la data base
        cursor.execute(query, id_buscar) 
        cliente = cursor.fetchone()#debuelve solo la linea donde esta el cursor
        
        return cliente #tupla

    except:
        return False
    
    finally: 
        cerrar_conexion(conexion)

def modificacion_cliente(cliente):
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()
        
        query = 'UPDATE clientes SET nombre_c = %s, apellido_c = %s, \
            cuit_cuil_c = %s, telefono_c = %s\
            WHERE id_c = %s;'
        values = (cliente[1], cliente[2], cliente[3], cliente[4], cliente[0]) ###REMPLAZA ESTOS VALORES EN %S EN ESTE ORDEN
       
        cursor.execute(query, values)
        conexion.commit()#realiza sel cambio si no tenemos el auto commit en nuestra bd
    
        return True
    
    except:
        return False
 
    finally: 
        cerrar_conexion(conexion)

def baja_cliente(id_eliminar):
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()
        
        query = 'DELETE FROM clientes WHERE id_c = %s;'
        cursor.execute(query, id_eliminar)
        conexion.commit()
        
        return True
    
    except:
        return False
    
    finally: 
        cerrar_conexion(conexion)

def alta_cliente(cliente):
    try: 
        conexion = abrir_conexion()
        cursor =  conexion.cursor()
       
        query = 'INSERT INTO clientes (nombre_c, apellido_c, cuit_cuil_c,\
             telefono_c) VALUES (%s, %s, %s, %s);'    
        cursor.execute(query, cliente[1:]) #[1:0] porq el 0 osea el id se genera solo 
        conexion.commit()
       
        query = 'SELECT * FROM clientes WHERE id_c = \
                                (SELECT MAX(id_c) FROM clientes)' #nos devuelve el cliente con id maximo osea el que acabamos de cargar #####
        cursor.execute(query) 
        cliente = cursor.fetchone() 
        
        return cliente    
    
    except:
        return False

    finally: 
        cerrar_conexion(conexion)

def lista_clientes():
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()

        query = 'SELECT * FROM clientes ORDER BY nombre_c'
        cursor.execute(query)
        
        lista_clientes = cursor.fetchall()#devuelve todas las lineas

        return lista_clientes
    
    except:
        return False

    finally: 
        cerrar_conexion(conexion)

def cantidad_de_clientes():
    try:
        conexion = abrir_conexion()
        cursor =  conexion.cursor()

        query = 'SELECT COUNT(id_c) FROM clientes'
        cursor.execute(query)
        
        cantidad = cursor.fetchone()
        
        return cantidad
    
    except:
        return False

    finally: 
        cerrar_conexion(conexion)



#print (alta_cliente([1,"nico", "intelangelo", 2045058693, 3401522221]))

#print (baja_cliente(1))

#print(tabulate(lista_clientes()))
#print (tabulate(lista_clientes(), headers =["ID", "Nombre", "Apellido", "Cuit/Cuil", "Teléfono"]))
#print(buscar_cliente_por_id(4)) # tupla

#cliente = [list(buscar_cliente_por_id(4)),list(buscar_cliente_por_id(5))]
#cliente = [[4, 'nicoo', 'inteelangelo', 1, 21], [5, 'nico', 'intelangelo', 23, 42]]

#print(modificacion_cliente([7, 'aaaa', 'aaaa', 172723, 213423]))
#print(tabulate(cliente))

#print(cantidad_de_cliente())

