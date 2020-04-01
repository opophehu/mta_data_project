# # method 1

# from bs4 import BeautifulSoup
# import requests
# from requests import get
# import wget


# domain = "http://http://web.mta.info/"
# page = requests.get("http://web.mta.info/developers/turnstile.html/")
# html = page.text
# soup = BeautifulSoup(html, "html.parser")

# for link in soup.find_all('a'):
#     url = link.get('href')
#     if 'April' or "May" or "June" or "04" or "05" or "06" not in url:
#         print(url)
#         file_name = url.split("turnstile")
#         with open(file_name,"wb") as file:
#             response = get(domain+url)
#             file.write(response.content)
#     else:
#         continue

# # method 2
# from bs4 import BeautifulSoup
# import requests
# from requests import get
# import wget

# FILETYPE = '.txt'
# def download_links(url):    
#     source_code = requests.get(url)
#     plain_text = source_code.text
#     soup= BeautifulSoup(plain_text, "html.parser")
#     for link in soup.findAll('a'):
#         try:
#             href = link.get('href')
#             # if FILETYPE in href:
#             print(href)
#             wget.download(href)
#         except:
#             print ("An exception occurred")
# download_links('http://web.mta.info/developers/turnstile.html')

# method 3
from urllib.request import urlretrieve as retrieve
url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_190629.txt"
# url = "http://web.mta.info/developers/data/nyct/turnstile/" + ^04 05 06$
# //regex concat?
retrieve(url, "0629_2019.csv")

# Saturday, June 22, 2019
# Saturday, June 15, 2019
# Saturday, June 08, 2019
# Saturday, June 01, 2019
# Saturday, May 25, 2019
# Saturday, May 18, 2019
# Saturday, May 11, 2019
# Saturday, May 04, 2019


# # method 4
# from bs4 import BeautifulSoup as bs
# import requests


# DOMAIN = 'http://web.mta.info/'
# URL = 'http://web.mta.info/data/nyct/turnstile/'
# FILETYPE = '.txt'

# def get_soup(url):
#     return bs(requests.get(url).text, 'html.parser')
#     for link in get_soup(URL).find_all('a'):
#         file_link = link.get('href')
#         if FILETYPE in file_link:
#             print (file_link)

# get_soup(URL)