import csv

date = '2020-05-07'
date_csv = open('./data/'+ date +'.csv', 'r')
date_reader = csv.reader(date_csv)

for line in date_reader:
    if date_reader.line_num == 1:
            continue
    topic_name = line[0]
    print ('打开: ' + topic_name)
    topic_csv = open('./data/'+ date + '/' + topic_name + '.csv', 'r')
    topic_reader = csv.reader(topic_csv)
    # result_csv = open('./data/'+ date + '/' + topic_name + '_res.csv', 'a')
    # result_writer = csv.writer(result_csv)
    for wb in topic_reader:
        if topic_reader.line_num == 1:
            continue
        print(wb)
        input()