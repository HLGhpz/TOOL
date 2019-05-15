import requests
from bs4 import BeautifulSoup
import hashlib
import random
from pprint import pprint
from googletrans import Translator

appid = '20190514000297546'
secretKey = 'vWpJ3A1JwWe9TFXBjLDl'

url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


def get_word():
    with open('lang\\from_lang.txt', encoding='utf-8-sig') as f:
        word = f.read()
    word = word.replace('\n', '')
    word = word.replace(' ', '')
    with open('lang\\result.txt', 'w+') as f:
        f.write('原文:\n' + word + '\n')
    # pprint(word)
    return word


def translate_baidu(word, to_lang):
    api = 'baidu'
    q = word
    # pprint(q)
    fromlang = 'auto'

    salt = random.randint(32768, 65536)  # 生成一个随机数
    sign = appid + q + str(salt) + secretKey
    md = hashlib.md5()
    md.update(sign.encode('utf-8'))
    sign = md.hexdigest()

    data = {
        'appid': appid,
        'q': q,
        'from': fromlang,
        'to': to_lang,
        'salt': str(salt),
        'sign': sign,
    }

    html = requests.get(url, params=data)
    html = html.json()
    # pprint(html)
    result = html['trans_result'][0]['dst']
    return_word(result, to_lang, api)
    return result


def translate_google(word, to_lang):
    api = 'google'
    if to_lang == 'zh':
        dest = 'zh-cn'
    elif to_lang == 'jp':
        dest = 'ja'
    elif to_lang == 'kor':
        dest = 'ko'
    elif to_lang == 'fra':
        dest = 'fr'
    elif to_lang == 'spa':
        dest = 'es'
    elif to_lang == 'ara':
        dest = 'ar'
    elif to_lang == 'vie':
        dest = 'vi'
    else:
        dest = to_lang
    translator = Translator()
    result = translator.translate(word, dest=dest).text
    return_word(result, to_lang, api)
    return result


def return_word(result, to_lang, api):
    if to_lang == 'zh':
        # print(1)
        with open('lang\\result.txt', 'a+') as f:
            f.write('\n' + api + '译文:\n' + result + '\n')
    # print(dst)
    else:
        with open('lang\\to_lang.txt', 'a+') as f:
            f.write('\n'+ api + '百度：\n' + result + '\n')


def main():
    print('auto:自动检测  zh:中文  en:英语  jp:日语  kor:韩语\n\
        fra:法语  spa:西班牙语  th:泰语  ara:阿拉伯语  ru:俄语\n\
        pt:葡萄牙语  de:德语  it:意大利语 vie:越南语\n')
    to_lang = input("请问要翻译成什么语言")
    word = get_word()
    translate_to_baidu = translate_baidu(word, to_lang)
    translate_to_google = translate_google(word, to_lang)

    translate_back_baidu = translate_baidu(translate_to_baidu, 'zh')
    translate_back_google = translate_google(translate_to_google, 'zh')


if __name__ == "__main__":
    main()
