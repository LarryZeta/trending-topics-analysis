import datetime, csv
import mysql.connector

db = mysql.connector.connect(
  host='nas',
  user='root',
  passwd='trending-data-db',
  database='trending-db',
  port='23306'
)

sql = "SELECT * FROM `trending-db`.`topics`"
cursor = db.cursor()

cursor.execute(sql)
# db.commit()
resaults = cursor.fetchall()

topics = []
for r in resaults:
    # print(r)
    topic_num = r[0]
    date = r[1].strftime('%Y-%m-%d')
    topic_name = r[2].decode('utf8')
    trending_count = r[3]
    weibo_num = r[4]
    emotion = None
    if r[5]:
        emotion = r[5].decode('utf8')
    tag_num = r[6]
    ncov = r[7]
    topic = (topic_num, date, topic_name, trending_count, weibo_num, emotion, tag_num,ncov)
    topics.append(topic)

# print(topics)
# with open('./data/topics.csv', 'a') as topic_csv:
#     topic_writer = csv.writer(topic_csv)
#     topic_writer.writerows(topics)
