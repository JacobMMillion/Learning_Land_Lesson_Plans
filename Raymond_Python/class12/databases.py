import psycopg2
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

# CONNECT TO THE DATABASE
load_dotenv()
CONN_STR = os.getenv('TOKEN')
conn = psycopg2.connect(CONN_STR)
cursor = conn.cursor()
# DONE CONNECTING, READY TO GO



# # Creating a new table
# query = """
# CREATE TABLE IF NOT EXISTS words (
#     word TEXT NOT NULL
# );
# """
# cursor.execute(query)
# conn.commit()
# cursor.close()
# conn.close()

# # Inserting data into the table
# word = "waterbottle"
# cursor.execute(
#     "INSERT INTO words (word) VALUES (%s);",
#     (word,)
# )
# conn.commit()
# cursor.close()
# conn.close()

# # Querying the table
# cursor.execute("SELECT * FROM words;")
# rows = cursor.fetchall()
# headers = [desc[0] for desc in cursor.description]
# print(headers)

# for row in rows:
#     print(row)

# cursor.close()
# conn.close()

# # 5) Dropping the table
# cursor = conn.cursor()
# cursor.execute("""
# DROP TABLE IF EXISTS raymonds_table;
# """)
# conn.commit()
# cursor.close()
# conn.close()