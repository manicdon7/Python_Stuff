import requests
from bs4 import BeautifulSoup as bs

github_user = input("Github username:")
#get the github username 
url = "https://github.com/"+ github_user

req = requests.get(url)
#get the request of the url
soup = bs(req.content,'html.parser')
#scrapping the content as html
profile_image = soup.find('img',{'alt' : 'Avatar'})["src"]
#find the image link with the necessary informations
print(profile_image)