import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv("pharmgeno_mixed_1000.csv")

st.title("🧬 GeneGuard - Side Effect Checker")
st.write("Enter a DNA Variant and a Medicine to check if any side effect is known.")

# User input fields
variant = st.text_input("Enter DNA Variant (e.g., rs429358):")
medicine = st.text_input("Enter Medicine name (e.g., aspirin):")

if st.button("Check Side Effect"):
    if variant and medicine:
        # Filter dataset
        result = df[(df["Variant/Haplotypes"].str.lower() == variant.strip().lower()) &
                    (df["Drug(s)"].str.lower() == medicine.strip().lower())]
        
        if not result.empty:
            side_effects = result["Side Effect"].tolist()
            # Remove duplicates
            side_effects = list(set(side_effects))
            # Check if all are "None"
            if all(se.lower() == "none" for se in side_effects):
                st.success(f"✅ No known side effects for {variant} with {medicine}.")
            else:
                st.error(f"⚠️ Known side effect(s) for {variant} with {medicine}: {', '.join(side_effects)}")
        else:
            st.info(f"No data found for {variant} with {medicine}. It might be safe, but not in our dataset.")
    else:
        st.warning("Please enter both DNA Variant and Medicine.")


    
