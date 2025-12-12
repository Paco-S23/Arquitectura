import streamlit as st
import os

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
    
    /* 5. Botones */
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
    
    /* Estilos para los botones del carrusel (más pequeños) */
    .stButton.carousel-btn>button {
        padding: 5px 10px !important;
        font-size: 20px !important;
    }

    hr { border-color: #e0e0e0; margin: 30px 0; }
</style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE AYUDA PARA CARGAR IMÁGENES ---
def load_image(filename, fallback_text="IMAGEN"):
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
        return f"https://placehold.co/800x500/e0e0e0/999999/png?text={fallback_text}"

# --- TÍTULO PRINCIPAL ---
st.title("Departamentos 33.10")
st.markdown("<div style='text-align: center; color: #555; margin-bottom: 20px;'><b>Puebla, Pue.</b> | 33 Oriente #10</div>", unsafe_allow_html=True)


# --- IMAGEN DE FACHADA ---
image_file = "imagen_2025-12-07_200507713.png"
valid_image_path = load_image(image_file, "VISTA+FACHADA")

col_izq, col_centro, col_der = st.columns([0.5, 3, 0.5]) 
with col_centro:
    st.image(valid_image_path, use_container_width=True)


# --- PRECIO DESTACADO ---
st.markdown('<div style="text-align: center;"><div class="price-tag">Desde $2,940,000.00</div></div>', unsafe_allow_html=True)

st.write("---")

# --- SECCIÓN: UBICACIÓN ---
# Mapa
map_file = "imagen_2025-12-07_202017772.png" 
valid_map_path = load_image(map_file, "MAPA+UBICACION")

# EL MAPA USA TODO EL ANCHO DISPONIBLE
st.image(valid_map_path, use_container_width=True)

# Botón Maps
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
    img_torre_a = load_image("imagen_2025-12-12_171537244.png", "PLANO+TORRE+A")
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
    img_torre_b = load_image("imagen_2025-12-12_170832401.png", "PLANO+TORRE+B")
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

# --- NUEVA SECCIÓN: GALERÍA INTERACTIVA (CARRUSEL) ---
st.subheader("📸 Galería Fotográfica")
st.write("Descubre cada detalle de tu próximo hogar.")

# Lógica del Carrusel
if 'gallery_index' not in st.session_state:
    st.session_state.gallery_index = 0

# Lista de imágenes (Asegúrate de subirlas con estos nombres)
gallery_images = ["Foto1.jpg", "Foto4.jpg", "Foto2.jpg", "Foto3.jpg"]
gallery_captions = [
    "Cocina Integral con Acabados de Lujo", 
    "Fachada Moderna y Exclusiva", 
    "Vistas Panorámicas", 
    "Diseño Arquitectónico de Vanguardia"
]

# Controles de navegación
col_prev, col_display, col_next = st.columns([1, 8, 1])

with col_prev:
    st.write("") # Espaciador vertical para centrar botón
    st.write("") 
    st.write("")
    if st.button("◀", key="prev_btn"):
        st.session_state.gallery_index = (st.session_state.gallery_index - 1) % len(gallery_images)

with col_next:
    st.write("") # Espaciador vertical
    st.write("")
    st.write("")
    if st.button("▶", key="next_btn"):
        st.session_state.gallery_index = (st.session_state.gallery_index + 1) % len(gallery_images)

with col_display:
    # Mostrar imagen actual
    current_img_name = gallery_images[st.session_state.gallery_index]
    current_caption = gallery_captions[st.session_state.gallery_index]
    
    # Cargamos la imagen
    img_path = load_image(current_img_name, "GALERIA")
    
    st.image(img_path, caption=f"{st.session_state.gallery_index + 1}/{len(gallery_images)} - {current_caption}", use_container_width=True)


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
