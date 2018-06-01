from core.get_urls import get_urls
from core.get_tab_files import get_tab_files
from core.get_ascii_tree import get_ascii_tree
from core.output import output
from spiders.git_files_spider import git_files
from spiders.git_details_spider import git_details


def run_scraper():
    # Get GitHub url for project
    urls = get_urls()

    for url in urls:
        # Get links from all files
        files_links = git_files(url)
        project = str(url.split("/")[-3])

        # list tab_files - extensions | lines | bytes
        list_tab_files = []
        # list tab_dir - (dir)filename | lines
        list_tab_dir = []

        for file_link in files_links:
            item = git_details(file_link)
            list_tab_files.append(
                [item['extension'], item['lines'], item['size_bytes']])
            list_tab_dir.append([item['dir_file'], item['lines']])

        # call def - get_tab_files
        tab_files = get_tab_files(list_tab_files)
        tab_dir = get_ascii_tree(list_tab_dir, project)

        # if tab_file is empty : skip
        if tab_files.empty:
            continue

        # output results
        output(project, tab_files, tab_dir)


run_scraper()
