'''
data : 2018.10.06
author : 极简XksA
goal : 爬取猫眼《悲伤逆流成河》影评，词云可视化
'''

# 猫眼电影介绍url
# http://maoyan.com/films/1217236

import requests
from fake_useragent import UserAgent
import json
headers = {
        "User-Agent": UserAgent(verify_ssl=False).random,
        "Host":"m.maoyan.com",
        "Referer":"http://m.maoyan.com/movie/1217236/comments?_v_=yes"
    }
# 猫眼电影短评接口
offset = 0
# 电影是2018.9.21上映的
startTime = '2018-09-21'
comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset,startTime)
# 发送get请求
response_comment = requests.get(comment_api,headers = headers)
json_comment = response_comment.text
json_comment = json.loads(json_comment)
print(json_comment)

def get_data(self,json_comment):
    json_response = json_comment["cmts"]  # 列表
    list_info = []
    for data in json_response:
        cityName = data["cityName"]
        content = data["content"]
        if "gender" in data:
            gender = data["gender"]
        else:
            gender = 0
        nickName = data["nickName"]
        userLevel = data["userLevel"]
        score = data["score"]
        list_one = [self.time,nickName,gender,cityName,userLevel,score,content]
        list_info.append(list_one)
    self.file_do(list_info)


def file_do(list_info):
    # 获取文件大小
    file_size = os.path.getsize(r'D:\maoyan.csv')
    if file_size == 0:
        # 表头
        name = ['评论日期', '评论者昵称', '性别', '所在城市','猫眼等级','评分','评论内容']
        # 建立DataFrame对象
        file_test = pd.DataFrame(columns=name, data=list_info)
        # 数据写入
        file_test.to_csv(r'G:\maoyan.csv', encoding='gbk', index=False)
    else:
        with open(r'G:\maoyan.csv', 'a+', newline='') as file_test:
            # 追加到文件后面
            writer = csv.writer(file_test)
            # 写入文件
            writer.writerows(list_info)