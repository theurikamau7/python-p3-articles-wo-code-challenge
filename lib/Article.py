class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)
        
    def title(self):
        return self._title
    
    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    def all():
        return Article.all_articles
    
author = ("Jason Sudeikis")
magazine = ("Ted Lasso", "Comedy")

article1 = Article(author, magazine, "Article 1")


print(article1.title())     
print(article1.author())    
print(article1.magazine())  


all_articles = Article.all()
for article in all_articles:
    print(article.title(), article.author(), article.magazine())