import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Mapping Demo", page_icon="🌍")


# Título y subtítulo
st.title("Proyecto Integrador: [Nombre del Proyecto]")
st.subheader("Un Viaje Creativo con [Nombre del Equipo]")

# Imagen de fondo
image = Image.open("./static/proyecto integrador.png") 
st.image(image, width=700, use_column_width=True)  

# Integrantes
st.header("Nuestro Equipo")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[Juan Carlos Garcia]**")
    st.write("[Colaborador]")

with col2:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[Juan Camilo Hernandez]**")
    st.write("[Colaborador]")
    
with col3:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[Duvan Sanchez]**")
    st.write("[Colaborador]")
    
with col4:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[Dayana Castro Villa]**")
    st.write("[Colaboradora]")
    
with col5:
    st.image("./static/user.png", width=200)  # Reemplaza con la ruta de la foto
    st.write("**[Bibiana Machado]**")
    st.write("[Colaboradora]")

# Descripción del proyecto
st.header("Sobre el Proyecto")
st.write("""
[Escribe aquí una breve descripción del proyecto, incluyendo el objetivo principal, la problemática que aborda y el enfoque que se utiliza. Puedes ser creativo y usar un lenguaje atractivo.]
""")

# Más información
st.header("Más Información")

# Puedes añadir secciones como:
# - Tecnología utilizada
# - Resultados esperados
# - Presentación de resultados (fecha y formato)
# - Contacto para preguntas

st.write("""
[Agrega la información adicional que consideres relevante.]
""")

# Footer con links
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://www.google.com">Google</a> |
        <a href="https://www.facebook.com">Facebook</a> |
        <a href="https://www.linkedin.com">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)