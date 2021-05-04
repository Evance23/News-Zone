
import urllib.request
import json

from app.models import News

# import urllib.request
# import json


# News = news.News

# Getting api key
api_key = None

# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    # print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        # print(url)
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']

            news_results = process_results(news_results_list)
    return news_results


def process_results(news_list):
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
        title = news_item.get('name')
        overview = news_item.get('description')

        news_object = News(id, title, overview)
        news_results.append(news_object)

    return news_results

#     def get_news(id):
#         get_news_details_url = base_url.format(id, api_key)

#         with urllib.request.urlopen(get_news_details_url) as url:
#             news_details_data = url.read()
#             news_details_response = json.loads(news_details_data)

#             news_object = None
#             if news_details_response:
#                 id = news_details_response.get('id')
#                 title = news_details_response.get('original_title')
#                 overview = news_details_response.get('overview')
#                 # poster = movie_details_response.get('poster_path')
#                 # vote_average = movie_details_response.get('vote_average')
#                 # vote_count = movie_details_response.get('vote_count')

#             news_object = News(id,title,overview)

#         return news_object


# def search_news(news_name):
#     search_news_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'.format(api_key,news_name)
#     with urllib.request.urlopen(search_news_url) as url:
#         search_news_data = url.read()
#         search_news_response = json.loads(search_news_data)

#         search_news_results = None

#         if search_news_response['results']:
#             search_news_list = search_news_response['results']
#             search_news_results = process_results(search_news_list)


#     return search_news_results
