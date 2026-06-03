def find_by(items, key, value):
    """
    Return the first object in a list of dicts where key == value.
    """
    return next((i for i in items if i.get(key) == value), None)


if __name__ == "__main__":
    sample = [
        {"id": "s1", "vpc_id": "vpc-a"},
        {"id": "s2", "vpc_id": "vpc-b"}
    ]

    print(find_by(sample, "id", "s2"))
