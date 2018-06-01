import requests
from lxml import html
from settings import SPLASH_URL


def git_files(url):
    page = requests.get(SPLASH_URL,
                        params={'url': url, 'wait': 0.5})

    response = html.fromstring(page.content)
    links = response.xpath(
        '//a[contains(@class, "css-truncate-target js-navigation-open js-tree-finder-path")]/@href')

    links_list = []
    for link in filter(lambda x: 'https' in x, links):
        links_list.append(link)
    return links_list
