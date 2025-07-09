import streamlit as st
from datetime import date
from database import Calificacion, Session, crear_tablas
from sqlalchemy import select
import pandas as pd

# Crear las tablas si no existen
crear_tablas()

# Titulo del formulario

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.image("images\logo_lead_grande.png", width=600)
st.title("📘 Registro de Calificaciones")
st.write("---")

# Formulario de ingreso de notas
with st.form("registro_formulario"):
    nombre = st.text_input("Nombre del estudiante")
    matricula = st.text_input("Matrícula / ID")
    curso = st.selectbox("Curso", ["Calculo 1", "Programación Web", "Base de datos", "Economía para Ingenieros", "Ética"])
    fecha = st.date_input("Fecha de evaluación", value=date.today())
    nota = st.number_input("Calificación (0 - 100)", min_value=0.0, max_value=100.0, step=0.1)
    observaciones = st.text_area("Observaciones (opcional)")
    submit = st.form_submit_button("Guardar")

    if submit:
        session = Session()
        nueva_calificacion = Calificacion(
            nombre_estudiante=nombre,
            matricula=matricula,
            curso=curso,
            fecha=fecha,
            nota=nota,
            observaciones=observaciones
        )
        session.add(nueva_calificacion)
        session.commit()
        session.close()
        st.success("✅ Registro guardado correctamente.")

st.divider()

# Base de datos
st.subheader("🔍 Calificaciones registradas")
filtro_curso = st.selectbox("Filtrar por curso", ["Todos", "Matemáticas", "Inglés", "Historia", "Ciencias", "Educación Física"])
filtro_nombre = st.text_input("Filtrar por nombre del estudiante")

# Mostrar registros
session = Session()
query = select(Calificacion)

if filtro_curso != "Todos":
    query = query.filter(Calificacion.curso == filtro_curso)

if filtro_nombre:
    query = query.filter(Calificacion.nombre_estudiante.like(f"%{filtro_nombre}%"))

resultados = session.execute(query).scalars().all()
session.close()

df = pd.DataFrame([{
    "Estudiante": r.nombre_estudiante,
    "Matrícula": r.matricula,
    "Curso": r.curso,
    "Fecha": r.fecha,
    "Nota": r.nota,
    "Observaciones": r.observaciones
} for r in resultados])

st.dataframe(df, use_container_width=True)
