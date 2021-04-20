from flask import render_template
from app import app
from newsapi import NewsApiClient


# Views
@app.route('/')
def index():
    # newsapi = NewsApiClient( api_key= "89a6b67f299a406690de9228d689ec14")
    # topheadlines =
    '''
    View root page function that returns the index page and its data and top headlines
    '''
    # getting popular news list
    technology = get_news ('technology')
    science = get_newsn('science')
    politics = get_news('politics')
    sports = get_news('sports')
    business = = get_news('business')
    entertainment = get_news('entertainment')

    
    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    title = "Home- Welcome to the Home of News Updates"
    return render_template('index.html', title = title, technology = technology, science = science, politics = politics, sports=sports, business = business. entertainment = entertainment')

