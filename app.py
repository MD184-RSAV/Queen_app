import streamlit as st
from openai import OpenAI

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Queen!", page_icon="👑")

# 2. STYLE "MD LABS" (Rose Peps et Vert Néon)
st.markdown("""
    <style>
    .main { background-color: #FF007A; color: white; }
    .stButton>button { 
        background-color: #00FFA3; color: black; 
        border-radius: 10px; font-size: 20px; font-weight: bold; height: 3em; width: 100%;
        border: none;
    }
    h1, h2, h3 { color: white; text-align: center; font-family: 'Arial Black', sans-serif; }
    .stTextArea textarea { background-color: #ffffff; color: #000000; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. INITIALISATION DU CLIENT OPENAI (La ligne qui manquait !)
# Assure-toi d'avoir configuré OPENAI_API_KEY dans les "Secrets" de Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Queen! 👑")

# Gestion des étapes de l'appli
if 'step' not in st.session_state:
    st.session_state.step = 'accueil'

# --- ÉTAPE 1 : L'ACCUEIL ---
if st.session_state.step == 'accueil':
    st.subheader("Salut ma Reine ! Vide ton sac...")
    mood = st.text_area("C'est quoi le mood là, tout de suite ?", placeholder="Sois cash, on est entre nous...", height=150)
    
    if st.button("REBOOT-MOI !"):
        if mood:
            st.session_state.mood = mood
            st.session_state.step = 'reboot'
            st.rerun()
        else:
            st.warning("Écris un petit truc quand même, je suis pas devine !")

# --- ÉTAPE 2 : LE REBOOT (L'IA EN ACTION) ---
elif st.session_state.step == 'reboot':
    st.subheader("Écoute-moi bien...")
    
    with st.spinner("Je prépare ton shot d'insolence..."):
        manifeste_queen = """
        Tu es Queen!, la coach la plus cash, drôle et insolente de la planète. 
        Ton job : Secouer l'utilisatrice avec amour pour la sortir de la culpabilité.
        
        RÈGLES D'OR :
        1. Tutoiement obligatoire. Utilise 'ma poule', 'meuf', 'ma reine', 'chérie'.
        2. Sois bonne vivante : le chocolat, le vin et les frites ne sont PAS des ennemis. 
        3. Interdiction de parler de régime ou de calories.
        4. Ton ton doit être un mix entre une humoriste de stand-up et une grande sœur protectrice.
        Format : Maximum 3 phrases percutantes.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": manifeste_queen},
                    {"role": "user", "content": f"Je me sens comme ça : {st.session_state.mood}"}
                ]
            )
            reponse_cash = response.choices[0].message.content
            st.markdown(f"### {reponse_cash}")
        except Exception as e:
            st.error(f"Oups, un petit souci technique avec le cerveau de l'IA... Vérifie ta clé API ! Erreur : {e}")
    
    st.write("---")
    st.write("### On fait quoi maintenant ?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("JE KIFFE ✨"):
            st.session_state.choice = "kiffe"
            st.session_state.step = 'action'
            st
# --- ÉTAPE 3 : L'ACTION ---
elif st.session_state.step == 'action':
    if st.session_state.choice == "kiffe":
        st.subheader("👑 Le Kiffe Royal")
        st.success("Prends une pause, mets ta musique préférée, et lâche-toi. Danse comme si personne ne te regardait. Tu es une reine, et les reines ont besoin de s'amuser pour régner. 💃✨")
    else:
        st.subheader("🔥 L'Énergie Brute")
        st.warning("On réveille la lionne ! 10 min de mouvements qui te font sentir SOLIDE. Danse, squats, boxe le vide... montre-moi ton insolence !")
    
    st.write("---")
    
    # On met les boutons dans des colonnes pour que ce soit joli
    col_fin1, col_fin2 = st.columns(2)
    
    with col_fin1:
        if st.button("JE SUIS INCROYABLE ✅"):
            st.balloons()
    
    with col_fin2:
        if st.button("RETOUR ACCUEIL 🏠"):
            st.session_state.step = 'accueil'
            st.rerun()
