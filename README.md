# news_highlights

This project was generated with python version 3.6.

### By Niklauspeter

##  Description
This is a python web appliction that consumes a news api(newsapi.org) and uses it to display an array of news feeds sourced from around the world. On clicking a link on the news source, the user is redirected to another webpage where they are able to view news articles with regards to the news source in question .


## User Stories
These include the features that the application allows.
The user is able to:
* See a variety of news items sourced globally
* Click on a link that gives them access to the particular news article
* See a relevant Image, description as well as the time the news article was created.


## Prerequisites
To develop the application , youll need to preinstall a few application. including
* python 3.6
* flask
* pip
* virtual environment
* a text editor 

## Technologies Used
* python 3.6 

## Setup Information
* Clone the application repository to your local machine .
* Create a new virtual environment and access the folder through your virtual amchine.
* Visit the https://newsapi.org/ site and register for an API key.
* Create start.sh file and write the line 
 export NEWS_API_KEY='<Your-Api-Key>'
* run this on your terminal python3.6 manage.py server
* Run chmod +x start.sh follwoed by ./start.sh while in the project folder to start the project.
* Once run, the project can be accessed on your localhost using the address: localhost:5000.

## BDD
|Behavior |Input |Output |
|:------------| :---------|:--------|
|display news sources |on page loading |displays list of news source as per their categories|
|Display news article |click link on news source|redirected to page listing articles from respective source|
|Diplays entire article |click on the article |redirected to the sources actual site to read the article|


## LICENSE
MIT License

Copyright (c) 2019 niklauspeter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact Information
For any enquiries email me at oriokiklaus@gmail.com or github username niklauspeter