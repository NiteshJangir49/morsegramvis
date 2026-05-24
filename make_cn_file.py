import pandas as pd

# Read the CSV file
df = pd.read_csv("dataset_files/Steel Beads/data/all_particle_stats.csv")

# Open text file for writing
with open("dataset_files/Steel Beads/data/cn_file.txt", "w", encoding="utf-8") as f:
    # Loop through rows and combine 2 columns
    for _, row in df.iterrows():
        text = f"{int(row['cp_id'])} {row['cn']}\n"
        f.write(text)

print("Done! Data written to output.txt")