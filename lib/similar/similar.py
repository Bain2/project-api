
def vectorize(rows: list[tuple]) -> list[set]:
    vectors = {}
    for (id, value) in rows:
        vectors.setdefault(id, set()).add(value)

    return list(vectors.values())


def overlap(u: set, v: set) -> float:
    return len(u & v) / len(u | v)


def most_similar(one: set, many: list[tuple]) -> tuple[float, set]:
    return max(
        (overlap(one, candidate), candidate) 
        for candidate in vectorize(many)
    )

