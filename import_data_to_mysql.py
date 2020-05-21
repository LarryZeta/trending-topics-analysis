import datetime, csv, emoji
import mysql.connector
from time import sleep


db = mysql.connector.connect(
  host='nas',
  user='root',
  passwd='trending-data-db',
  database='trending-db',
  port='23306'
)

def get_days_between(start_str, end_str):
    def parse_ymd(date_str):
        year_str, mon_str, day_str = date_str.split('-')
        return datetime.datetime(int(year_str), int(mon_str), int(day_str))
    
    # start = datetime.datetime(2020, 4, 7)
    start_date = parse_ymd(start_str)
    # end = datetime.datetime(2020, 5, 15)
    end_date = parse_ymd(end_str)

    delta = end_date - start_date

    days = []
    for i in range(delta.days + 1):
        days.append(str((start_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d')))
    
    return days


def get_all_topics(days):
    
    topics = []
    
    for date in days:
        date_csv = open('./data/spader_row_data/'+ date +'.csv', 'r')
        date_reader = csv.reader(date_csv)
        
        for line in date_reader:
            if date_reader.line_num == 1:
                continue
            topic_name = line[0]
            trending_count = line[1]
            if trending_count == '': trending_count = None
            emotion = line[2]
            if emotion == '': emotion = None
            topic = (date, topic_name, trending_count, emotion)
            topics.append(topic)
    
    return topics


# def get_all_weibos(days):

#     weibos = []
#     topic_num = 0

#     for date in days:
#         date_csv = open('./data/spader_row_data/'+ date +'.csv', 'r')
#         date_reader = csv.reader(date_csv)
#         for line in date_reader:
#             if date_reader.line_num == 1:
#                 continue
#             topic_name = line[0]
#             topic_num = topic_num + 1
#             topic_file_csv = open('./data/'+ date + '/' + topic_name + '.csv', 'r')
#             topic_file_reader = csv.reader(topic_file_csv)
#             for weibo in topic_file_reader:
#                 if topic_file_reader.line_num == 1:
#                     continue
#                 weibo_user = weibo[0]
#                 weibo_content = emoji.demojize(weibo[1])
#                 weibo = (topic_num, weibo_user, weibo_content)
#                 weibos.append(weibo)

#     return weibos


def get_all_weibos():
    
    weibos = []
    weibo_csv = open('./data/weibos.csv', 'r')
    weibo_reader = csv.reader(weibo_csv)
    
    for line in weibo_reader:
        if weibo_reader.line_num == 1:
            continue
        weibo = (line[0], line[1], line[2])
        weibos.append(weibo)
    
    return weibos


def get_all_resaults(file_name):
    
    resaults = []
    resault_csv = open('./data/resault_data/' + file_name, 'r')
    resault_reader = csv.reader(resault_csv)

    for line in resault_reader:
        # if resault_reader.line_num == 1:
        #     continue
        sentiment_num = line[4]
        sentiment_value = line[5]
        if sentiment_num == '':
            sentiment_num = None
        if sentiment_value == '':
            sentiment_value = None
        resault = (line[0], line[3], sentiment_num, sentiment_value)
        resaults.append(resault)
    
    return resaults


def insert_topics_to_mysql(topics):

    sql = 'INSERT INTO `topics` (date, topic_name, trending_count, emotion) VALUES (%s, %s, %s, %s)'
    cursor = db.cursor()
    cursor.executemany(sql, topics)
    db.commit()
    print(cursor.rowcount, "topics was inserted.")
    return cursor.rowcount


# def insert_weibos_to_mysql(weibos):

#     sql = 'INSERT INTO `weibo` (topic_num, weibo_user, weibo_content) VALUES (%s, %s, %s)'
#     cursor = db.cursor()
#     cursor.executemany(sql, weibos)
#     db.commit()
#     print(cursor.rowcount, "weibos was inserted.")
#     return cursor.rowcount


def insert_resaults_to_mysql(resaults):

    sql = 'INSERT INTO `trending-db`.`resaults` (`topic_num`, `resault_json`, `sentiment_num`, `sentiment_value`) VALUES (%s, %s, %s, %s);'
    cursor = db.cursor()
    cursor.executemany(sql, resaults)
    db.commit()
    print(cursor.rowcount, "resaults was inserted.")
    return cursor.rowcount


def main():
    # days = get_days_between('2020-04-07', '2020-05-15')
    # resaults = get_all_resaults('weibos_res_1_40000.csv')
    resaults = get_all_resaults('weibos_res_140001_20000.csv')
    count = 0
    # weibo_csv = open('./data/weibos.csv', 'a')
    # weibo_writer = csv.writer(weibo_csv)
    # weibo_writer.writerows(weibos)
    for i in range(0, 20000, 1000):
        j = i + 1000
        count = count + insert_resaults_to_mysql(resaults[i : j])
        sleep(3)
    print(count, 'resaults was totally inserted.')

def test():
    resaults = get_all_resaults('test.csv')
    insert_resaults_to_mysql(resaults)
    
    

if __name__ == '__main__':
    main()