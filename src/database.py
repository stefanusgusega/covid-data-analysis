"""
This is the script to connect to the database
"""
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# Load the environment variables from .env
load_dotenv()

# Define connection variables
USERNAME = "postgres"
PASSWORD = os.getenv("DB_PASSWORD")
IP_ADDRESS = "localhost"
PORT = 5432
DB_NAME = "coviddatabase"

# Define paths
DATA_PATH = "data"

postgres_str = f"postgresql://{USERNAME}:{PASSWORD}@{IP_ADDRESS}:{PORT}/{DB_NAME}"

# Create the connection
conn = create_engine(postgres_str)

# Loading dataframes
task_1_1 = pd.read_csv(os.path.join(DATA_PATH, "task11.csv"))
task_1_2 = pd.read_csv(os.path.join(DATA_PATH, "task12.csv"))
task_1_3 = pd.read_csv(os.path.join(DATA_PATH, "task13.csv"))

# Make table from the first task to sql
task_1_1.to_sql("task_1_1", con=conn, index=False, if_exists="replace")

# Make table from the first task to sql
task_1_2.to_sql("task_1_2", con=conn, index=False, if_exists="replace")

# Make table from the first task to sql
task_1_3.to_sql("task_1_3", con=conn, index=False, if_exists="replace")
