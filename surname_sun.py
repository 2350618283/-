import requests
import parsel
import csv
url = 'https://cs.lianjia.com/ershoufang/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 '
                      'Safari/537.36 '
    }
response = requests.get(url=url, headers=headers)
print(response.text)
selector = parsel.Selector(response.text)
lis = selector.css('.sellListContent li')
for li in lis:
    # 标题
    title = li.css('.title a::text').get()
    # 地址
    positionInfo = li.css('.positionInfo a::text').getall()

    community = ''
    address = ''
    if len(positionInfo):
        # 小区
        community = positionInfo[0]
        # 地名
        address = positionInfo[1]
    # 房子基本信息
    houseInfo = li.css('.houseInfo::text').get()
    # 房价
    print('数据类型:', type(li.css('.totalPrice span::text').get()))
    txt = li.css('.totalPrice span::text').get()
    Price = ''
    if isinstance(txt, str):
        Price = li.css('.totalPrice span::text').get() + '万'
    # 单价
    print('单价数据类型:', type(li.css('.unitPrice span::text').get()))
    txt = li.css('.unitPrice span::text').get()
    unitPrice = ''
    if isinstance(txt, str):
        unitPrice = li.css('.unitPrice span::text').get().replace('单价', '')
    # 发布信息
    followInfo = li.css('.followInfo::text').get()
    dit = {
        '标题': title,
        '小区': community,
        '地名': address,
        '房子基本信息': houseInfo,
        '房价': Price,
        '单价': unitPrice,
        '发布信息': followInfo,
    }
    print(dit)
# 创建文件
f = open('长沙二手房数据.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '小区', '地名', '房子基本信息',
                                           '房价', '单价', '发布信息'])
# 写入表头
csv_writer.writeheader()
'''
'''
def downloadLianjia(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 '
                      'Safari/537.36 '
    }
csv_writer.writerow(dit)
for page in range(1, 101):
    url = 'https://cs.lianjia.com/ershoufang/'
    downloadLianjia(url)



    response = requests.get(url=url, headers=headers)
    print(response.text)

    selector = parsel.Selector(response.text)
    lis = selector.css('.sellListContent li')
    for li in lis:
        # 标题
        title = li.css('.title a::text').get()
        # 地址
        positionInfo = li.css('.positionInfo a::text').getall()

        community = ''
        address = ''
        if len(positionInfo):
            # 小区
            community = positionInfo[0]
            # 地名
            address = positionInfo[1]
        # 房子基本信息
        houseInfo = li.css('.houseInfo::text').get()
        # 房价
        print('数据类型:', type(li.css('.totalPrice span::text').get()))
        txt = li.css('.totalPrice span::text').get()
        Price = ''
        if isinstance(txt, str):
            Price = li.css('.totalPrice span::text').get() + '万'
        # 单价
        print('单价数据类型:', type(li.css('.unitPrice span::text').get()))
        txt = li.css('.unitPrice span::text').get()
        unitPrice = ''
        if isinstance(txt, str):
            unitPrice = li.css('.unitPrice span::text').get().replace('单价', '')
        # 发布信息
        followInfo = li.css('.followInfo::text').get()
        dit = {
            '标题': title,
            '小区': community,
            '地名': address,
            '房子基本信息': houseInfo,
            '房价': Price,
            '单价': unitPrice,
            '发布信息': followInfo,
        }
        print(dit)

        # 创建文件
        f = open('长沙二手房数据.csv', mode='a', encoding='utf-8', newline='')
        csv_writer = csv.DictWriter(f, fieldnames=['标题', '小区', '地名', '房子基本信息',
                                                   '房价', '单价', '发布信息'])
        # 写入表头
        csv_writer.writeheader()
        '''
        '''
        csv_writer.writerow(dit)