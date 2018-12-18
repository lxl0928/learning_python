#! /usr/bin/eny python3
# coding: utf-8 

import re
import requests
import http.cookiejar
from PIL import Image
import time, json,threading
from bs4 import BeautifulSoup
import mysql.connector

# 提交头数据
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
    "Referer": "http://www.zhihu.com/",
    'Host': 'www.zhihu.com',
}
# 保存cookie的文件名
filename = 'cookie'
# 建立一个session
session = requests.Session()
# 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
session.cookies = http.cookiejar.LWPCookieJar(filename)


# 登陆
def login():
    # 第一次需要输入自己的账号密码
    username = input('输入账号：')
    password = input('输入密码：')

    # 有@符号为邮箱登陆
    if "@" in username:
        print('使用邮箱登录中...')
        url = 'https://www.zhihu.com/login/email'
        data = {'_xsrf': get_xsrf(),
                'password': password,
                'remember_me': 'true',
                'email': username
                }
    else:
        print('使用手机登录中...')
        url = 'http://www.zhihu.com/login/phone_num'
        data = {'_xsrf': get_xsrf(),
                'password': password,
                'remember_me': 'true',
                'phone_num': username
                }
    # 若不用验证码，直接登录
    try:
        result = session.post(url, data=data, headers=headers)
        print((json.loads(result.text))['msg'])
    # 要用验证码，post后登录
    except:
        data['captcha'] = get_captcha()
        result = session.post(url, data=data, headers=headers)
        print((json.loads(result.text))['msg'])
    # 保存cookie到本地
    session.cookies.save(ignore_discard=True, ignore_expires=True)


# 判断是否登陆，后面灭有用到，但是舍不得删掉
def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, allow_redirects=False).status_code
    if int(x=login_code) == 200:
        return True
    else:
        return False


# 获取xsrf
def get_xsrf():
    response = session.get('https://www.zhihu.com', headers=headers)
    html = response.text
    get_xsrf_pattern = re.compile(r'<input type="hidden" name="_xsrf" value="(.*?)"')
    _xsrf = re.findall(get_xsrf_pattern, html)[0]
    return _xsrf


# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    response = session.get(captcha_url, headers=headers)
    with open('cptcha.gif', 'wb') as f:
        f.write(response.content)
    im = Image.open('cptcha.gif')
    im.show()
    captcha = input('请输入验证码： ')
    return captcha


# 获取用户基本信息
def get_userInfo(userID):
    user_url = 'https://www.zhihu.com/people/' + userID
    response = session.get(user_url, headers=headers)

    # 由于我在window上编程所以只能用html5lib，有钱了去买了个mac
    soup = BeautifulSoup(response.content, 'html5lib')
    # 打印出页面
    # with open('zhihuprifile.html', 'wb') as f:
    #     f.write(response.content)

    d = {}
    # userId = soup.find("a",class_="Tabs-link")["href"].split("/")[2]
    d['userId'] = userID

    try:
        nickname = soup.find_all('span', {'class': 'ProfileHeader-name'})[0].string
    except:
        nickname = "None"
    d['nickname'] = nickname

    try:
        word = soup.find('span', class_="RichText ProfileHeader-headline").string
        if word == None:
            word = 'None'
    except:
        word = "None"
    d['word'] = word

    try:
        business = soup.find_all('div', {'class': 'ProfileHeader-iconWrapper'})[0].next_sibling
        if business == None:
            business = 'None'
    except:
        business = 'None'
    d['business'] = business

    try:
        company = soup.find_all('div', {'class': 'ProfileHeader-divider'})[0].next_sibling
        if company == None:
            company = 'None'
    except:
        company = 'None'
    d['company'] = company

    try:
        location = soup.find_all('div', {'class': 'ProfileHeader-divider'})[1].next_sibling
        if location == None:
            location = 'None'
    except:
        location = "None"
    d['location'] = location

    try:
        school = soup.find_all('div', {'class': 'ProfileHeader-iconWrapper'})[1].next_sibling
        if school == None:
            school = 'None'
    except:
        school = 'None'
    d['school'] = school

    try:
        subject = soup.find_all('div', {'class': 'ProfileHeader-divider'})[2].next_sibling
        if subject == None:
            subject = 'None'
    except:
        subject = 'None'
    d['subject'] = subject

    try:
        # 分割错误说明没有“回答”，会报错
        answers = soup.find('div', {'class': 'IconGraf-iconWrapper'}).next_sibling.split(' ')[1]
    except:
        answers = None
    if answers == None:
        answers = 0
    d['answers'] = answers

    try:
         followees = soup.find_all('div', {'class': 'Profile-followStatusValue'})[0].string
    except:
        followees = None
    if followees == None:
        followees = 0
    # print('followees: %s' % followees)
    d['followees'] = followees

    try:
        followers = soup.find_all('div', {'class': 'Profile-followStatusValue'})[1].string
    except:
        followers = None
    if followers == None:
        followers = 0
    d['followers'] = followers

    return d


