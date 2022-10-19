from distutils.spawn import spawn
from bs4 import BeautifulSoup
import requests

#print("hello this is new")

url = 'https://readnoveltrend.com/novelfull/kingdoms-bloodline/chapter-1'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')
main_text = ''
wcon = soup.find_all('div', class_='chr-c')
print(wcon)
for tc in wcon:
    main_text = tc
#print(main_text.prettify())
#nextone=BeautifulSoup(html, 'html.parser')
my_data=soup.find_all( 'a', attrs = {'id': 'next_chap'})
for x in my_data:
    my_href = x.get("href")

split = my_href.split(" ",1)
new_url = (split[0]);
# for tag in nextone.find_all('a', {"id" :"next_chap"}):
#     print (tag)
# res = nextone.select('a[id="next-chap"]')


################

