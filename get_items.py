import datetime, csv

start = datetime.datetime(2020, 4, 7)
end = datetime.datetime(2020, 5, 12)

delta = end - start

days = []
for i in range(delta.days + 1):
    days.append(str((start + datetime.timedelta(days=i)).strftime('%Y-%m-%d')))


count = 0
for date in days:
    date_csv = open('./data/'+ date +'.csv', 'r')
    date_reader = csv.reader(date_csv)
    for line in date_reader:
        if date_reader.line_num == 1:
            continue
        topic_name = line[0]
        new = len(open('./data/'+ date + '/' + topic_name + '.csv', 'r').readlines()) - 1
        count = count + new

print('一共：', count , '条微博')