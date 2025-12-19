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

# --- ESTILOS PERSONALIZADOS (MODO 'KIOSCO' LIMPIO) ---
st.markdown("""
<style>
    /* 1. Fondo y Colores Generales */
    .stApp, div[data-testid="stAppViewContainer"] {
        background-color: #f8f9fa !important;
        color: #212529 !important;
    }
    
    /* 2. OCULTAR ELEMENTOS DE INTERFAZ (GitHub, Menús, etc.) */
    
    /* Oculta la barra superior completa (donde sale tu foto y el menú) */
    header[data-testid="stHeader"] {
        visibility: hidden;
        display: none !important;
        height: 0px !important;
        padding: 0px !important;
    }
    
    /* Oculta el menú de hamburguesa específicamente */
    #MainMenu {
        visibility: hidden;
        display: none !important;
    }
    
    /* Oculta el footer estándar dentro de la app */
    footer {
        visibility: hidden;
        display: none !important;
    }
    
    /* Oculta la barra de herramientas del desarrollador */
    div[data-testid="stToolbar"] {
        visibility: hidden; 
        display: none !important;
    }
    
    /* Oculta el botón de 'Deploy' si llegara a aparecer */
    .stDeployButton {
        display: none !important;
    }
    
    /* Ajuste para subir el contenido al tope de la pantalla */
    .block-container {
        padding-top: 2rem !important; /* Mínimo espacio arriba */
        padding-bottom: 2rem !important;
    }

    /* 3. Estilos del Flyer */
    
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
    
    /* Etiqueta de Precio (NO usada ya, pero la dejo por si la usas después) */
    .price-tag {
        background-color: #2b2b2b;
        color: #ffffff;
        padding: 12px 30px;
        font-size: 1.4rem;
        font-weight: 700;
        border-radius: 50px;
        display: inline-block;
        margin-top: 10px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }

    /* Mensaje de Urgencia */
    .urgency-box {
        background-color: #ffebee;
        color: #c62828;
        border: 1px solid #ffcdd2;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: 800;
        text-transform: uppercase;
        margin: 15px 0;
        font-size: 1.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    /* Tarjetas de Tiempo */
    .time-card {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    .time-val { font-size: 1.5rem; font-weight: bold; color: #111827; }
    .time-label { font-size: 0.85rem; color: #666; text-transform: uppercase; margin-top: 5px; }

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

    /* --- Caja de precio (ARREGLADA: responsive + sin desbordes) --- */
    .price-box{
      background-color:#111827;
      border-radius:14px;
      padding:20px 22px;
      text-align:center;
      margin:25px auto;
      width:100%;
      max-width:440px;
      box-shadow:0 15px 35px rgba(0,0,0,0.25);
      overflow:hidden;
      box-sizing:border-box;
      transform-origin:center;
      animation:pulse 2s infinite;
    }
    .price-box .badge{
      color:#ffffff;
      font-weight:900;
      text-transform:uppercase;
      font-size:1.35rem;
      margin-bottom:12px;
      letter-spacing:0.5px;
    }
    .price-box .price-pill{
      background-color:#ffffff;
      color:#111827;
      display:inline-block;
      padding:12px 34px;
      border-radius:999px;
      font-size:1.35rem;
      font-weight:800;
      box-shadow:0 6px 15px rgba(0,0,0,0.2);
      white-space:nowrap;
    }
    @media (max-width:480px){
      .price-box{ padding:18px 16px; }
      .price-box .badge{ font-size:1.1rem; }
      .price-box .price-pill{ font-size:1.15rem; padding:10px 18px; }
    }
</style>
""", unsafe_allow_html=True)

# --- FUNCIONES DE UTILIDAD ---
def get_valid_path(filename):
    base_dirs = ["", "Stream", "stream"]
    name, ext = os.path.splitext(filename)
    variations = [
        filename, 
        filename.lower(), 
        filename.capitalize(),
        f"{name.lower()}{ext.lower()}",
        f"{name.capitalize()}{ext.lower()}"
    ]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for base in base_dirs:
        for variant in variations:
            if os.path.exists(os.path.join(base, variant)):
                return os.path.join(base, variant)
            full_path = os.path.join(current_dir, base, variant)
            if os.path.exists(full_path):
                return full_path
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

# --- CONTENIDO ---
st.title("Departamentos 33.10")
st.markdown("<div style='text-align: center; color: #6c757d; margin-bottom: 20px; font-weight: 500;'>33 Oriente #10, Puebla, Pue.</div>", unsafe_allow_html=True)

# Portada
hero_image = load_image_for_st("imagen_2025-12-07_200507713.png", "FACHADA PRINCIPAL") 
col_L, col_C, col_R = st.columns([0.1, 4, 0.1])
with col_C:
    st.image(hero_image, use_container_width=True)

# Precio y Urgencia (ARREGLADO)
st.markdown("""
<div class="price-box">
  <div class="badge">🔥 Últimos 3 departamentos disponibles</div>
  <div class="price-pill">Desde $2,940,000.00</div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Ubicación
map_path = load_image_for_st("imagen_2025-12-07_202017772.png", "MAPA UBICACION")
st.image(map_path, use_container_width=True)

link_maps = "https://www.google.com/maps/search/?api=1&query=33+Oriente+10+Puebla+Pue"
st.markdown(f"""
    <div style="text-align: center; margin-top: 15px; margin-bottom: 25px;">
        <a href="{link_maps}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #0d6efd; color: white; border: none; padding: 10px 25px; border-radius: 50px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                📍 Ver en Google Maps
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# Tiempos
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="time-card"><div class="time-val">5 min</div><div class="time-label">Medicina BUAP</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="time-card"><div class="time-val">3 min</div><div class="time-label">Plaza Dorada</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="time-card"><div class="time-val">10 min</div><div class="time-label">Centro Histórico</div></div>', unsafe_allow_html=True)

st.markdown("<div style='text-align:center; color:#888; font-size:0.8rem; margin-top:5px;'>Cerca de: Parque Juárez, La Noria y Zona Universitaria.</div>", unsafe_allow_html=True)

st.write("---")

# Modelos
st.subheader("📐 Modelos ")
tab_a, tab_b = st.tabs(["Torre A ", "Torre B "])

with tab_a:
    st.markdown("##### 🏢 Modelo A")
    img_modelo_a = load_image_for_st("imagen_2025-12-12_171537244.png", "PLANO TORRE A")
    st.image(img_modelo_a, use_container_width=True)

with tab_b:
    st.markdown("##### 🏢 Modelo B")
    img_modelo_b = load_image_for_st("imagen_2025-12-12_170832401.png", "PLANO TORRE B")
    st.image(img_modelo_b, use_container_width=True)

st.write("---")

# Galería
st.subheader("📸 Galería del Proyecto")
st.write("Descubre cada detalle de tu próximo hogar.")

carousel_data = [
    {"file": "foto11.jpg", "caption": "Fachada Principal con Áreas Verdes"},
    {"file": "Foto1.jpg", "caption": "Cocina Equipada y Cubierta de Cuarzo"},
    {"file": "Foto2.jpg", "caption": "Vistas Exteriores"},
    {"file": "Foto3.jpg", "caption": "Patios Interiores y Ventilación"},
    {"file": "Foto4.jpg", "caption": "Arquitectura Moderna"},
    {"