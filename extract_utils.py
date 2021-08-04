def extract_code_text(bs, index):
    """
    give a page/post object of beautifulsoap, extracts text and code in seperate variable.
    index:
        give 0 extracts the question and their corresponding code and text
        given 1 extracts code and text of first answer
    """
    texts = ''
    code = ''
    try:
        for a in bs.find_all('div', class_='post')[index].find_all('p'):
            texts += a.text
        for a in bs.find_all('div', class_='post')[index].find_all('code'):
            code += a.text
    except:
        pass
    return texts, code

# import requests
# from bs4 import BeautifulSoup

# post1 = "https://discuss.pytorch.org/t/how-to-check-torch-gpu-compatibility-without-initializing-cuda/128528"



# post_res = requests.get(post1)
# post_bs = BeautifulSoup(post_res.content, 'html.parser')
# post_bs.find('a', href='/t/how-to-check-torch-gpu-compatibility-without-initializing-cuda/128528').text

# post_bs.find_all('div', class_='post')[0]


# print(post_res)
