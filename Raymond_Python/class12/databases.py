import psycopg2
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

# Connect to the database with the token
load_dotenv()
CONN_STR = os.getenv('TOKEN')
conn = psycopg2.connect(CONN_STR)
cursor = conn.cursor()

# Example query used in the wild
query = """
SELECT * FROM queued_payments;
"""
cursor.execute(query)
rows = cursor.fetchall()
headers = [desc[0] for desc in cursor.description]
print("Headers:", headers)

for row in rows:
    print(row)

cursor.close()
conn.close()


# # Creating a new table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS raymonds_table (
#     name TEXT NOT NULL
# );
# """)
# cursor.execute(query)
# conn.commit()
# cursor.close()
# conn.close()

# # Inserting data into the table
# word = "hello"
# cursor.execute(
#     "INSERT INTO raymonds_table (name) VALUES (?);",
#     (word,)
# )
# cursor.execute(query)
# conn.commit()
# cursor.close()
# conn.close()

# # Querying the table
# cursor.execute("SELECT * FROM raymonds_table;")
# rows = cursor.fetchall()
# headers = [desc[0] for desc in cursor.description]
# print("Headers:", headers)

# for row in rows:
#     print(row)

# cursor.close()
# conn.close()