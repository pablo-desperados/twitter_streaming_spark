import psycopg2

conn = psycopg2.connect(host="localhost",port=5432,database="[YOUR DATABASE HERE]", user="YOUR USERNAME HERE", password="")

cur=conn.cursor()
sqltable = "CREATE TABLE tweets_table (id SERIAL PRIMARY KEY , hashtag_text varchar(128), count int);"

cur.execute(sqltable)
conn.commit()
