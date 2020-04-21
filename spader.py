import get_topic_contents, csv, random
from time import sleep

days = []

for date in days:
    csvFile = open('./data/'+ date +'.csv', 'r')
    reader = csv.reader(csvFile)

    for item in reader:
        if reader.line_num == 1:
            continue
        get_topic_contents.get_topic_contents(item[0], date)
        sleep(random.randint(6, 10))