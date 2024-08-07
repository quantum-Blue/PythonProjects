import requests

class theMovieDB:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="934edd32d73859170059504686ca638c"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDB()

while True:
    secim = input("1- Popular Movies\n2- Search Movie\n3- Exit\nSecim: ")
    
    if secim == "1":
        movies = movieApi.getPopulars()
        for movies in movies["results"]:
            print(movies["title"])
    
    elif secim == "2":
        keyword = input("keyword: ")
        movies = movieApi.getSearchResults(keyword)
        for movies in movies["results"]:
            print(movies["name"])

    elif secim == "3":
        break