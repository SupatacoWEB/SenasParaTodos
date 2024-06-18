from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error
dir(Flask)

app = Flask(__name__)
@app.route('https://supatacoweb.github.io/SenasParaTodos/')
def index():
    return render_template('index.html')

@app.rout('/register', method="post") 
def register():
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    email=request.form['email']
    usuario=request.form['usuario']
    password=request.form['password']   

    conexion = Conexionbasedatos()
    if conexion is not None:
        Insertardatos(conexion, 'nombre', 'apellido', 'email', 'usuario', 'password')
        conexion.close()  
    return "Registro de datos completado con exito" 
        

def Conexionbasedatos():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root12345",
            database="Hello_mysql"
        )
        if conexion.is_connected():
            print("Conexion Establecida")
            return conexion
    except Error as e:
        print("Conexion No Establecida")
        return None

def Insertardatos(conexion, nombre, apellidos, email, usuario, password):
    try:
        cursor = conexion.cursor()
        consulta_sql = """
        INSERT INTO usuarios (nombre, apellidos, email, usuario, password)
        VALUES (%s, %s, %s, %s, %s)
        """
        # Tupla con los datos que queremos insertar
        datos = (nombre, apellidos, email, usuario, password)
        # Ejecutar la consulta SQL con los datos
        cursor.execute(consulta_sql, datos)
        # Confirmar la transacción
        conexion.commit()  
        print("Datos insertados exitosamente")
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            
if __name__ == '__main__':
    app.run(debug=True)
