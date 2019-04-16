from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news, get_sources
#from .forms import ReviewForm
from ..models import News

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources for index page
    general_sources= get_sources('general')
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')

    
    title = 'Home - Welcome to The best news hightlight Website Online'
    return render_template('index.html', title=title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources, general_sources=general_sources)


@main.route('/news/<id>')
def news(id):
    '''
    View articles page
    '''
    news_articles = get_news(id)
    title = f'NH | {id}'
    
    return render_template('news_articles.html', title= title,news_articles = news_articles)
