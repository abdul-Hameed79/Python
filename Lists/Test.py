""" WAP to ask the user to enter names of their fav 3 movies & store them in a list """

# movies = []
# movie1 = input("Enter first movie: ")
# movie2 = input("Enter second movie: ")
# movie3 = input("Enter third movie: ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

movies = []

for i in range(3):
    movie = input(f"Enter movie {i + 1}: ")
    movies.append(movie)
print("Your fav movies are:", movies)
