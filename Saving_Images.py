import requests
from lxml import html, etree

def get_tree(url:str):
    r = requests.get(url)
    status = r.status_code
    text = r.text
    if status == 200:
        return html.fromstring(text)
    else:
        return False

def parse_text(html):
    text = html.xpath('//div[@class = "pi_text"]')[0]
    text = etree.tounicode(text)
    if ('<br/>' in text):
        text = text.replace('<br/>', '\n')
    return text[21:-11]

def parse_media(html):
    media = html.xpath('//a[@class = "thumb_map thumb_map_wide thumb_map_l al_photo"]')
    for a in media:
        a = etree.tounicode(a)
        yield a

def parse_author(html):
    author = html.xpath('//a[@class = "user"]')
    if(len(author) != 0):
        return author[0].text_content()
    else:
        pass
post_number = 42000
counter = 0
while post_number != 42857:
    link = f"https://vk.com/nzni_net?w=wall-21093944_{post_number}"
    tree = get_tree(link)
    if (tree == "False"):
        print("No Response from %s"%(link))
    author = parse_author(tree)
    print(author)
    if(author == "Денис Дудушкин"): counter+= 1
    post_number+= 1
    print(post_number)

#комментарий для теста atom git gui
#username test 

#комментарий для теста atom git gui 

#133 Слава Карелин
#62 Денис Дудушкин
