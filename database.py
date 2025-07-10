from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import mysql.connector

# Configuración de la base de datos, Validar segun sea el caso
DB_USER = "root"
DB_PASSWORD = "Jer123456789"  # Validar contraseña
DB_HOST = "localhost"
DB_PORT = "3306" # Validar puerto
DB_NAME = "calificaciones_db"

# Crear la base de datos en caso de que no exista
def crear_base_de_datos_si_no_existe():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conexion.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conexion.close()
    except mysql.connector.Error as err:
        print(f"Error al intentar crear la base de datos: {err}")
        print("Asegúrate de que el contenedor Docker de MySQL esté corriendo y que la contraseña sea correcta.")

crear_base_de_datos_si_no_existe()

# Modelo de datos
Base = declarative_base()
class Calificacion(Base):
    __tablename__ = 'calificaciones'
    id = Column(Integer, primary_key=True)
    nombre_estudiante = Column(String(100))
    matricula = Column(String(20))
    curso = Column(String(100))
    fecha = Column(Date)
    nota = Column(Float)
    observaciones = Column(Text)

engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
Session = sessionmaker(bind=engine)

def crear_tablas():
    Base.metadata.create_all(engine)