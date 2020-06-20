import requests
import lxml.html


def search_text(word: str, url):
    try:
        url += word
        api = requests.get(url)

        tree = lxml.html.document_fromstring(api.text)
        text = tree.xpath('//*[@id="mw-content-text"]/div/p[1]')[0].text_content()

        return text, url

    except Exception:
        return "Sorry, I don't know this word &#128532"
