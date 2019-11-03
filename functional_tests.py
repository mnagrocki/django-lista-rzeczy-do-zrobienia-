from selenium import webdriver

browser = webdriver.Chrome(r'C:\Users\mnagr\PycharmProjects\TDD-poprawki\drivers\chromedriver.exe')
browser.get('http://localhost:8000')
assert 'Django' in browser.title
