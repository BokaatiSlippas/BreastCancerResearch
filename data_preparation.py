import pandas as pd
import numpy as np

# Read the original file
input_filename = "METABRIC_RNA_Mutation.csv"
df = pd.read_csv(input_filename, usecols=[
    "age_at_diagnosis",
    "cancer_type",
    "cancer_type_detailed",
    "pam50_+_claudin-low_subtype",
    "pten", "tp53", "tp53bp1", "aurka", "egfr", "erbb2", "rpgr",
    "pten_mut", "tp53_mut", "rpgr_mut", "egfr_mut", "erbb2_mut",
    "overall_survival", "death_from_cancer"
])

# Function to create positional encoding with NaN handling
def create_positional_encoding(subtype, categories):
    encoding = ['0'] * len(categories)
    if pd.notna(subtype) and subtype in categories:
        index = categories.index(subtype)
        encoding[index] = '1'
    return ''.join(encoding)

# Get unique categories, handling NaN values properly
pam50_categories = sorted([x for x in df['pam50_+_claudin-low_subtype'].unique() if pd.notna(x)])
cancer_type_categories = sorted([x for x in df['cancer_type_detailed'].unique() if pd.notna(x)])

print("PAM50 categories:", pam50_categories)
print("Number of PAM50 categories:", len(pam50_categories))
print("Cancer type detailed categories:", cancer_type_categories)
print("Number of Cancer type categories:", len(cancer_type_categories))

# Encode both columns with proper NaN handling
df['pam50_encoded'] = df['pam50_+_claudin-low_subtype'].apply(
    lambda x: create_positional_encoding(x, pam50_categories)
)

df['cancer_type_detailed_encoded'] = df['cancer_type_detailed'].apply(
    lambda x: create_positional_encoding(x, cancer_type_categories)
)

# Optional: Drop original columns if desired
# df = df.drop(['pam50_+_claudin-low_subtype', 'cancer_type_detailed'], axis=1)

# Save the result
output_filename = 'metabric_encoded.csv'
df.to_csv(output_filename, index=False)

print(f"Encoding complete! File saved as: {output_filename}")
print("\nSample of encoded data:")
print(df[['pam50_+_claudin-low_subtype', 'pam50_encoded', 
          'cancer_type_detailed', 'cancer_type_detailed_encoded']].head(10))

# Check for missing values
print("\nMissing value counts:")
print("pam50_+_claudin-low_subtype:", df['pam50_+_claudin-low_subtype'].isna().sum())
print("cancer_type_detailed:", df['cancer_type_detailed'].isna().sum())