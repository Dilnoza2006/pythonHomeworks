import requests
import random

API_KEY = "your_api_key_here"
BASE_URL = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()["genres"]
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
    return None

def get_random_movie(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            return random.choice(movies)
    return None

def main():
    genre = input("Enter a movie genre: ")
    genre_id = get_genre_id(genre)
    if genre_id:
        movie = get_random_movie(genre_id)
        if movie:
            print(f"Recommended movie: {movie['title']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No movies found in this genre.")
    else:
        print("Invalid genre.")

if __name__ == "__main__":
    main()