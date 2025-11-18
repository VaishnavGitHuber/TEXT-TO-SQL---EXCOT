import pandas as pd
import sqlite3
# pip install pandas openpyxl


# Load Excel file
file_path = "input.xlsx"     
sheet_name = 0                    

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure required columns exist
if "Query Generated(GPT5)" not in df.columns:
    raise ValueError('Column "Query Generated(GPT5)" not found in Excel.')

# Add output columns if not present
if "Win(1)/Loss(0)" not in df.columns:
    df["Win(1)/Loss(0)"] = ""

if "Type Error" not in df.columns:
    df["Type Error"] = ""

# Connect to SQLite database
db_path = "california_schools.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# Execute all queries
for i, query in df["Query Generated(GPT5)"].items():
    try:
        cursor.execute(query)
        conn.commit()

        # Success
        df.at[i, "Win(1)/Loss(0)"] = 1
        df.at[i, "Type Error"] = ""
    
    except Exception as e:
        # Failure
        df.at[i, "Win(1)/Loss(0)"] = 0
        df.at[i, "Type Error"] = str(e)


# Save new Excel
output_file = "query_validation_output.xlsx"
df.to_excel(output_file, index=False)

print(f"Completed! Output saved to: {output_file}")
