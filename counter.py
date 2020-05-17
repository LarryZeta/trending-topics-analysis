import datetime, csv
import mysql.connector

start = datetime.datetime(2020, 4, 7)
end = datetime.datetime(2020, 5, 15)

delta = end - start

days = []
for i in range(delta.days + 1):
    days.append(str((start + datetime.timedelta(days=i)).strftime('%Y-%m-%d')))

topic_num = 0
weibo_num = 0

db = mysql.connector.connect(
  host='nas',
  user='root',
  passwd='trending-data-db',
  database='trending-db',
  port='23306'
)

sql = "UPDATE `trending-db`.`topics` SET `weibo_num`=%s WHERE `topic_name`=%s "
cursor = db.cursor()

for date in days:
    date_csv = open('./data/'+ date +'.csv', 'r')
    date_reader = csv.reader(date_csv)
    for line in date_reader:
        if date_reader.line_num == 1:
            continue
        topic_name = line[0]
        topic_num = topic_num + 1
        new_topic_num = len(open('./data/'+ date + '/' + topic_name + '.csv', 'r').readlines()) - 1
        weibo_num = weibo_num + new_topic_num
        # val = (new_topic_num, topic_name)
        # cursor.execute(sql, val)

# db.commit()
# print(cursor.rowcount, "record updated.")


print('共：', topic_num , '条热搜，', weibo_num , '条微博')