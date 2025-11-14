class Movies:
    def __init__(self,name,hero,heroine):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        
    def info(self):
        print(f'Movie name : {self.name}')
        print(f'Movie name : {self.hero}')
        print(f'Movie name : {self.heroine}')
list_of_movies = []
while True:
    name = input('Enter movie name :')
    hero = input('Enter hero name :')
    heroine = input('Enter heroineie name :')
    m=Movies(name,hero,heroine)
    list_of_movies.append(m)
    print('Movies successfully added......')
    option = input('Do you want add more movies.. If yes|No :')
    if option.lower() == 'no' :
        break
for movies in list_of_movies:
    movies.info()
    print()
