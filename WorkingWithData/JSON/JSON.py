import json

def openFile(path: str):
    file = open(path)
    x = json.load(file)
    return x

def addNewRating(title: str, rating: int):
    return {"title": title, "rating": rating}

def saveToFile(path: str, data):
    with open(path, 'w') as f:
        json.dump(data, f, ensure_ascii=False)

def showMenu():
    print("\nEnter 1 to delete record")
    print("Enter 2 to add record")

if __name__ == '__main__':
    file = open("movies.json")
    data = json.load(file)

    print("Current ratings: ")
    for i in data:
        print("     {}, rating: {}".format(i.get("title"), i.get("rating")))

    showMenu()
    x = input("\nOption number: ")
    if int(x) == 1:
        newMovies = []
        movieTitle = input("Please enter movie title: ")
        for i in data:
            if i.get('title') != movieTitle :
                newMovies.append(i)
        saveToFile("movies.json", newMovies)

    if int(x) == 2:
        movieTitle, rating = input("Please enter movie title and rating: ").split()
        record = addNewRating(movieTitle, int(rating))
        data.append(record)
        saveToFile("movies.json", data)
