from selenium import webdriver


browser = webdriver.Firefox()
# Edith has heard about a new online to-do app. She goes to check out its
# homepage
browser.get('http://localhost:8000')

# She notices the page title/header mention to-do lists
assert 'To-Do' in browser.title

# She is prompted to enter a to-do item
# She does other things the author is too tired to currently write about
# Eventually, after entering in things for her list, she checks the URL later
# and sees her list still there

browser.quit()
