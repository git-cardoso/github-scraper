def get_urls():
    with open("repositories.txt", "rt") as f:
        start_urls = ['https://github.com/' +
                      url.strip() + '/find/master' for url in f.readlines()]
    return start_urls
