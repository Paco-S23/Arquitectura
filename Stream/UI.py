import streamlit as st
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Departamentos 33.10",
    page_icon="🏢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS PERSONALIZADOS (MODO CLARO MINIMALISTA) ---
st.markdown("""
<style>
    /* 1. Forzar Fondo Blanco Puro y Texto Oscuro */
    .stApp, div[data-testid="stAppViewContainer"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 2. Tipografía Limpia */
    h1 {
        font-family: 'Helvetica', sans-serif; 
        color: #111827 !important; 
        font-weight: 800; 
        text-transform: uppercase;
        font-size: 2.2rem;
        margin-bottom: 0px;
    }
    h2 {color: #374151 !important; font-weight: 400;}
    h3 {color: #111827 !important; font-weight: 600;}
    p, li, .stMarkdown {color: #4B5563 !important;}
    
    /* 3. Etiqueta de Precio */
    .price-tag {
        background-color: #f3f4f6;
        color: #111827;
        padding: 8px 16px;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 99px;
        border: 1px solid #e5e7eb;
        display: inline-block;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* 4. Tarjetas de Métricas */
    div[data-testid="stMetricValue"] {
        color: #111827 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #6B7280 !important;
    }

    /* 5. Botones */
    .stButton>button {
        width: 100%;
        background-color: #111827;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 14px;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #374151;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    hr { border-color: #f3f4f6; }
</style>
""", unsafe_allow_html=True)

# --- CABECERA (HERO) ---

# Lógica para cargar la imagen localmente o usar fallback si no existe
# Esto evita que la app se rompa si olvidas subir la imagen
image_path = "stream/imagen_2025-12-07_194253899.png"
# Nota: Si pruebas esto en local (no en Cloud), la ruta podría ser solo el nombre del archivo dependiendo de dónde corras el comando.
# Streamlit Cloud corre desde la raíz del repo, por eso "stream/..."

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    # Intenta buscar en la raíz por si acaso
    if os.path.exists("imagen_2025-12-07_194253899.png"):
        st.image("imagen_2025-12-07_194253899.png", use_container_width=True)
    else:
        st.error("⚠️ No se encontró la imagen. Asegúrate de que 'imagen_2025-12-07_194253899.png' esté en la carpeta 'stream' en GitHub.")
        st.image("https://placehold.co/800x450/f3f4f6/9ca3af/png?text=SUBE+TU+IMAGEN+AL+REPO", use_container_width=True)

st.title("Departamentos 33.10")
st.markdown("**Puebla, Pue.** | 33 Oriente #10")

# Precio estilo Badge
st.markdown('<div class="price-tag">$2,940,000.00</div>', unsafe_allow_html=True)

st.write("---")

# --- SECCIÓN: UBICACIÓN ---
st.subheader("📍 Ubicación Estratégica")
st.markdown("Todo lo que necesitas a menos de 15 minutos.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Centro Histórico", value="5 min")
with col2:
    st.metric(label="Parque Ninfas", value="8 min")
with col3:
    st.metric(label="Paseo Bravo", value="13 min")

# Nota pequeña estilo caption
st.caption("Cerca de: Plaza Dorada, La Noria, Parque Juárez y Prepa BUAP.")

st.write("---")

# --- SECCIÓN: MODELOS ---
st.subheader("📐 Modelos Disponibles")

# Tabs limpias
tab_a, tab_b = st.tabs(["Torre A (89m²)", "Torre B (96m²)"])

with tab_a:
    st.image("https://placehold.co/600x400/f9fafb/d1d5db/png?text=Plano+Torre+A", use_container_width=True)
    st.markdown("### Modelo Inversión")
    
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
    st.image("https://placehold.co/600x400/f9fafb/d1d5db/png?text=Plano+Torre+B", use_container_width=True)
    st.markdown("### Modelo Flexibilidad")
    
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

st.markdown("<br><div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Departamentos 33.10 | Diseño Arquitectónico</div>", unsafe_allow_html=True)
