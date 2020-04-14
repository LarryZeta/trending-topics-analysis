import get_topic_contents, csv, random
from time import sleep


csvFile = open('./data/2020-04-13.csv', 'r')
reader = csv.reader(csvFile)

for item in reader:
    if reader.line_num == 1:
        continue
    get_topic_contents.get_topic_contents(item[0], item[1])
    sleep(random.randint(6, 10))