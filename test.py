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

    # Vérifier si toutes les valeurs ont été fournies
    if taille != 0.0 and sexe != "" and age != 0 and poids_initial != 0.0:
        # Calculer le poids idéal selon la formule de Lorentz pour les hommes
        if sexe == "M":
            poids_ideal = (taille * 100 - 100) - ((taille * 100 - 150) / 4) + ((age - 20) / 4)
        # Calculer le poids idéal selon la formule de Lorentz pour les femmes
        elif sexe == "F":
            poids_ideal = (taille * 100 - 100) - ((taille * 100 - 150) / 2.5) + ((age - 20) / 6)
        else:
            st.write("Sexe non valide.")

        # Calculer la différence entre le poids initial et le poids idéal
        difference_poids = poids_initial - poids_ideal

        # Afficher le poids idéal et la différence de poids
        st.write("Le poids idéal est de", poids_ideal, "kg.")
        st.write("La différence de poids est de", difference_poids, "kg.")

# # Appeler la fonction pour exécuter le programme
# calculer_poids()
recommander_regime(difference_poids)
def recommander_regime(difference_poids):
    if difference_poids > 0:
        st.write("Pour atteindre votre poids idéal, nous vous recommandons de suivre ces conseils alimentaires :")
        st.write("- Réduisez votre consommation de sucre et d'aliments riches en matières grasses.")
        st.write("- Augmentez votre consommation de légumes, de fruits et de protéines maigres.")
        st.write("- Faites de l'exercice régulièrement pour brûler des calories supplémentaires.")
    elif difference_poids < 0:
        st.write("Pour maintenir un poids santé, nous vous recommandons de suivre ces conseils alimentaires :")
        st.write("- Assurez-vous de consommer suffisamment de calories pour répondre à vos besoins énergétiques.")
        st.write("- Optez pour une alimentation équilibrée comprenant des légumes, des fruits, des céréales complètes et des protéines.")
        st.write("- Faites de l'exercice régulièrement pour renforcer votre tonus musculaire et maintenir votre métabolisme.")
    else:
        st.write("Votre poids est déjà idéal. Continuez à adopter de bonnes habitudes alimentaires et à rester actif pour maintenir votre poids.")
# Appeler la fonction pour exécuter le programme
calculer_poids()
