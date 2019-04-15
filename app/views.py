from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting news headlines
    top_headlines = get_news('top-headlines')
    
    title = 'Home - Welcome to The best news hightlight Website Online'
    return render_template('index.html', title=title, headlines=top_headlines)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    
    return render_template('news.html', id=news_id)
