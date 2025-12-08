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
        font-size: 1.5rem !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #666666 !important;
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

# --- SECCIÓN: UBICACIÓN (MAPA REDUCIDO) ---
st.subheader("📍 Ubicación Estratégica")

# Mapa
map_file = "imagen_2025-12-07_201722511.png"
valid_map_path = load_image(map_file, "MAPA+UBICACION")

# REDUCCIÓN DE TAMAÑO: Usamos columnas [1, 3, 1] para que ocupe aprox el 60% del ancho
c_map_L, c_map_C, c_map_R = st.columns([1, 3, 1])
with c_map_C:
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
    st.metric(label="Centro Histórico", value="5 min")
with col2:
    st.metric(label="Parque Ninfas", value="8 min")
with col3:
    st.metric(label="Paseo Bravo", value="13 min")

st.caption("Cerca de: Plaza Dorada, La Noria, Parque Juárez y Prepa BUAP.")

st.write("---")

# --- SECCIÓN: MODELOS ---
st.subheader("📐 Modelos Disponibles")

tab_a, tab_b = st.tabs(["Torre A (89m²)", "Torre B (96m²)"])

with tab_a:
    st.markdown("### Modelo Inversión")
    # PLANO ORIGINAL
    st.image("https://placehold.co/600x400/e5e5e5/a0a0a0/png?text=Plano+Torre+A", use_container_width=True)
    
    # BOCETO DE RECÁMARA (NUEVO)
    # Sube tu imagen como 'recamara_a.png' o cambia el nombre aquí
    img_recamara_a = load_image("recamara_a.png", "BOCETO+RECAMARA+A")
    st.image(img_recamara_a, caption="Proyección de Recámara Principal", use_container_width=True)
    
    st.write("") # Espacio
    
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
    st.markdown("### Modelo Flexibilidad")
    # PLANO ORIGINAL
    st.image("https://placehold.co/600x400/e5e5e5/a0a0a0/png?text=Plano+Torre+B", use_container_width=True)
    
    # BOCETO DE RECÁMARA (NUEVO)
    # Sube tu imagen como 'recamara_b.png' o cambia el nombre aquí
    img_recamara_b = load_image("recamara_b.png", "BOCETO+RECAMARA+B")
    st.image(img_recamara_b, caption="Proyección de Espacios Amplios", use_container_width=True)

    st.write("") # Espacio

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

# --- NUEVA SECCIÓN: GALERÍA DE DECORACIÓN ---
st.subheader("✨ Estilo y Acabados")
st.write("Una muestra de la atmósfera que podrás disfrutar.")

# Sube tus imágenes como 'decoracion_1.png', 'decoracion_2.png', etc.
col_d1, col_d2 = st.columns(2)
with col_d1:
    img_deco1 = load_image("decoracion_1.png", "DECORACION+1")
    st.image(img_deco1, use_container_width=True)
with col_d2:
    img_deco2 = load_image("decoracion_2.png", "DECORACION+2")
    st.image(img_deco2, use_container_width=True)

# Tercera imagen centrada más grande
img_deco3 = load_image("decoracion_3.png", "DECORACION+3")
st.image(img_deco3, use_container_width=True)

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
