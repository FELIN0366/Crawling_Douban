# 安装库
import json
import requests
import time
import random
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent # 代理池


# 对html进行数据爬取
def crawl_douban_data(page):
    # # 从代理池里面获取随机账户
    # u = UserAgent()
    # user_agent = u.random
    # # headers={'user-agent':user_agent}

    # 直接使用cookie(Cookie与Referer都是直接从网页手工摘取下来的)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Referer': 'https://www.douban.com',
        #'Cookie':'ll="118281"; bid=SIszYXiRivw; __gads=ID=da1ce2c73b991004-2245c82afad10020:T=1650020954:RT=1650020954:S=ALNI_MZhDr01WcGYPooZURdLHQ8swS33Ig; viewed="10554308"; gr_user_id=9817b66c-4e0c-4285-ace3-687bdfabf979; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; ct=y; __gpi=UID=00000606dc6a1a9a:T=1653963522:RT=1654324743:S=ALNI_MZKZREA-CFw4WDg6OZQurHlsFPhEg; ap_v=0,6.0; __utmz=30149280.1654563597.13.7.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=30149280; __utma=30149280.1999213187.1650020952.1654563597.1654567266.14; dbcl2="183479190:p1TVpdAX/gs"; ck=YvqG; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1654567306%2C%22https%3A%2F%2Fmovie.douban.com%2F%22%5D; _pk_id.100001.8cb4=2d4f9bbfae4608c5.1650784641.9.1654567306.1654563597.; _pk_ses.100001.8cb4=*; __utmt=1; __utmv=30149280.18347; __utmb=30149280.2.10.1654567266'
        #阙阙的：'Cookie':'ll="118281"; bid=qnHe6DyJS10; viewed="2355626"; gr_user_id=32bf20dc-14cd-4c80-9461-4714b5c869c4; __gads=ID=952584a9d8188ec0-2216aa102fd3008d:T=1652530581:RT=1652530581:S=ALNI_MZDOD9tSwUTi0bFgdG5ZVx0jdcQyw; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1654591193%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1884767538.1652530554.1652530554.1654591194.2; __utmc=30149280; __utmz=30149280.1654591194.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; dbcl2="254246445:+NvGR/uO10w"; ck=53Mk; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25424; _pk_id.100001.8cb4=ca47dccc7f7aadb6.1652530553.2.1654591236.1652530569.; __utmb=30149280.7.10.1654591194'
        #马马的'Cookie': 'bid=Aew2bgAIBSQ; ll="118281"; _pk_ses.100001.8cb4=*; __utma=30149280.1137699068.1654564671.1654564671.1654564671.1; __utmc=30149280; __utmz=30149280.1654564671.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; dbcl2="257741514:+Exd5uoCPeg"; ck=2cC1; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25774; _pk_id.100001.8cb4=b0e50f15f8a4ea95.1654564669.1.1654564800.1654564669.; __utmb=30149280.11.10.1654564671'
        #小欧的'Cookie':'ll="118281"; bid=SIszYXiRivw; __gads=ID=da1ce2c73b991004-2245c82afad10020:T=1650020954:RT=1650020954:S=ALNI_MZhDr01WcGYPooZURdLHQ8swS33Ig; viewed="10554308"; gr_user_id=9817b66c-4e0c-4285-ace3-687bdfabf979; douban-fav-remind=1; push_doumail_num=0; push_noty_num=0; ct=y; __utmz=30149280.1654323910.7.6.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __gpi=UID=00000606dc6a1a9a:T=1653963522:RT=1654324743:S=ALNI_MZKZREA-CFw4WDg6OZQurHlsFPhEg; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1654485993%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.1999213187.1650020952.1654413787.1654485993.12; __utmc=30149280; dbcl2="210301196:U0XbMHxSp10"; ck=pekg; __utmv=30149280.21030; __utmt=1; _pk_id.100001.8cb4=2d4f9bbfae4608c5.1650784641.7.1654487528.1654324737.; __utmb=30149280.18.10.1654485993'
    }


    crawl_url = 'https://movie.douban.com/subject/30444960/reviews?start=' + str(page)

    try:
        res = requests.get(url=crawl_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        print(soup)
        divs = soup.find_all("div", class_="review-list")
        return divs

    except Exception as e:
        print("运行失败！")

# 解析爬取出来的信息
def parse_douban_data(comments):
    cm = BeautifulSoup(str(comments), 'html.parser')

    all_divs = cm.find_all('div', attrs={'data-cid': True})

    remarks = []
    for div in all_divs:
        remark = {}

        # head层有name、星级、发布时间
        head = div.find('header', class_="main-hd")
        if head.find('a', class_='name'):
            remark['name'] = head.find('a', class_='name').text
        if head.find('span', title=True):
            answer = head.find('span')
            remark['star'] = answer['title']
        else:
            continue
        if head.find('span', class_="main-meta"):
            remark['time'] = head.find('span', class_="main-meta").get('content')

        # body层有review
        body = div.find('div', class_='main-bd')
        if body.find('div', class_='short-content'):
            review = body.find('div', class_='short-content').text
            pp = review.replace('"', '!').replace("'", '!')
            remark["review"] = pp

        remarks.append(remark)
    return remarks

# 爬取并解析数据
data=[]
# for i in range(0,3020,20):
for i in range(0,2):
    # 获取每一页的评论
    comments=crawl_douban_data(i)
    print(len(comments))
    # 处理每一页的评论
    data=data+parse_douban_data(comments)
    # 保存文件成json格式
    json_data = json.loads(str(data).replace("'", '"').replace("\\", ""))
    # 将文件存储到work目录下
    # with open('remarks'+str(i)+'.json', 'w', encoding='UTF-8') as f:
    #     json.dump(json_data, f, ensure_ascii=False)
    # 查看完进度
    print("已完成第",i,"条评论的提取！")
    # 休眠
    x=random.randint(5,10)
    time.sleep(x)





