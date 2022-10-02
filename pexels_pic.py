'''
main website https://www.pexels.com
how to download pictures in pexels
'''

import requests

weburl ='https://www.pexels.com/zh-cn/api/v2/feed?seed=2022-10-02T14:39:12.839Z&per_page=30'

# headers should have secret-key
chrome_header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'secret-key':'H2jk9uKnhRmL6WPwh89zBezWvr'
}

response =requests.get(weburl, headers=chrome_header)

re_file = re.findall(r'"download_link":"(.*?)"' ,str(response.text))

for i in re_file:
    pic =i.split('?')[0]
    print(pic)
