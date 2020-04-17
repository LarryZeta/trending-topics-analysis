import get_topic_contents, csv, random
from time import sleep

date = '2020-04-16'
csvFile = open('./data/'+ date +'.csv', 'r')
reader = csv.reader(csvFile)

for item in reader:
    if reader.line_num == 1:
        continue
    get_topic_contents.get_topic_contents(item[0], item[1], date)
    sleep(random.randint(6, 10))