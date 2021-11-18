
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware as cors


app = FastAPI()
app.add_middleware(cors,allow_origins=["*"])


@app.get("/api/v1/sample/movies/recommend")
async def movie_recommend_sample():
    return {
        "movies": {
            'Event Horizon (1997)' : 5,
            'Hoop Dreams (1994)' : 4,
            'Basic Instinct (1992)' : 3
        }
    }
import sys; sys.path.append('./lib')

import sqlite3
from ratings import get_movies_rated, get_user_liked
from similar.recm import most_similar


@app.post("/api/v1/movies/recommend")
async def movie_recommend(their_movies: set[int] = Form(...)):
    with sqlite3.connect("db/ratings.db") as db:  
        score, movies = most_similar(their_movies, get_user_liked(db))

        return {
            "score": round(2**(score-1), 2),
            "movies": get_movies_rated(db, movies - their_movies)
        }
