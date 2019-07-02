import code
from decimal import *

user_dict = {}
movies = set()
with open("RecommenderSystem/input/userRating.txt") as f:
    data = f.readlines()
    for line in data:
        line = line.strip().split(",")
        userId, movieId, rating = line
        movies.add(movieId)
        if userId not in user_dict:
            user_dict[userId] = {}
        user_dict[userId][movieId] = rating

# code.interact(local = locals())

num_of_movies = len(movies)
for userId in user_dict:
    userId_ratings = user_dict[userId].values()
    userId_ratings = [float(ratings) for ratings in userId_ratings]
    arv = sum(userId_ratings)/len(userId_ratings)
    arv = str(Decimal(arv).quantize(Decimal('.1')))

    for movieId in movies:
        if movieId not in user_dict[userId]:
            user_dict[userId][movieId] = arv

# code.interact(local = locals())

with open("RecommenderSystemFramework/input/processed_userRating.txt", "w+") as f:
    for userId in user_dict:
        for movieId in user_dict[userId]:
            f.write("{},{},{}\n".format(userId, movieId, user_dict[userId][movieId]))



