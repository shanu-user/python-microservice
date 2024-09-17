import requests
from bs4 import BeautifulSoup


def fetch_articles():
    url = "https://www.who.int/news/"
    response = requests.get(url)
    print("Hello", response)



    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        pageArticles = soup.find('div', {'class': 'hubfiltering'})
        
        print('Getting content under pageArticles: \n',pageArticles)
        
        listArticles = pageArticles.find('div', {'class': 'list-view'})

        print('Getting content under listArticles: \n',listArticles)

        viewContent = listArticles.find('div', {'class': 'k-listview-content'})
    
        print('Getting content under viewContent: \n', viewContent)


fetch_articles()
