from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, get_news, search_news
from .forms import ReviewForm
from ..models import Review


# Views
@main.route('/')
def index():
    # newsapi = NewsApiClient( api_key= "89a6b67f299a406690de9228d689ec14")
    # topheadlines =
    '''
    View root page function that returns the index page and its data and top headlines
    '''
    # getting popular news list
    technology = get_news('technology')
    science = get_newsn('science')
    politics = get_news('politics')
    sports = get_news('sports')
    business = get_news('business')
    entertainment = get_news('entertainment')

    # Getting popular news
    popular_news = get_news('popular')
    # print(popular_news)
    title = "Home- Welcome to the Home of News Updates"
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search', news_name=search_news))
    else:
        return render_template('index.html', title=title, technology=technology, science=science, politics=politics, sports=sports, business=business, entertainment=entertainment)

@main.route('/news/<int:id>')
def news(id):

    news = get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)

    return render_template('news.html', title=title, news=news, reviews=reviews)


@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'

    return render_template('search.html', news=searched_news)


@main.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id, title, news.poster, review)
        new_review.save_review()
        return redirect(url_for('news', id=news.id))

    title = f'{news.title} review'
    return render_template('new_review.html', title=title, review_form=form, news=news)
