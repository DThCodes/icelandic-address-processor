import pandas as pd

try:
    # Load the original CSV file, specifying 'HUSMERKING' and 'SVFNR' as string columns
    df = pd.read_csv('https://fasteignaskra.is/Stadfangaskra.csv', dtype={'HUSMERKING': 'str', 'SVFNR': 'str'})

    # Part A: Select the desired columns
    selected_columns_df_a = df[['SVFNR', 'POSTNR', 'HEITI_NF', 'HEITI_TGF', 'HUSMERKING']].copy()

    # Save to CSV
    selected_columns_df_a.to_csv('stadfangaskra_trimmed.csv', index=False)
    print("New CSV file 'stadfangaskra_trimmed.csv' created successfully!")

    # Part B: Select columns and modify
    selected_columns_df_b = df[['POSTNR', 'HEITI_NF', 'HEITI_TGF', 'HUSMERKING']].copy()

    # Append 'HUSMERKING' to 'HEITI_NF' and 'HEITI_TGF' only if it exists and is not empty
    selected_columns_df_b['HEITI_NF'] = selected_columns_df_b.apply(
        lambda row: f"{row['HEITI_NF']} {row['HUSMERKING']}" if pd.notna(row['HUSMERKING']) and row['HUSMERKING'] != '' else row['HEITI_NF'],
        axis=1
    )
    selected_columns_df_b['HEITI_TGF'] = selected_columns_df_b.apply(
        lambda row: f"{row['HEITI_TGF']} {row['HUSMERKING']}" if pd.notna(row['HUSMERKING']) and row['HUSMERKING'] != '' else row['HEITI_TGF'],
        axis=1
    )

    # Drop the original 'HUSMERKING' column
    selected_columns_df_b = selected_columns_df_b.drop('HUSMERKING', axis=1)

    # Remove duplicates based on 'POSTNR' and 'HEITI_NF'
    selected_columns_df_b = selected_columns_df_b.drop_duplicates(subset=['POSTNR', 'HEITI_NF'])

    # Sort by 'POSTNR' and then 'HEITI_NF'
    selected_columns_df_b = selected_columns_df_b.sort_values(by=['POSTNR', 'HEITI_NF'])

    # Save to CSV
    selected_columns_df_b.to_csv('selected_stadfangaskra-b.csv', index=False)
    print("New CSV file 'selected_stadfangaskra-b.csv' created successfully!")

except Exception as e:
    print(f"Error processing CSV: {e}")
