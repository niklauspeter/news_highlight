from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news, get_sources
from .models import news

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources for index page
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')

    # Getting news headlines
    top_headlines = get_news('top-headlines')
    
    title = 'Home - Welcome to The best news hightlight Website Online'
    return render_template('index.html', title=title, headlines=top_headlines,sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    
    return render_template('news.html', id=news_id)
