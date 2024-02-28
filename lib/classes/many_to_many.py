class Article:

    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, 'title'):
            self._title = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine

class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != "" and not hasattr(self, 'name'):
            self._name = name

    def articles(self):
        return [article for article in Article.all if article._author == self]

    def magazines(self):
        return list({article._magazine for article in Article.all if article._author == self})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list({article._magazine.category for article in Article.all if article._author == self})
        return topics if topics else None

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and category != "":
            self._category = category

    def articles(self):
        return [article for article in Article.all if article._magazine == self]

    def contributors(self):
        return list({article._author for article in Article.all if article._magazine == self})

    def article_titles(self):
        titles = [article._title for article in Article.all if article._magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article._author for article in Article.all if article._magazine == self]
        contributors = list({author for author in authors if authors.count(author) > 2})
        return contributors if contributors else None