#MOD1
#Dataset upload check 
import pandas as pd
file_path = "Brain_GSE50161.csv"
df = pd.read_csv(file_path)
print(f"{df.shape[0]} rows (patients) and {df.shape[1]} columns (features).") 

#MOD2
# CuMiDa datasets usually have one text column for the cancer type (e.g., 'Ependymoma').
# find it by looking for the column that isn't a number.

label_column = df.select_dtypes(exclude=['float64', 'int64']).columns[0]

# Isolate just the numerical gene expression data
gene_data = df.select_dtypes(include=['float64', 'int64'])

#statistical variance of all features

variances = gene_data.var()

# We sort from highest variance to lowest, and grab the names (index) of the top 1000
top_1000_gene_names = variances.sort_values(ascending=False).head(1000).index

# Rebuild the dataset with only the important data
df_optimized = df[[label_column] + list(top_1000_gene_names)]

# 5. Verify the new, compressed dimensions
print(f"Old Dataset Structure: {df.shape[0]} rows and {df.shape[1]} columns.")
print(f"Optimized Structure: {df_optimized.shape[0]} rows and {df_optimized.shape[1]} columns.")

# View the new optimized DataFrame
df_optimized.head()

#MOD3
import pybiomart

# 1. Connect to the public human genomic assembly
server = pybiomart.Dataset(name='hsapiens_gene_ensembl', host='http://www.ensembl.org')

# 2. Query using the correct Affymetrix chip name
query_attributes = ['affy_hg_u133_plus_2', 'chromosome_name', 'start_position', 'band']
reference_table = server.query(attributes=query_attributes)

# 3. Clean up the database column names to match your project specs
reference_table.columns = ['Probe_ID', 'Chromosome_Number', 'Base_Pair_Start', 'Cytoband_Location']

# 4. Clean out empty rows and view the downloaded external reference table
reference_table.dropna(inplace=True)
print("Reference Table Downloaded Successfully!")
print(reference_table.head())

#MOD4
export_filename = "OncoLens_Annotated_Top1000.csv"

# Extract the gene probe IDs from df_optimized (excluding 'type' and 'samples')
# Based on the df_optimized.head() output, the gene names start from the third column
gene_probe_ids = df_optimized.columns[2:].to_frame(name='Probe_ID')

# Merge with the reference_table to get the annotations
final_annotated_genes = pd.merge(gene_probe_ids, reference_table, on='Probe_ID', how='left')

final_annotated_genes.to_csv(export_filename, index=False)

print(f"Success! Your data is saved as: {export_filename}")

#MOD5
# Print the first 10 genetic feature names
print(df_optimized.columns[1:11])
