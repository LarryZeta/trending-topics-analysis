import datetime, csv

start = datetime.datetime(2020, 4, 7)
end = datetime.datetime(2020, 5, 13)

delta = end - start

days = []
for i in range(delta.days + 1):
    days.append(str((start + datetime.timedelta(days=i)).strftime('%Y-%m-%d')))

topic_num = 0
weibo_num = 0

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

print('共：', topic_num , '条热搜，', weibo_num , '条微博')