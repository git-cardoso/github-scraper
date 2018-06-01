import pytest

def test_create_git_repository():
    # create new repositorie
    rep = "eduleones/github-scraper"
    with open("repositories.txt", "w") as f:
        f.write(rep)

def test_run():
    import run

def test_exist_file_txt():
    import os
    os.path.exists('results/github-scraper.txt')

def test_remove_file_txt():
    import os
    os.remove('results/github-scraper.txt')

def test_remove_git_repositoy():
    with open("repositories.txt", 'w'): pass