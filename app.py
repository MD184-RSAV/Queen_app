import streamlit as st

# Configuration du look "Peps"
st.set_page_config(page_title="Queen!", page_icon="👑")

st.markdown("""
    <style>
    .main { background-color: #FF007A; color: white; } /* Rose ultra peps */
    .stButton>button { 
        background-color: #00FFA3; color: black; /* Vert néon */
        border-radius: 10px; font-size: 20px; font-weight: bold; height: 3em; width: 100%;
    }
    h1, h2, h3 { color: white; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("Queen! 👑")

if 'step' not in st.session_state:
    st.session_state.step = 'accueil'

# --- ETAPE 1 : L'ACCUEIL ---
if st.session_state.step == 'accueil':
    st.subheader("Salut ma Reine ! Prête à briller ?")
    mood = st.text_area("Dis-moi tout : c'est quoi le mood dans ton corps et ta tête ?", placeholder="Je me sens comme une loque...")
    if st.button("REBOOT-MOI !"):
        st.session_state.mood = mood
        st.session_state.step = 'reboot'
        st.rerun()

# --- ETAPE 2 : LE REBOOT ---
elif st.session_state.step == 'reboot':
    st.subheader("Écoute-moi bien...")
    # Ici on intégrera l'IA plus tard. Pour le test :
    st.write(f"Ma poule, tu dis que tu es en mode '{st.session_state.mood}', mais moi je vois une Queen qui a juste besoin de secouer sa couronne. On ne se punit pas, on se célèbre. Tu bouges avec moi ?")
    
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

# --- ETAPE 3 : L'ACTION ---
elif st.session_state.step == 'action':
    if st.session_state.choice == "kiffe":
        st.subheader("Option : Le Kiffe Royal")
        st.write("Marche fière dans ton salon pendant 10 min. Tête haute, on savoure !")
    else:
        st.subheader("Option : L'Énergie Brute")
        st.write("10 min de danse sauvage ou de squats insolents. Fais trembler les murs !")
    
    if st.button("JE SUIS INCROYABLE ✅"):
        st.balloons()
        st.success("Mission accomplie, Majesté !")
        if st.button("Recommencer"):
            st.session_state.step = 'accueil'
            st.rerun()
