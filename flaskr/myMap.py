from flaskr.config import MapApi 

def MapViewUrl(mode):
    key = MapApi["key"]
    url_part = 'https://www.google.com/maps/embed/v1/{mode}?key={key}&q=Eiffel+Tower,Paris+France'
    url = url_part.format(mode=mode, key=key)
    urlDict = {
        "url": url
    }
    return urlDict




