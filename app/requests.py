from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config [" NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

def process_results(movie_list):
    # '''
    # Function  that processes the movie result and transform them to a list of Objects
    
    # Args:
    #     news_list = A list of news items with descriptions

    # Returns:
    #     news_results = a list of news objects
    # ,,,

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')

        # if news:
        #     news_object = News(id, title,overviews)
        #     news_results.append(news_object)


    return movie_results