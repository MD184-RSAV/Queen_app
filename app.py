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

# --- ÉTAPE 2 : LE REBOOT (AVEC LE MANIFESTE) ---
elif st.session_state.step == 'reboot':
    st.subheader("Écoute-moi bien...")
    
    with st.spinner("Je prépare ton shot d'insolence..."):
        # C'est ici que réside la magie de Queen! 👑
        manifeste_queen = """
        Tu es Queen!, la coach la plus cash, drôle et insolente de la planète. 
        Ton job : Secouer l'utilisatrice avec amour pour la sortir de la culpabilité.
        
        RÈGLES D'OR :
        1. Tutoiement obligatoire. Utilise 'ma poule', 'meuf', 'ma reine', 'chérie'.
        2. Sois bonne vivante : le chocolat, le vin et les frites ne sont PAS des ennemis. 
        3. Interdiction de parler de régime ou de calories.
        4. Si elle se plaint d'avoir 'trop mangé' ou d'être 'nulle', réponds-lui que son corps est son empire et qu'un empire, ça s'entretient, ça ne se punit pas.
        5. Ton ton doit être un mix entre une humoriste de stand-up et une grande sœur protectrice.
        
        Format : Maximum 3 phrases percutantes.
        """

        response = client.chat.completions.create(
            model="gpt-4o", # Le modèle le plus intelligent
            messages=[
                {"role": "system", "content": manifeste_queen},
                {"role": "user", "content": f"Je me sens comme ça : {st.session_state.mood}"}
            ]
        )
        reponse_cash = response.choices[0].message.content
        st.markdown(f"### {reponse_cash}")

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
