import streamlit as st
import pandas as pd

def run():
    st.set_page_config(
        page_title="Application de Vocabulaire Allemand",
        page_icon="🇩🇪 ",
        layout="wide",
    )

    st.title("🇩🇪 Application de Vocabulaire Allemand")

    try:
        df = pd.read_csv("vocabulary.csv")
    except FileNotFoundError:
        st.error("Erreur : vocabulary.csv introuvable. Veuillez vous assurer que le fichier se trouve dans le même répertoire que l'application.")
        return

    st.sidebar.header("Filtrer le Vocabulaire")

    # Get unique categories and sub-categories
    categories = ["Tout"] + list(df["catégorie"].unique())
    selected_category = st.sidebar.selectbox("Catégorie", categories)

    if selected_category == "Tout":
        filtered_df = df
    else:
        filtered_df = df[df["catégorie"] == selected_category]

    sub_categories = ["Tout"] + list(filtered_df["sous catégorie"].unique())
    selected_sub_category = st.sidebar.selectbox("Sous-catégorie", sub_categories)

    if selected_sub_category != "Tout":
        filtered_df = filtered_df[filtered_df["sous catégorie"] == selected_sub_category]

    st.markdown("--- # Sélectionner les colonnes à afficher")
    all_columns = df.columns.tolist()
    default_columns = [col for col in all_columns if col not in ["catégorie", "sous catégorie"]]
    selected_columns = st.multiselect(
        "Colonnes",
        all_columns,
        default=default_columns
    )

    if selected_columns:
        st.subheader(f"Vocabulaire ({len(filtered_df)} mots)")
        st.dataframe(filtered_df[selected_columns])
    else:
        st.warning("Veuillez sélectionner au moins une colonne à afficher.")


if __name__ == "__main__":
    run()