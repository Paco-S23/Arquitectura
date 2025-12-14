import streamlit as st
import os
import base64
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Departamentos 33.10",
    page_icon="🏢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
<style>
    /* Fondo y Colores Generales */
    .stApp, div[data-testid="stAppViewContainer"] {
        background-color: #f8f9fa !important;
        color: #212529 !important;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Tipografía */
    h1 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
        color: #111827 !important; 
        font-weight: 800; 
        text-transform: uppercase;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    h2, h3 {color: #343a40 !important;}
    p {color: #495057 !important;}
    
    /* Etiqueta de Precio */
    .price-tag {
        background-color: #212529;
        color: #ffffff;
        padding: 12px 30px;
        font-size: 1.4rem;
        font-weight: 700;
        border-radius: 50px;
        display: inline-block;
        margin: 20px 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }

    /* Botones */
    .stButton>button {
        width: 100%;
        background-color: #111827;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #333;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    hr { border-color: #dee2e6; margin: 40px 0; }
</style>
""", unsafe_allow_html=True)

# --- FUNCIONES DE UTILIDAD ---
def get_valid_path(filename):
    """Busca la imagen en local o en la carpeta Stream intentando varias combinaciones."""
    # Lista de posibles rutas y variaciones de nombre
    nombres_a_probar = [filename, filename.capitalize(), filename.lower()]
    
    base_dirs = [
        "", # Directorio actual
        "Stream/", # Carpeta Stream
        "stream/", # Carpeta stream (minúscula)
        os.path.dirname(__file__),
        os.path.join(os.path.dirname(__file__), "Stream")
    ]

    for base in base_dirs:
        for nombre in nombres_a_probar:
            ruta_completa = os.path.join(base, nombre)
            if os.path.exists(ruta_completa):
                return ruta_completa
    return None

def load_image_for_st(filename, fallback_text="IMAGEN"):
    path = get_valid_path(filename)
    if path:
        return path
    return f"https://placehold.co/800x500/e9ecef/6c757d/png?text={fallback_text}"

def get_base64_image(filename):
    path = get_valid_path(filename)
    if path:
        with open(path, "rb") as img_file:
            return f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode()}"
    return "https://placehold.co/800x500/e9ecef/6c757d/png?text=Cargando..."

# --- ENCABEZADO ---
st.title("Departamentos 33.10")
st.markdown("<div style='text-align: center; color: #6c757d; margin-bottom: 20px; font-weight: 500;'>33 Oriente #10, Puebla, Pue.</div>", unsafe_allow_html=True)

# Imagen Principal (RESTAURADA a la original que subiste al principio)
hero_image = load_image_for_st("imagen_2025-12-07_200507713.png", "FACHADA PRINCIPAL") 
col_L, col_C, col_R = st.columns([0.2, 4, 0.2])
with col_C:
    st.image(hero_image, use_container_width=True)

st.markdown('<div style="text-align: center;"><div class="price-tag">Desde $2,940,000.00</div></div>', unsafe_allow_html=True)

st.write("---")

# --- UBICACIÓN ---
# Mapa original
map_path = load_image_for_st("imagen_2025-12-07_202017772.png", "MAPA UBICACION")
st.image(map_path, use_container_width=True)

link_maps = "https://www.google.com/maps/search/?api=1&query=33+Oriente+10+Puebla+Pue"
st.markdown(f"""
    <div style="text-align: center; margin-top: 15px;">
        <a href="{link_maps}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #0d6efd; color: white; border: none; padding: 10px 25px; border-radius: 50px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                📍 Ver en Google Maps
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns(3)
col1.metric("Medicina BUAP", "5 min")
col2.metric("Plaza Dorada", "3 min")
col3.metric("Centro Histórico", "10 min")

st.write("---")

# --- MODELOS ---
st.subheader("📐 Modelos Disponibles")
tab_a, tab_b = st.tabs(["Torre A (89m²)", "Torre B (96m²)"])

with tab_a:
    st.markdown("##### 🏢 Modelo A")
    # Imagen de plano original (RESTAURADA)
    img_modelo_a = load_image_for_st("imagen_2025-12-12_171537244.png", "PLANO TORRE A")
    st.image(img_modelo_a, use_container_width=True)
    c1, c2 = st.columns(2)
    c1.markdown("- 89 m²\n- 2 Recámaras\n- 2 Baños")
    c2.markdown("- Terraza\n- 2 Cajones\n- Paneles Solares")

with tab_b:
    st.markdown("##### 🏢 Modelo B")
    # Imagen de plano original (RESTAURADA)
    img_modelo_b = load_image_for_st("imagen_2025-12-12_170832401.png", "PLANO TORRE B")
    st.image(img_modelo_b, use_container_width=True)
    c1, c2 = st.columns(2)
    c1.markdown("- 96 m²\n- 2 Recámaras\n- 2 Baños")
    c2.markdown("- **Opción 3ª Recámara**\n- 2 Cajones\n- Bodega")

st.write("---")

# --- GALERÍA CARRUSEL (AUTOMÁTICA) ---
st.subheader("📸 Galería del Proyecto")
st.write("Descubre cada detalle de tu próximo hogar.")

# LISTA DE IMÁGENES EXACTA (Nombres originales que subiste)
carousel_data = [
    {"file": "foto11.jpg", "caption": "Fachada Principal con Áreas Verdes"},
    {"file": "Foto1.jpg", "caption": "Cocina Integral Equipada"},
    {"file": "Foto2.jpg", "caption": "Vistas Exteriores y Cielo Azul"},
    {"file": "Foto3.jpg", "caption": "Patios Interiores y Ventilación"},
    {"file": "Foto4.jpg", "caption": "Arquitectura Moderna"},
    {"file": "foto5.jpg", "caption": "Habitaciones Amplias e Iluminadas"},
    {"file": "foto6.jpg", "caption": "Espacios de Sala-Comedor"},
    {"file": "foto7.jpg", "caption": "Área de Servicio"},
    {"file": "foto8.jpg", "caption": "Estacionamiento y Jardineras de Bambú"},
    {"file": "foto9.jpg", "caption": "Detalles de Fachada Lateral"},
    {"file": "foto10.jpg", "caption": "Estructura Sólida y Diseño Urbano"}
]

# Generar HTML de Slides
slides_markup = ""
for item in carousel_data:
    b64 = get_base64_image(item["file"])
    slides_markup += f"""
    <div class="mySlides fade">
        <img src="{b64}" style="width:100%">
        <div class="text">{item["caption"]}</div>
    </div>
    """

# Componente HTML/JS Completo
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {{box-sizing: border-box;}}
body {{font-family: sans-serif; margin: 0;}}
.mySlides {{display: none;}}
img {{vertical-align: middle; width: 100%; height: 450px; object-fit: cover; border-radius: 12px;}}

/* Contenedor */
.slideshow-container {{
  max-width: 100%;
  position: relative;
  margin: auto;
}}

/* Botones Next/Prev - Transparentes sobre la imagen */
.prev, .next {{
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 24px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
  background-color: rgba(0,0,0,0.1); /* Muy sutil */
  text-shadow: 1px 1px 2px black;
}}
.next {{
  right: 0;
  border-radius: 3px 0 0 3px;
}}
.prev:hover, .next:hover {{
  background-color: rgba(0,0,0,0.6);
}}

/* Texto Caption */
.text {{
  color: #f2f2f2;
  font-size: 16px;
  padding: 12px;
  position: absolute;
  bottom: 0px;
  width: 100%;
  text-align: center;
  background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0));
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  font-family: 'Helvetica', sans-serif;
  letter-spacing: 0.5px;
}}

/* Animación */
.fade {{animation-name: fade; animation-duration: 1.5s;}}
@keyframes fade {{from {{opacity: .4}} to {{opacity: 1}}}}
</style>
</head>
<body>

<div class="slideshow-container">
{slides_markup}
<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>

<script>
let slideIndex = 1;
let timer;
showSlides(slideIndex);

// Auto-play cada 4 segundos
timer = setInterval(function() {{ plusSlides(1); }}, 4000);

function plusSlides(n) {{
  clearInterval(timer); // Reinicia el timer al hacer click manual
  timer = setInterval(function() {{ plusSlides(1); }}, 4000);
  showSlides(slideIndex += n);
}}

function showSlides(n) {{
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {{slideIndex = 1}}    
  if (n < 1) {{slideIndex = slides.length}}
  for (i = 0; i < slides.length; i++) {{
    slides[i].style.display = "none";  
  }}
  slides[slideIndex-1].style.display = "block";  
}}
</script>

</body>
</html>
"""

components.html(html_code, height=460)

st.write("---")

# --- CONTACTO ---
st.subheader("¿Te interesa invertir?")
st.write("Agenda una visita hoy mismo.")

phone = "522221256530"
link_wa = f"https://wa.me/{phone}?text=Hola,%20me%20interesa%20informaci%C3%B3n%20de%20Deptos%2033.10"

st.markdown(f"""
<a href="{link_wa}" target="_blank" style="text-decoration: none;">
    <button style="width: 100%; background-color: #25D366; color: white; border: none; padding: 15px; border-radius: 8px; font-weight: bold; font-size: 1.1rem; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px;">
        <span>📲</span> Contactar por WhatsApp
    </button>
</a>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; margin-top: 30px; color: #aaa; font-size: 0.8rem;'>© 2025 Departamentos 33.10</div>", unsafe_allow_html=True)
