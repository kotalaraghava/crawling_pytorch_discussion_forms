from bs4 import BeautifulSoup
import requests
from extract_utils import extract_code_text

website_url = "https://discuss.pytorch.org/"
res = requests.get(website_url)

bs = BeautifulSoup(res.content,  'html.parser')

#contains all categories
categories = []
for a in bs.find_all(class_='category'):
    a_res = a.find('a', href=True)
    if a_res:
        categories.append(a_res['href'])


for cat in categories:
    cat_url = f"{website_url}{cat}"
    cat_res = requests.get(cat_url)
    cat_bs = BeautifulSoup(cat_res.content, 'html.parser')
    print(cat_bs)
    #extracting links in the category page and looping over each one
    for a in cat_bs.find_all('a', class_='title raw-link raw-topic-link'):
        ques_url = a['href']
        que_res = requests.get(ques_url)
        que_bs = BeautifulSoup(que_res.content, 'html.parser')
        title = ques_url.split('/')[-2]
        que_text, que_code = extract_code_text(que_bs, 0)
        ans_text, ans_code = extract_code_text(que_bs, 1)
        print(que_bs, que_text, que_code, ans_text, ans_code)
        break
    break

print('pass')