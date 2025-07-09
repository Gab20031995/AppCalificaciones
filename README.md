![LOGO ULEAD](https://github.com/user-attachments/assets/6f54a45a-9049-4952-8bd9-ffe2d4983bf3)

# **2025- II Programación Web**
# **Entregable grupal #2**

## Profesor: Alejandro Zamora Esquivel

Alumnos:
- Gabriel Corrales Mora.
- Jeralin Mayerlin Flores Hernández.
- Jean Rabbat Sánchez.


# **📘 Aplicación de Registro de Calificaciones**

Este proyecto es una sencilla aplicación web para el registro y consulta de calificaciones de estudiantes, construida utilizando **Streamlit** para la interfaz de usuario y **SQLAlchemy** con **MySQL** (gestionado a través de Docker) para la persistencia de datos.

## **✨ Características**

* **Registro de Calificaciones:** Permite ingresar nuevas calificaciones con información detallada como nombre del estudiante, matrícula, curso, fecha, nota y observaciones.  
* **Visualización de Calificaciones:** Muestra todas las calificaciones registradas en una tabla interactiva.  
* **Filtrado por Curso:** Permite filtrar los registros por el curso impartido.  
* **Búsqueda por Nombre:** Permite buscar estudiantes por su nombre (parcial o completo).  
* **Base de Datos Persistente:** Utiliza MySQL para almacenar los datos de forma duradera.

## **🛠️ Tecnologías Utilizadas**

* **Python**  
* **Streamlit:** Para la interfaz de usuario web interactiva.  
* **SQLAlchemy:** ORM para interactuar con la base de datos.  
* **mysql-connector-python:** Conector Python para MySQL.  
* **Pandas:** Para la manipulación y visualización de datos en el st.dataframe.  
* **Docker:** Para la gestión y ejecución del servidor MySQL.

## **🚀 Requisitos Previos**

Antes de configurar y ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

* **Python 3.7+**  
* **pip** (gestor de paquetes de Python)  
* **Git**  
* **Docker Desktop** (o Docker Engine en Linux)

## **⚙️ Configuración del Entorno**

Sigue estos pasos para poner en marcha el proyecto en tu máquina local:

### **1\. Clonar el Repositorio**

Abre tu terminal o línea de comandos y clona el proyecto:

`git clone https://github.com/tu-usuario/AppCalificaciones.git` \# Reemplaza con la URL real de tu repo  
cd AppCalificaciones

### **2\. Configurar la Base de Datos con Docker**

Utilizaremos Docker para ejecutar una instancia de MySQL.

\# Para iniciar el contenedor MySQL (asegúrate de que no haya otro MySQL en el puerto 3307\)  
\# Esto crea un contenedor llamado 'local-mysql' que mapea el puerto 3307 de tu host al 3306 del contenedor.  
`docker run \--name local-mysql \-e MYSQL\_ROOT\_PASSWORD=123Queso. \-p 3307:3306 \-d mysql/mysql-server:latest`

**Nota Importante:**

* La contraseña de root para MySQL dentro del contenedor se establece como `123Queso.`. Si quieres cambiarla, asegúrate de actualizarla tanto en el comando docker run como en el archivo database.py.  
* Si el puerto 3307 ya está en uso en tu máquina, cámbialo en el comando Docker (ej. \-p 3308:3306) y luego asegúrate de reflejar ese cambio en database.py.

Puedes verificar que el contenedor está corriendo con:

`docker ps`

Deberías ver local-mysql en la lista con estado Up.

### **3\. Configurar el Entorno Python**

Es altamente recomendable usar un entorno virtual para gestionar las dependencias del proyecto.

\# Crear un entorno virtual  
`python \-m venv venv`

\# Activar el entorno virtual  
\# En Windows:  
`.\\venv\\Scripts\\activate`  
\# En macOS/Linux:  
`source venv/bin/activate`

\# Instalar las dependencias  
`pip install \-r requirements.txt`

### **4\. Configuración del Archivo database.py**

Abre el archivo database.py y asegúrate de que los detalles de conexión coincidan con tu configuración de Docker.

**Verifica que DB\_PORT sea 3307** (o el puerto que hayas mapeado en tu comando docker run si lo cambiaste).

\# database.py  
\# ...  
`DB\_USER \= "root"`  
`DB\_PASSWORD \= "123Queso."`  \# Asegúrate de que coincida con la de tu contenedor Docker  
`DB\_HOST \= "localhost"`  
`DB\_PORT \= "3307"`          \# ¡IMPORTANTE\! Debe coincidir con el mapeo de puerto de Docker  
`DB\_NAME \= "calificaciones\_db"`  
\# ...

El script database.py automáticamente creará la base de datos calificaciones\_db si no existe al iniciar la aplicación.

## **▶️ Cómo Ejecutar la Aplicación**

Con el contenedor Docker de MySQL corriendo y el entorno Python configurado, puedes iniciar la aplicación Streamlit:

streamlit run main.py

Esto abrirá la aplicación en tu navegador web (normalmente en http://localhost:8501).

## **📂 Estructura del Proyecto**

AppCalificaciones/  
├── main.py                 \# Script principal de la aplicación Streamlit  
├── database.py             \# Configuración de la base de datos y modelo ORM  
├── requirements.txt        \# Dependencias de Python del proyecto  
├── .gitignore              \# Archivos y carpetas ignorados por Git  
├── README.md               \# Este archivo  
└── logo.png                \# (Opcional) Imagen utilizada en la UI  
└── venv/                   \# Entorno virtual de Python (ignorado por Git)


