import requests
from lxml import html, etree

def get_tree(url:str):
    r = requests.get(url).text
    return html.fromstring(r)

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
tree = get_tree("https://vk.com/nzni_net?w=wall-21093944_42669")
media = parse_media(tree)
