import hmac
from hashlib import sha256

def generate_sig(endpoint, params, secret):
    sig = endpoint
    for key in sorted(params.keys()):
        sig += '|%s=%s' % (key, params[key])
    return hmac.new(secret, sig, sha256).hexdigest()

def save_picture(url, i):
    import urllib
    urllib.urlretrieve(url, "pictures/picture_{0}.jpg".format(str(i)))

from instagram.client import InstagramAPI

api = InstagramAPI(client_id='cab252bf28404d94b9b224ce34bfe0dc', client_secret='768d8cbfd06e4bc3abe1e4836a2222a4')
popular_media = api.media_search(lat=55.615966, lng=12.076837, distance=8000, max_timestamp=1433894400)
#popular_media = api.tag_search('rf15')
for i, media in enumerate(popular_media):
    url = media.images['standard_resolution'].url
    print url
    media_id = media.get_id()
    comments = api.media_comments(media_id)
    print comments
    likes = api.media_likes(media_id)
    print likes
    save_picture(url, i)



#lat 55.615966,
#long 12.076837