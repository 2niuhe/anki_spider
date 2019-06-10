import requests
from bs4 import BeautifulSoup
import json
import re
from lxml import etree


HEADERS = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "\
           "Chrome/65.0.3325.181 Safari/537.36"}


page_max = 3


    
url3 = "http://book.qsbdc.com/word_list.php?book_id=1454&&tag=all&&group_id=19606&&page_id=3"
# 获取一个分组的所有单词列表
def get_group(book_id,group_id,page_max = 4):
    page_num = 1
    wordlist = list()
    words = list()
    pronons = list()
    meanings = list()
    sentenses = list()
    
    for page in range(page_max):
        page = page+1
        url = "http://book.qsbdc.com/word_list.php?book_id=" + str(book_id) + "&&tag=all&&group_id=" + str(group_id) + "&&page_id=" +  str(page)
        html = requests.get(url, headers=HEADERS).text

        selector = etree.HTML(html)
        
        words.extend(selector.xpath('//*[@class="hidden_1_1"]/text()'))
        pronons.extend(selector.xpath('//*[@class="hidden_2_1"]/text()'))
        meanings.extend(selector.xpath('//*[@class="hidden_3_1"]/text()'))
        sentenses.extend(selector.xpath('//*[@class="mytitle"]/@title'))
        
    for index,pronon in enumerate(pronons):
        if pronon == []:
            pronons[index] = ''
    temp = list()
    for index in range(len(words)):
        s = process_sentense(sentenses[index])
        wordlist.append([words[index],pronons[index],meanings[index],'',s[0],s[1],s[2],s[3],''])
    
    return wordlist
        

# 参数：未处理的例句字符串
# 返回[英文1，中文1，英文2，中文2]
def process_sentense(s):
    if not s:
        return ['','','','']
    
    zh = re.compile(u'[\u4e00-\u9fa5]')
    en = re.compile(u'[\u0061-\u007a,\u002e\u0020]')
    r_s = list()
    # 去除句首
    if len(s.split("||||")) > 1:
        s = s.split("||||")[1:]
    else:
        s = None           
    for tmp in s:
        r_s.append(zh.split(tmp)[0])
        r_s.append(en.split(tmp)[-1])
    if len(r_s) == 4:   
        return r_s
    else:
        return ['','','','']
 
    
def gen_anki(wordlist):
    wordlist = wrap_string(wordlist)
    for w in wordlist:
        print('\t'.join(w))
    

def wrap_string(wordlist):
    for i,word in enumerate(wordlist):
        for j,item in enumerate(word):
            wordlist[i][j] = "<div>" + item + "</div>"
    return wordlist
            
if __name__ == '__main__':
    book_id = 1712                                  # 修改book_id
    group_ids = range(24300,24344)                  # 修改book_id对应的group
    word_number = 0
    for group_id in group_ids:
        temp = get_group(book_id,group_id)
        gen_anki(temp)
        word_number += len(temp)
    #print(word_number)
        
