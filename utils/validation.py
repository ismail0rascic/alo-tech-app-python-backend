
def validate_genre_input(data, genre):
    error = False

    if genre not in data:
        error = "This genre is not available, please try another!"

    if genre == '':
        error = "Please, input genre to start searching!"

    return error