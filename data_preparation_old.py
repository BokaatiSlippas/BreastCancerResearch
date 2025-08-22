import csv

desired_columns = [
    "age_at_diagnosis",
    "cancer_type",
    "cancer_type_detailed",
    "pam50_+_claudin-low_subtype",
    "pten",           # Gene expression
    "tp53",           # Gene expression
    "tp53bp1",
    "aurka",          # Gene expression
    "egfr",           # Gene expression
    "erbb2",          # Gene expression (HER2)
    "rpgr",           # Gene expression
    "pten_mut",       # Mutation status
    "tp53_mut",       # Mutation status
    "rpgr_mut",       # Mutation status
    "egfr_mut",       # Mutation status
    "erbb2_mut",       # Mutation status (HER2)
    "overall_survival",
    "death_from_cancer"
]

input_filename = "METABRIC_RNA_Mutation.csv"
output_filename = "metabric_filtered.csv"
with open(input_filename, 'r', newline='') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=desired_columns)
    writer.writeheader()

    for row in reader:
        filtered_row = {col: row[col] for col in desired_columns}
        writer.writerow(filtered_row)