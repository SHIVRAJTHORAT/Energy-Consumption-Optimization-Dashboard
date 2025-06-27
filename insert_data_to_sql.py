import pandas as pd
from sqlalchemy import create_engine

# Load your processed data
df = pd.read_csv("processed_energy_data.csv")

# ✅ Correct connection details
username = 'postgres'        # Your actual PostgreSQL username
password = 'Shivraj%40123'   # Replace with your PostgreSQL password
host = 'localhost'           # Usually localhost unless using remote DB
port = '5432'                # Default PostgreSQL port
database = 'energy_dashboard'        # Your database name

# ✅ Correct connection string
engine = create_engine('postgresql://postgres:Shivraj%40123@localhost:5432/energy_dashboard')

# Write data to table
df.to_sql("energy_usage", engine, if_exists="replace", index=False)

print("✅ Data successfully inserted into PostgreSQL.")
