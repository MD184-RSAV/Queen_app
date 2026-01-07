import streamlit as st
from openai import OpenAI

# CONFIGURATION & STYLE
st.set_page_config(page_title="Queen!", page_icon="👑")
st.markdown("""
    <style>
    .main { background-color: #FF007A; color: white; }
    .stButton>button { 
        background-color: #00FFA3; color: black; border-radius: 10px; 
        font-size: 20px; font-weight: bold; width: 100%; border: none;
    }
    h1, h2, h3 { color: white; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# INITIALISATION IA
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if 'step' not in st.session_state:
    st.session_state.step = 'accueil'

# --- ÉTAPE 1 : ACCUEIL ---
if st.session_state.step == 'accueil':
    st.title("Queen! 👑")
    st.subheader("Salut ma Reine ! Vide ton sac...")
    mood = st.text_area("C'est quoi le mood ?", placeholder="Sois cash...", height=150)
    if st.button("REBOOT-MOI !"):
        if mood:
            st.session_state.mood = mood
            st.session_state.step = 'reboot'
            st.rerun()

# --- ÉTAPE 2 : LE REBOOT ---
elif st.session_state.step == 'reboot':
    st.title("Écoute-moi bien...")
    with st.spinner("Ton shot d'insolence arrive..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Tu es Queen!, une coach insolente et cash. Tutoiement obligatoire. Max 3 phrases."},
                {"role": "user", "content": st.session_state.mood}
            ]
        )
        st.markdown(f"### {response.choices[0].message.content}")
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("JE KIFFE ✨"):
            st.session_state.choice = "kiffe"
            st.session_state.step = 'action'
            st.rerun()
    with col2:
        if st.button("J'ENVOIE 🔥"):
            st.session_state.choice = "envoie"
            st.session_state.step = 'action'
            st.rerun()

# --- ÉTAPE 3 : L'ACTION ---
elif st.session_state.step == 'action':
    st.title("Ton Plan de Règne 👑")
    if st.session_state.choice == "kiffe":
        st.success("Option KIFFE : Mets du son, danse 10 min. C'est un ordre de ta Reine. 💃")
    else:
        st.warning("Option ENVOIE : 10 min de squats ou de boxe. On veut de la puissance ! 🔥")
    
    st.write("---")
    if st.button("RETOUR ACCUEIL 🏠"):
        st.session_state.step = 'accueil'
        st.rerun()
