
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
