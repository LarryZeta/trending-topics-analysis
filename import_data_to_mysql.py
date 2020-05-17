import datetime, csv
import mysql.connector


db = mysql.connector.connect(
  host='nas',
  user='root',
  passwd='trending-data-db',
  database='trending-db',
  port='23306'
)

sql = 'INSERT INTO topics (date, topic_name, trending_count, emotion) VALUES (%s, %s, %s, %s)'
cursor = db.cursor()
vals = []
# val = ('2020-04-24', '中国航天日', None, None)
# cursor.execute(sql, val)
# db.commit()

# start = datetime.datetime(2020, 4, 7)
# end = datetime.datetime(2020, 5, 13)

# delta = end - start

days = ['2020-05-15']
# for i in range(delta.days + 1):
#     days.append(str((start + datetime.timedelta(days=i)).strftime('%Y-%m-%d')))

for date in days:
    date_csv = open('./data/'+ date +'.csv', 'r')
    date_reader = csv.reader(date_csv)
    for line in date_reader:
        if date_reader.line_num == 1:
            continue
        topic_name = line[0]
        trending_count = line[1]
        if trending_count == '': trending_count = None
        emotion = line[2]
        if emotion == '': emotion = None
        val = (date, topic_name, trending_count, emotion)
        vals.append(val)

cursor.executemany(sql, vals)
db.commit()
print(cursor.rowcount, "was inserted.")

