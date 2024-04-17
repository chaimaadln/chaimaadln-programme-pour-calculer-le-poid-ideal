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
        st.write("Le poids idéal est ", round(poids_ideal,2), "kg.")
        st.write("La différence de poids est ", round(difference_poids, 2), "kg.")

        # Vérifier la différence de poids et afficher les recommandations diététiques correspondantes
        if difference_poids > 0:
            st.write("*votre poids est superieur a votre poids ideal*")
            st.write("Pour atteindre votre poids idéal, vous pouvez suivre ces recommandations :")
            st.write("  - Réduisez votre consommation de calories en limitant les aliments riches en matières grasses et en sucre.")
            st.write("  - Augmentez votre consommation de fruits, légumes et aliments riches en fibres.")
            st.write("  - Pratiquez une activité physique régulière pour brûler des calories.")

        elif difference_poids < 0:
            st.write("*votre poids est inferieur a votre poids ideal*")
            st.write("Pour maintenir un poids sain, vous pouvez suivre ces recommandations :")
            st.write("- Assurez-vous de consommer suffisamment de calories pour répondre à vos besoins nutritionnels.")
            st.write("- Choisissez des aliments nutritifs et équilibrés, comprenant des protéines, des glucides, des lipides et des vitamines.")
            st.write("- Restez actif et intégrez une activité physique régulière à votre routine.")

# Appeler la fonction pour exécuter le programme
calculer_poids()
