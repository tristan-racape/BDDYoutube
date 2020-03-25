import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["videos"]


file = 'youtube_new/YouTubeDataset_withChannelElapsed.json'
data = []
with open(file) as f:
    for line in f:
        data.append(json.loads(line))

for object in data[0]:

    channel = {}

    video = {}

    for attribute,valeur in object.items():
        if ((attribute == "channelViewCount") | (attribute =="subscriberCount") | (attribute =="videoCount") |
                (attribute =="channelelapsedtime") | (attribute =="channelCommentCount") |
                (attribute =="totvideos/videocount") | (attribute =="channelId") |
                (attribute =="totviews/totsubs") | (attribute == "totalviews/channelelapsedtime")) :
            channel[attribute] = valeur
    # print(channel)
    # ajouter a la db le dictionnaire channel
    x = mycol.insert_one(channel)

    for attribute, valeur in object.items():
        if ((attribute == "videoId") | (attribute == "videoCategoryId") | (attribute == "views/subscribers") | (
                attribute == "likes/subscriber") | (attribute == "likes/views") | (
                attribute == "dislikes/views") | (attribute == "videoViewCount") | (
                attribute == "comments/subscriber") | (attribute == "likes/dislikes") | (attribute == "comments/views")
                | (attribute == "elapsedtime") | (attribute == "videoDislikeCount") |
                (attribute == "dislikes/subscriber")
                | (attribute == "views/elapsedtime") | (attribute == "VideoCommentCount")):
            video[attribute] = valeur
        if attribute == "channelId":
            myquery = {attribute: valeur}
        # do something for date isolation ?
        if attribute == "videoPublished":
            myquery2 = {attribute: valeur}
            video[attribute] = valeur
    # print(video)
    # PUSH le dictionnaire video
    newvideo = {"$push": {"video": video}}
    mycol.update_one(myquery, newvideo)

myclient.close()