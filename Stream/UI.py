import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Departamentos 33.10",
    page_icon="🏢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS PERSONALIZADOS (CSS - MODO OSCURO ELEGANTE) ---
st.markdown("""
<style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Fondo general más oscuro para coincidir con tu flyer */
    .stApp {
        background-color: #f8f9fa;
    }

    /* Tipografía */
    h1 {
        font-family: 'Helvetica', sans-serif; 
        color: #1a1a1a; 
        font-weight: 800; 
        text-transform: uppercase;
        font-size: 2.5rem;
    }
    h2 {color: #333; font-weight: 300;}
    h3 {color: #B8860B; font-weight: 600;}
    
    /* PRECIO DESTACADO */
    .price-tag {
        background-color: #555; /* Gris del flyer */
        color: white;
        padding: 10px 20px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }

    /* Botones personalizados */
    .stButton>button {
        width: 100%;
        background-color: #1a1a1a; /* Negro casi puro */
        color: white;
        border-radius: 4px;
        border: none;
        padding: 16px;
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #333;
        color: #fff;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- CABECERA (HERO) ---
# Placeholder de imagen
st.image("https://placehold.co/800x500/2b2b2b/FFFFFF/png?text=DEPARTAMENTOS+33.10", use_container_width=True)

st.title("Departamentos 33.10")
st.markdown("📍 **UBICACIÓN:** 33 Oriente #10, Puebla, Pue.")

# --- PRECIO (NUEVO) ---
# Mostramos el precio destacado como en tu flyer
st.markdown('<div class="price-tag">Desde $2,940,000.00</div>', unsafe_allow_html=True)

st.write("---")

# --- SECCIÓN: UBICACIÓN ---
st.header("📍 Vive cerca de todo")
st.markdown("Conectividad inigualable en el corazón de Puebla.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Centro Histórico", value="5 min")
with col2:
    st.metric(label="Parque Ninfas", value="8 min")
with col3:
    st.metric(label="Paseo Bravo", value="13 min")

st.info("💡 **Puntos cercanos:** Plaza Dorada, La Noria, Parque Juárez y Prepa BUAP.")

st.write("---")

# --- SECCIÓN: MODELOS ---
st.header("📐 Elige tu Espacio")
tab_a, tab_b = st.tabs(["🏙️ TORRE A (89m²)", "🌇 TORRE B (96m²)"])

with tab_a:
    st.subheader("Modelo Inversión")
    # Imagen placeholder para Torre A
    st.image("https://placehold.co/600x400/e5e7eb/a3a3a3/png?text=Plano+Torre+A", use_container_width=True)
    col_feat1, col_feat2 = st.columns(2)
    with col_feat1:
        st.markdown("- **89 m²** Construcción\n- 🛏️ 2 Recámaras\n- 🚿 2 Baños")
    with col_feat2:
        st.markdown("- 🌳 Terraza Privada\n- 🚗 2 Cajones\n- ☀️ Paneles Solares")

with tab_b:
    st.subheader("Modelo Flexibilidad")
    # Imagen placeholder para Torre B
    st.image("https://placehold.co/600x400/e5e7eb/a3a3a3/png?text=Plano+Torre+B", use_container_width=True)
    col_feat1, col_feat2 = st.columns(2)
    with col_feat1:
        st.markdown("- **96 m²** Construcción\n- 🛏️ 2 Recámaras\n- 🚿 2 Baños")
    with col_feat2:
        st.markdown("- 🛋️ **Opción 3ª Habitación**\n- 🚗 2 Cajones\n- 📦 Bodega")

st.write("---")

# --- CALL TO ACTION (ACTUALIZADO) ---
st.subheader("¿Te interesa invertir?")
st.markdown("Agenda una visita al Showroom directamente con nosotros.")

# Botón con el número real
phone_number = "522221256530" # Número extraído de tu imagen
whatsapp_url = f"https://wa.me/{phone_number}?text=Hola,%20vi%20el%20flyer%20de%20Departamentos%2033.10%20y%20me%20interesa%20m%C3%A1s%20informaci%C3%B3n."

st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <button style="
            width: 100%;
            background-color: #25D366; 
            color: white; 
            border: none; 
            padding: 15px; 
            border-radius: 5px; 
            font-weight: bold; 
            font-size: 16px; 
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
            📲 CONTACTAR POR WHATSAPP
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; color: grey; font-size: 12px; margin-top: 30px;'>Departamentos 33.10 | Puebla, Pue.</div>", unsafe_allow_html=True)
