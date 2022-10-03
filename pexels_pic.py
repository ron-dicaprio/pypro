'''
main website https://www.pexels.com
how to download pictures in pexels
'''

#-*- coding:utf-8 -*-
import requests, re

# get filename from url
def get_image_name(url):
    pattern = re.search("([|.|\w|\s|-])*?.(jpg|gif|png|jpeg)", url)
    if not pattern:
        return
    image_name = pattern.group()
    return image_name

weburl ='https://www.pexels.com/zh-cn/api/v2/feed?seed=2022-10-02T14:39:12.839Z&per_page=30'

# secret-key should in headers
chrome_header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'secret-key':'H2jk9uKnhRmL6WPwh89zBezWvr'
    }

response =requests.get(weburl, headers=chrome_header,allow_redirects=True)

re_file = re.findall(r'"download_link":"(.*?)"' ,str(response.text))

#print(type(re_file))
for i in re_file:
    
    pic =i.split('?')[0]
    if '.jpeg' in i:
        print(pic)
        ress = requests.get(pic,headers=chrome_header)
        with open(get_image_name(pic),'ab+') as file:
            file.write(ress.content)
            exit(-1)
