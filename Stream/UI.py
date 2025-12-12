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

# --- ESTILOS PERSONALIZADOS (MODO ARQUITECTÓNICO) ---
st.markdown("""
<style>
    /* 1. Fondo Gris Suave */
    .stApp, div[data-testid="stAppViewContainer"] {
        background-color: #f5f5f5 !important;
        color: #1a1a1a !important;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 2. Tipografía */
    h1 {
        font-family: 'Helvetica', sans-serif; 
        color: #111827 !important; 
        font-weight: 800; 
        text-transform: uppercase;
        font-size: 2.5rem;
        margin-top: 0px;
        margin-bottom: 10px;
        text-align: center;
    }
    
    h2 {color: #374151 !important; font-weight: 400;}
    h3 {color: #111827 !important; font-weight: 600;}
    p, li, .stMarkdown {color: #444444 !important;}
    
    /* 3. Etiqueta de Precio */
    .price-tag {
        background-color: #2b2b2b;
        color: #ffffff;
        padding: 10px 25px;
        font-size: 1.3rem;
        font-weight: 600;
        border-radius: 8px;
        display: inline-block;
        margin-top: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* 4. Métricas */
    div[data-testid="stMetricValue"] {
        color: #111827 !important;
        font-size: 1.3rem !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #666666 !important;
        font-size: 0.9rem !important;
    }
    
    /* 5. Botones Generales */
    .stButton>button {
        width: 100%;
        background-color: #111827;
        color: white !important;
        border-radius: 6px;
        border: none;
        padding: 16px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #333333;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    hr { border-color: #e0e0e0; margin: 30px 0; }
</style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE AYUDA PARA CARGAR IMÁGENES ---
def get_valid_path(filename):
    """Busca la imagen en local o en la carpeta Stream y devuelve la ruta válida."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_local = os.path.join(current_dir, filename)
    path_repo = f"Stream/{filename}"
    
    if os.path.exists(path_local):
        return path_local
    elif os.path.exists(path_repo):
        return path_repo
    elif os.path.exists(filename):
        return filename
    else:
        return None

def load_image_for_st(filename, fallback_text="IMAGEN"):
    """Para st.image (imágenes estáticas)"""
    path = get_valid_path(filename)
    if path:
        return path
    return f"https://placehold.co/800x500/e0e0e0/999999/png?text={fallback_text}"

# --- NUEVA FUNCIÓN PARA EL CARRUSEL ---
def get_base64_image(filename):
    """Convierte la imagen a Base64 para usarla en el HTML del carrusel."""
    path = get_valid_path(filename)
    if path:
        with open(path, "rb") as img_file:
            return f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode()}"
    return "https://placehold.co/800x500/e0e0e0/999999/png?text=Imagen+No+Encontrada"

# --- TÍTULO PRINCIPAL ---
st.title("Departamentos 33.10")
st.markdown("<div style='text-align: center; color: #555; margin-bottom: 20px;'><b>Puebla, Pue.</b> | 33 Oriente #10</div>", unsafe_allow_html=True)


# --- IMAGEN DE FACHADA ---
image_file = "imagen_2025-12-07_200507713.png"
valid_image_path = load_image_for_st(image_file, "VISTA+FACHADA")

col_izq, col_centro, col_der = st.columns([0.5, 3, 0.5]) 
with col_centro:
    st.image(valid_image_path, use_container_width=True)


# --- PRECIO DESTACADO ---
st.markdown('<div style="text-align: center;"><div class="price-tag">Desde $2,940,000.00</div></div>', unsafe_allow_html=True)

st.write("---")

# --- SECCIÓN: UBICACIÓN ---
map_file = "imagen_2025-12-07_202017772.png" 
valid_map_path = load_image_for_st(map_file, "MAPA+UBICACION")

st.image(valid_map_path, use_container_width=True)

google_maps_url = "https://www.google.com/maps/search/?api=1&query=33+Oriente+10+Puebla+Pue"
st.markdown(f"""
    <div style="text-align: center; margin: 10px 0 20px 0;">
        <a href="{google_maps_url}" target="_blank" style="text-decoration: none;">
            <button style="
                background-color: #4285F4; 
                color: white; 
                border: none; 
                padding: 10px 20px; 
                border-radius: 50px; 
                font-weight: bold; 
                font-size: 14px;
                cursor: pointer;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                📍 Ver en Google Maps
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("Todo lo que necesitas a menos de 15 minutos.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Facultad Medicina BUAP", value="5 min")
with col2:
    st.metric(label="Plaza Dorada", value="3 min")
with col3:
    st.metric(label="Centro Histórico", value="10 min")

st.caption("Cerca de: Parque Juárez, La Noria y Zona Universitaria.")

st.write("---")

# --- SECCIÓN: MODELOS ---
st.subheader("📐 Modelos Disponibles")

tab_a, tab_b = st.tabs(["Torre A (89m²)", "Torre B (96m²)"])

with tab_a:
    st.markdown("### Modelo A")
    img_torre_a = load_image_for_st("imagen_2025-12-12_171537244.png", "PLANO+TORRE+A")
    st.image(img_torre_a, use_container_width=True)
    
    st.write("") 
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        * **89 m²** Totales
        * 🛏️ 2 Recámaras
        * 🚿 2 Baños
        """)
    with c2:
        st.markdown("""
        * 🌳 Terraza
        * 🚗 2 Cajones
        * ☀️ Paneles Solares
        """)

