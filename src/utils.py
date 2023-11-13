def get_id(__obj: object) -> None | int:
    _id = id(__obj)
    if (_id == id(None)):
        return "None"
    else:
        return _id