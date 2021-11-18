import similar 

example = [
    ("User1", "FilmA"), 
    ("User1", "FilmB"), 
    ("User2", "FilmC"), 
    ("User2", "FilmD")
]


def test_sampledataset():
    assert len(example) == 4
    assert ("User2", "FilmD") in example


    
def test_vectorize():
    assert [{"FilmA", "FilmB"}, {"FilmC", "FilmD"}] == similar.vectorize(example)



def test_overlap():
    assert 1 == similar.overlap({"FilmA", "FilmB"}, {"FilmA", "FilmB"})
    assert 0 == similar.overlap({"FilmA", "FilmB"}, {"FilmC", "FilmD"})
    


def test_most_similar():
    assert (1.0, {"FilmA", "FilmB"}) == similar.most_similar({"FilmA", "FilmB"}, example)
    assert (0.5, {"FilmA", "FilmB"}) == similar.most_similar({"FilmA"}, example)
    assert (0.5, {"FilmC", "FilmD"}) == similar.most_similar({"FilmC"}, example)
