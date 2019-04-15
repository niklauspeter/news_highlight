from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title ="welcome to news highlights"
    return render_template('index.html', title= title)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    message = "you are the one "
    return render_template('news.html',id = news_id)