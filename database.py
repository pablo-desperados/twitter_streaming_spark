import psycopg2

def update_hashtag_count(payload):
conn = psycopg2.connect(host="localhost",port=5432,database="[YOUR DATABASE HERE]", user="YOUR USERNAME HERE", password="")
    cur=conn.cursor()
    for i in payload:
        value = i[0]
        count = i[1]
        cur.execute("SELECT * FROM tweets_table WHERE tweets_table.hashtag_text='"+value+"'")
        result = len(cur.fetchall())>0
        if(result):
            cur.execute("UPDATE tweets_table SET count = tweets_table.count + 1 WHERE tweets_table.hashtag_text='"+value+"'")

        else:
            cur.execute("INSERT INTO tweets_table VALUES (DEFAULT,%s,%s)",(value,count))



    conn.commit()
    conn.close()
    cur.close()
