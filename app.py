import pandas as pd

# -----------------------------------
# STEP 1: Load the prepared dataset
# -----------------------------------
# (Make sure pharmgeno_mixed_1000.csv is in the same folder)
try:
    df = pd.read_csv("pharmgeno_mixed_1000.csv")
    print("✅ Dataset loaded successfully!")
    print(f"Total records: {len(df)}")
except FileNotFoundError:
    print("❌ Dataset file not found. Please check the file name or path.")
    raise SystemExit

# -----------------------------------
# STEP 2: Build lookup dictionary
# -----------------------------------
lookup = {}
for _, row in df.iterrows():
    key = (row["Variant/Haplotypes"].strip(), row["Drug(s)"].strip().lower())
    lookup[key] = row["Side Effect"]

print("✅ Lookup table ready with", len(lookup), "known combinations.")

# -----------------------------------
# STEP 3: User input
# -----------------------------------
while True:
    print("\n🔎 --- GeneGuard Lookup ---")
    variant_input = input("Enter DNA Variant (e.g., rs429358): ").strip()
    drug_input = input("Enter Medicine Name (e.g., warfarin): ").strip().lower()

    # -----------------------------------
    # STEP 4: Output prediction
    # -----------------------------------
    result = lookup.get((variant_input, drug_input), None)

    if result is None or result == "None":
        print("✅ Output: No Side Effect")
    else:
        print(f"⚠️ Output: {result}")

    # -----------------------------------
    # STEP 5: Ask if user wants to try again
    # -----------------------------------
    again = input("\nDo you want to check another combination? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("✅ Thank you for using GeneGuard!")
        break
