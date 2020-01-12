def song_info2(title,artist= "Unknown"):
    return {"title": title, "artist": artist}

def song_create(passed_list):
    for song in passed_list:
        print(song)
