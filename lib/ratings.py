
def get_user_liked(db, cutoff=4):
    return db.execute(f"""
        SELECT UserID, ItemID 
        FROM ratings
        WHERE Rating >= {cutoff}
    """)

def get_movies_rated(db, movies, n=6):
    return db.execute(f"""
        SELECT MovieTitle, ROUND(100 * AVG(Rating)/5)
        FROM ratings 
        WHERE ItemID IN {tuple(movies)}
        GROUP BY MovieTitle
        ORDER BY Rating 
        LIMIT {n}
    """)
