import imghdr


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


def sort_data(data: list, key: str, order: str):
    if key == "vote_number":
        order = "asc" if order == "desc" else "desc"
    if order == "desc":
        reverse_order = True
    else:
        reverse_order = False
    return sorted(data, key=lambda d: d.get(key, 0), reverse=reverse_order)


def timestamp_to_date():
    pass
