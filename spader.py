import get_topic_contents, csv, random, yaml, datetime
from time import sleep

date = datetime.date.today().strftime('%Y-%m-%d')
# days = ['2020-04-20']
days = [date]

for date in days:
    cookies = {}
    with open('./config.yml', 'r') as config_file:
        config = yaml.load(config_file.read(), Loader=yaml.SafeLoader)
        cookie_str = config['cookies']
        
        for line in cookie_str.split(';'):
            key, value = line.strip().split('=', 1)
            cookies[key] = value
    
    csv_file = open('./data/' + date + '.csv', 'r')
    reader = csv.reader(csv_file)
    
    for item in reader:
        if reader.line_num == 1:
            continue
        get_topic_contents.get_topic_contents(item[0], date, cookies)
        sleep(random.randint(6, 10))
