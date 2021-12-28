from bs4 import BeautifulSoup 
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

# search 
query = input('massukan query : ') 
print(query)
if query == '' : 
    query+= 'cerita'


# get url 
get_data = requests.get(f'https://www.wattpad.com/stories/{query}/hot?locale=id_ID', headers=headers).text
soup = BeautifulSoup(get_data, 'html.parser')

# find all elemet 
des = soup.find_all('div', class_='description')
athor = soup.find_all('a', 'username')
view = soup.find_all('span', class_='read-count')
title = soup.find_all('a', class_='title')

#
data =[]
for index,row in enumerate(title): 

    # get image
    img = soup.find_all('a', class_='cover')[index]
    img2 = []
    for i in img: 
        img2.append(i.find('img').get('src'))

    # extrack data to dict 
    data.append(
        {
        'author': athor[index].get_text(), 
        'view': view[index].get_text(),
        'descritions': des[index].get_text(), 
        'title': row.get_text(), 
        'img': img2

        
        }, 

    )


print(data)
    
    
    
