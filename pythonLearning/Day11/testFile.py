import time
# import requests
import json
def getHead():
    pass
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])

def main():
    pass
    mydict = {
        "name": 'wb',
        "age": 38,
        "qq": 957658,
        "friends": ['王大锤', '白元芳'],
        "cars": [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')
    # getHead()

if __name__ == '__main__':
    main()