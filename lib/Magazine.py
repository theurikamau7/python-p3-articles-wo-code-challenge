class Magazine:
    all_magazines = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        Magazine.all_magazines.append(self)
      
    def name(self):
        return self._name

    def category(self):
        return self._category

    def contributors(self):
        return self._contributors
    
    def add_contributor(self, author):
        self._contributors.append(author)

author1 = ("George R.R. Martin ")
author2 = ("Charmaine DeGraté")
author3 = ("Ian Kamau")

magazine = Magazine("House of the Dragon", "Drama, Action")

magazine.add_contributor(author1)
magazine.add_contributor(author2)
magazine.add_contributor(author3)

print(magazine.name())           
print(magazine.category())
print(magazine.contributors())