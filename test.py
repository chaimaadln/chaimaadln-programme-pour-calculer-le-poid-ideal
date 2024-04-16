import streamlit as st

def calculer_poids():
    # Demander la taille à l'utilisateur en mètres
    taille = st.number_input("Entrez la taille en mètres : ", min_value=0.0)

    # Demander le sexe de la personne
    sexe = st.radio("Entrez le sexe :", ("M", "F"))

    # Demander l'âge de la personne
    age = st.number_input("Entrez l'âge : ", min_value=0)

    # Demander le poids initial de la personne
    poids_initial = st.number_input("Entrez le poids initial en kg : ", min_value=0.0)

    # Initialiser le poids idéal à None
    poids_ideal = None

    # Calculer le poids idéal selon la formule de Lorentz pour les hommes
    if sexe == "M":
        poids_ideal = (taille * 100 - 100) - ((taille * 100 - 150) / 4) + ((age - 20) / 4)
    # Calculer le poids idéal selon la formule de Lorentz pour les femmes
    elif sexe == "F":
        poids_ideal = (taille * 100 - 100) - ((taille * 100 - 150) / 2.5) + ((age - 20) / 6)
    else:
        st.write("Sexe non valide.")

    # Vérifier si le poids idéal a été calculé avec succès
    if poids_ideal is not None:
        # Calculer la différence entre le poids initial et le poids idéal
        difference_poids = poids_initial - poids_ideal

        # Afficher le poids idéal et la différence de poids
        st.write("Le poids idéal est de", poids_ideal, "kg.")
        st.write("La différence de poids est de", difference_poids, "kg.")

# Appeler la fonction pour exécuter le programme
calculer_poids()