with tab_b:
    st.markdown("### Modelo B")
    img_torre_b = load_image_for_st("imagen_2025-12-12_170832401.png", "PLANO+TORRE+B")
    st.image(img_torre_b, use_container_width=True)
    
    st.write("") 

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        * **96 m²** Totales
        * 🛏️ 2 Recámaras
        * 🚿 2 Baños
        """)
    with c2:
        st.markdown("""
        * 🛋️ **Opción 3ª Recámara**
        * 🚗 2 Cajones
        * 📦 Bodega
        """)

st.write("---")

# --- SECCIÓN: GALERÍA DE FOTOS (HTML/JS CARRUSEL) ---
st.subheader("📸 Galería Fotográfica")
st.write("Descubre cada detalle de tu próximo hogar.")

# 1. Preparamos las imágenes en Base64 para que el HTML pueda leerlas
img1_b64 = get_base64_image("Foto1.jpg") # Cocina
img4_b64 = get_base64_image("Foto4.jpg") # Fachada blanca
img2_b64 = get_base64_image("Foto2.jpg") # Cielo/Edificio azul
img3_b64 = get_base64_image("Foto3.jpg") # Interior vertical

# 2. Código HTML/CSS/JS del Carrusel
#    - autoplay de 4000ms (4 segundos)
#    - botones transparentes superpuestos
carousel_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
* {{box-sizing: border-box}}
body {{font-family: Helvetica, sans-serif; margin:0}}
.mySlides {{display: none; transition: opacity 1s ease-in-out;}}
img {{vertical-align: middle; width: 100%; border-radius: 10px; object-fit: cover; height: 500px;}}

/* Contenedor principal */
.slideshow-container {{
  max-width: 100%;
  position: relative;
  margin: auto;
}}

/* Botones Siguiente y Anterior */
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
  background-color: transparent; /* Fondo transparente por defecto */
  text-shadow: 0px 0px 5px rgba(0,0,0,0.7); /* Sombra al texto para que se vea en fondos blancos */
}}

/* Posición del botón derecho */
.next {{
  right: 0;
  border-radius: 3px 0 0 3px;
}}

/* Efecto Hover sutil */
.prev:hover, .next:hover {{
  background-color: rgba(0,0,0,0.1); /* Ligeramente oscuro al pasar el mouse */
}}

/* Texto del Caption */
.text {{
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
  background: rgba(0, 0, 0, 0.5);
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}}

/* Animación Fade */
.fade {{
  animation-name: fade;
  animation-duration: 1.5s;
}}

@keyframes fade {{
  from {{opacity: .4}} 
  to {{opacity: 1}}
}}
</style>
</head>
<body>

<div class="slideshow-container">

<div class="mySlides fade">
  <img src="{img1_b64}">
  <div class="text">Cocina Integral con Acabados de Lujo</div>
</div>

<div class="mySlides fade">
  <img src="{img4_b64}">
  <div class="text">Fachada Moderna y Exclusiva</div>
</div>

<div class="mySlides fade">
  <img src="{img2_b64}">
  <div class="text">Vistas Panorámicas</div>
</div>

<div class="mySlides fade">
  <img src="{img3_b64}">
  <div class="text">Diseño Arquitectónico de Vanguardia</div>
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>

</div>

<script>
let slideIndex = 1;
let slideInterval;

showSlides(slideIndex);
startAutoPlay(); // Inicia el movimiento automático

// Controles manuales
function plusSlides(n) {{
  showSlides(slideIndex += n);
  resetTimer(); // Reinicia el contador si el usuario toca un botón
}}

function currentSlide(n) {{
  showSlides(slideIndex = n);
  resetTimer();
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

function startAutoPlay() {{
    slideInterval = setInterval(function() {{
        plusSlides(1);
    }}, 4000); // 4000ms = 4 segundos
}}

function resetTimer() {{
    clearInterval(slideInterval);
    startAutoPlay();
}}
</script>

</body>
</html>
"""

# 3. Renderizar el componente
components.html(carousel_html, height=520)

st.write("---")

# --- CTA WHATSAPP ---
st.subheader("¿Te interesa?")
st.write("Agenda tu visita al Showroom.")

phone_number = "522221256530"
whatsapp_url = f"https://wa.me/{phone_number}?text=Hola,%20me%20interesa%20info%20de%20Deptos%2033.10"

st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <button style="
            width: 100%;
            background-color: #25D366; 
            color: white; 
            border: none; 
            padding: 16px; 
            border-radius: 8px; 
            font-weight: 600; 
            font-size: 16px; 
            cursor: pointer;
            transition: background-color 0.3s;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            📲 Agendar Visita por WhatsApp
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("<br><div style='text-align: center; color: #888; font-size: 12px;'>Departamentos 33.10 | Diseño Arquitectónico</div>", unsafe_allow_html=True)
