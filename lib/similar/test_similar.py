import similar 

example = [
    ("User1", "FilmA"), 
    ("User1", "FilmB"), 
    ("User2", "FilmC"), 
    ("User2", "FilmD"),
    ("User2", "FilmE"), 
    ("User2", "FilmX")
]


def test_sampledataset():
    assert len(example) == 6
    assert ("User2", "FilmD") in example