# 获取关注者的主页url，只获取前三个
def followeesUrl(userId):
    user_url = 'https://www.zhihu.com/people/' + userId + "/following"
    response = session.get(user_url, headers=headers)

    # 由于我在windows上编程所以只能用html5lib，有钱了去买了个mac
    soup = BeautifulSoup(response.content, 'html5lib')
    # with open('following.html', 'wb') as f:
    #     f.write(response.content)
    urls = soup.find_all("div", {'aria-haspopup': "true"})

    # 保存url，去掉重复的
    urllist = set([])
    for url in urls:
        urllist.add(url.a["href"])

    # 拼接为字符串返回
    saveUrl = ''
    for u in urllist:
        if saveUrl != '':
            saveUrl = saveUrl + "," + u
        else:
            saveUrl = u
    return saveUrl


# ----------------------------------------------------------------以下为数据库操作------------------------------------------------------------------------------
# 数据库链接信息,填入自己的数据库信息
conn = mysql.connector.connect(host='localhost', user='****', password='****', database='zhihu')


# 存取数据到数据库
def saveInfo(info):
    cursor = conn.cursor()
    data = [str(info.get("userId")), str(info.get("nickname")), str(info.get("word")), str(info.get("business")),
            str(info.get("company")), str(info.get("location")), str(info.get("school")), str(info.get("subject")),
            int(info.get("answers")), int(info.get("followers")), int(info.get("followees")), info.get("f_url")]
    try:
        cursor.execute(
            "insert into zhihu(userId,nickname,word,business,company,location,school, subject,answers,followers,followees,f_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            data)
    except:
        pass

    conn.commit()
    cursor.close()


# 修改状态，1表示已经查询过
def changeSate(userId):
    cursor = conn.cursor()
    # sql = "updata zhihu set flag = 1 where userId = " + userId
    # cursor.execute(sql)
    data = [userId]
    cursor.execute("update zhihu set flag = 1 where userId = %s", data)
    conn.commit()
    cursor.close()


# 查询url
def selectOneUrl(c):
    c.send(None)
    cursor = conn.cursor()
    flag = [0, ]
    while True:
        # 查询出一条未爬取的数据即可
        cursor.execute("select userId,f_url from zhihu where flag = %s limit 1", flag)
        data = cursor.fetchall()
        userId = data[0][0]
        url = data[0][1]
        urlList = []
        for u in url.split(","):
            urlList.append(u)
        s = SelectClass(userId, urlList)
        #送为消费者
        date = c.send(s)
    #关闭协程
    c.close()
    conn.commit()
    cursor.close()

#------------------------------以下为具体操作方法------------------------------------------------

def threadingExecution(urltemp):

    userId = urltemp.get_userId()
    urls = urltemp.get_urlList()
    if urls != None and urls != '':
        for u in urls:
            try:
                id = u.split("/")[2]
            except:
                continue

            info = get_userInfo(id)

            nickname = info['nickname']

            if nickname == 'None':
                continue
            print(nickname)

            info['f_url'] = followeesUrl(info['userId'])
            saveInfo(info)
            # 睡5秒后再请求，我怕请求太快，被限制
            time.sleep(5)
    # 改变数据状态
    changeSate(userId)

# 批量获取信息
def selectMessage():
    date = None
    while True:
        # 开始运行时间
        start = time.time()
        # 从数据库中查询没有被爬取的数据
        urltemp =  None
        try:
            # 获取数据
            urltemp = yield date

        except:
            print("用户查询完毕")
        t = threading.Thread(target=threadingExecution(urltemp),args=(urltemp))
        t.setDaemon(True)
        t.start()
        t.join(30)

        # 结束时间
        end = time.time()
        # 超时退出函数
        if (end - start) > 29:
            break
            # 退出函数



#超时后重新启动，感觉递归太耗资源，可以换其他方式来做
def execution():

    c = selectMessage()
    selectOneUrl(c)

    #睡三分钟，会不会太久了
    time.sleep(180)
    #再次登陆后重连
    session.cookies.load(filename=filename, ignore_discard=True)
    execution()


# 存放从数据库中查询出来的信息
class SelectClass:
    def __init__(self, userId, urlList):
        self.__userId = userId
        self.__urlList = urlList

    def get_userId(self):
        return self.__userId

    def get_urlList(self):
        return self.__urlList

    def set_userId(self, userId):
        self.__userId = userId

    def set_urlList(self, urlList):
        self.__urlList = urlList


# -----------------------主方法------------------------------------
if __name__ == '__main__':
    #-----------------------插入一条数据----------------------------------
    #初始id，根据这个id开始爬取,从yunshu大神开始爬取，233
    userId= 'yunshu'
    try:
        #如果有cookie保存，用cookie登陆
        session.cookies.load(filename=filename, ignore_discard=True)
    except:
        #正常流程登陆
        login()
    #获取用户基本信息
    info = get_userInfo(userId)
    #获取关注的人的url
    info['f_url'] = followeesUrl(userId)
        #插入数据库
    saveInfo(info)
    #------------------------数据库有一条数据后开始批量爬取---------------------------------
    #数据库有数据后开始批量爬取

    execution()
