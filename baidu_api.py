import requests
from bs4 import BeautifulSoup
import hashlib
import random
from pprint import pprint

appid = '20190514000297546'
secretKey = 'vWpJ3A1JwWe9TFXBjLDl'

url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


# def get_word():
#     with open('from_lang.txt', encoding='utf-8') as f:
#         word = f.read()
#     word = word.replace('\n', '')
#     word = word.replace(' ', '')
#     return word


def translate():
    flag = 0
    while(1):
        if flag == 1:
            select = input('是否继续翻译？\n继续翻译请按"y",退出请按"N"\n')
            if select == 'y' or select == 'Y':
                pass
            elif select == 'n' or select == 'N':
                print('欢迎下次使用\n')
                return 0
            else:
                print('输入错误\n')
                return 0

        flag = 1
        q = input('请输入要翻译的内容\n>>>')
        fromlang = 'auto'
        print('auto:自动检测  zh:中文  en:英语  yue:粤语  wyw:文言文\n\
            jp:日语  kor:韩语  fra:法语  spa:西班牙语  th:泰语  ara:阿拉伯语\n\
            ru:俄语  pt:葡萄牙语  de:德语  it:意大利语  el:希腊语  nl:荷兰语\n\
            pl:波兰语  bul:保加利亚语  est:爱沙尼亚语  dan:丹麦语  fin:芬兰语\n\
            cs:捷克语  rom:罗马尼亚语  slo:斯洛文尼亚语  swe:瑞典语  hu:匈牙利语\n\
            cht:繁体中文  vie:越南语\n')
        tolang = input('请选择翻译成什么语言\n>>>')

        salt = random.randint(32768, 65536)  # 生成一个随机数
        sign = appid + q + str(salt) + secretKey
        md = hashlib.md5()
        md.update(sign.encode('utf-8'))
        sign = md.hexdigest()

        data = {
            'appid': appid,
            'q': q,
            'from': fromlang,
            'to': tolang,
            'salt': str(salt),
            'sign': sign,
        }

        html = requests.get(url, params=data)
        html = html.json()
        dst = html['trans_result'][0]['dst']
        print(dst)
        return dst


# def return_word(dst):
#     with open('to_lang.txt', encoding='utf-8') as f:
#         f.write(dst)


def main():
    translate()


if __name__ == "__main__":
    main()
