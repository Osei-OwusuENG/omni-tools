import pandas as pd
from pathlib import Path

# Folder with Excel files
input_folder = Path("./data/combined")
output_folder = Path("./data/output")
output_folder.mkdir(exist_ok=True, parents=True)

# Metadata storage
metadata = []

# Loop over Excel files
for excel_file in input_folder.glob("*.xlsm"):
    xls = pd.ExcelFile(excel_file)
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name, header=None)
        
        # Detect tables by blank row separation
        tables = []
        current_table = []
        
        for row in df.values:
            if all(pd.isna(row)):
                if current_table:
                    tables.append(pd.DataFrame(current_table))
                    current_table = []
            else:
                current_table.append(row)
        
        if current_table:
            tables.append(pd.DataFrame(current_table))
        
        # Save each table as CSV
        for idx, table in enumerate(tables):
            # Try to detect title in first row (optional)
            title = str(table.iloc[0,0]) if table.shape[1] > 0 else f"Table{idx+1}"
            table_data = table[1:].reset_index(drop=True)  # remove title row
            
            # Clean empty columns
            table_data = table_data.dropna(axis=1, how="all")
            
            # Create CSV filename
            safe_title = title.replace(" ", "_").replace("/", "_")
            csv_file_name = f"{excel_file.stem}_{sheet_name}_table{idx+1}_{safe_title}.csv"
            csv_path = output_folder / csv_file_name
            
            table_data.to_csv(csv_path, index=False)
            
            # Record metadata
            metadata.append({
                "source_file": excel_file.name,
                "sheet_name": sheet_name,
                "table_index": idx+1,
                "table_title": title,
                "csv_file": str(csv_path)
            })

# Save metadata
metadata_df = pd.DataFrame(metadata)
metadata_df.to_csv(output_folder / "metadata_log.csv", index=False)

print("Extraction complete! Metadata saved as metadata_log.csv")