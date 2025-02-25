# class Article:
#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
        
# class Author:
#     def __init__(self, name):
#         self.name = name

#     def articles(self):
#         pass

#     def magazines(self):
#         pass

#     def add_article(self, magazine, title):
#         pass

#     def topic_areas(self):
#         pass

# class Magazine:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     def articles(self):
#         pass

#     def contributors(self):
#         pass

#     def article_titles(self):
#         pass

#     def contributing_authors(self):
#         pass






# class Article:
#     all = []  # Store all article instances

#     def __init__(self, author, magazine, title):
#         if type(author) is Author and type(magazine) is Magazine and type(title) is str and 5 <= len(title) <= 50:
#             self._author = author
#             self._magazine = magazine
#             self._title = title  # Immutable
#             Article.all.append(self)

#     @property
#     def title(self):
#         return self._title  # No setter (immutable)

#     @title.setter
#     def title(self, value):
#         raise AttributeError("Title is immutable and cannot be changed")

#     @property
#     def author(self):
#         return self._author

#     @author.setter
#     def author(self, value):
#         if type(value) is Author:
#             self._author = value

#     @property
#     def magazine(self):
#         return self._magazine

#     @magazine.setter
#     def magazine(self, value):
#         if type(value) is Magazine:
#             self._magazine = value


# class Author:
#     def __init__(self, name):
#         if type(name) is str and len(name) > 0:
#             self._name = name

#     @property
#     def name(self):
#         return self._name  # Immutable

#     @name.setter
#     def name(self, value):
#         raise AttributeError("Author name cannot be changed")

#     def articles(self):
#         return [article for article in Article.all if article.author == self]

#     def magazines(self):
#         return list(set(article.magazine for article in self.articles())) if self.articles() else []

#     def add_article(self, magazine, title):
#         if type(magazine) is Magazine and type(title) is str and 5 <= len(title) <= 50:
#             return Article(self, magazine, title)

#     def topic_areas(self):
#         topics = list(set(magazine.category for magazine in self.magazines()))
#         return topics if topics else None


# class Magazine:
#     def __init__(self, name, category):
#         self._name = name if type(name) is str and 2 <= len(name) <= 16 else "Default"
#         self._category = category if type(category) is str and len(category) > 0 else "General"

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if type(value) is str and 2 <= len(value) <= 16:
#             self._name = value

#     @property
#     def category(self):
#         return self._category

#     @category.setter
#     def category(self, value):
#         if type(value) is str and len(value) > 0:
#             self._category = value

#     def articles(self):
#         return [article for article in Article.all if article.magazine == self]

#     def contributors(self):
#         return list(set(article.author for article in self.articles())) if self.articles() else []

#     def article_titles(self):
#         titles = [article.title for article in self.articles()]
#         return titles if titles else None

#     def contributing_authors(self):
#         author_count = {}
#         for article in self.articles():
#             author_count[article.author] = author_count.get(article.author, 0) + 1
#         top_authors = [author for author, count in author_count.items() if count > 2]
#         return top_authors if top_authors else None




class Article:
    all = []  # Store all article instances

    def __init__(self, author, magazine, title):
        if type(author) is Author and type(magazine) is Magazine and type(title) is str and 5 <= len(title) <= 50:
            self._author = author
            self._magazine = magazine
            if not hasattr(self, '_title'):
                self._title = title  # Immutable
            Article.all.append(self)

    @property
    def title(self):
        return self._title  # No setter (immutable)

    @title.setter
    def title(self, value):
        if not hasattr(self, '_title'):
            self._title = value  # Allow setting only once

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if type(value) is Author:
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if type(value) is Magazine:
            self._magazine = value


class Author:
    def __init__(self, name):
        if type(name) is str and len(name) > 0:
            if not hasattr(self, '_name'):
                self._name = name

    @property
    def name(self):
        return self._name  # Immutable

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):
            self._name = value  # Allow setting only once

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles())) if self.articles() else []

    def add_article(self, magazine, title):
        if type(magazine) is Magazine and type(title) is str and 5 <= len(title) <= 50:
            return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(set(magazine.category for magazine in self.magazines()))
        return topics if topics else None


class Magazine:
    def __init__(self, name, category):
        self._name = name if type(name) is str and 2 <= len(name) <= 16 else "Default"
        self._category = category if type(category) is str and len(category) > 0 else "General"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is str and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) is str and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles())) if self.articles() else []

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
        top_authors = [author for author, count in author_count.items() if count > 2]
        return top_authors if top_authors else None
