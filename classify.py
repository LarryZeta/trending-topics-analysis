import pandas as pd

type_list = ['新冠肺炎', '游戏', '娱乐圈', '体育', '时政', '经济', '社会', '军事', '生活', '科技']

test = pd.read_csv('./data/2020-04-07.csv')
print(test)