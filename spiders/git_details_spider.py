import requests
from lxml import html
from settings import SPLASH_URL
from core.normalize_itens import normalize_lines, normalize_size, normalize_extension


def git_details(url):
    page = requests.get(url)
    response = html.fromstring(page.content)

    item = {}
    item['dir_file'] = url.split('master/')[-1]
    item['extension'] = normalize_extension(item['dir_file'])
    # response list with lines and file size
    response_list = response.xpath('//div[@class="file-info"]/text()')
    item['lines'] = normalize_lines(response_list)
    item['size_bytes'] = normalize_size(response_list[-1])

    return item
