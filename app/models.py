class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,author,description,url,urlToImage, publishedAt, content):
        self.id =id
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage=urlToImage    
        self.publishedAt=publishedAt
        self.content=content

class Sources:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country