import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["videos"]


file = 'youtube_new/YouTubeDataset_withChannelElapsed.json'
data = []
listattributechannel = ["channelViewCount", "subscriberCount","videoCount", "channelelapsedtime","channelCommentCount",
                        "totvideos/videocount", "channelId", "totviews/totsubs", "totalviews/channelelapsedtime"]

listattributevideo = ["videoId", "videoCategoryId", "views/subscribers", "likes/subscriber", "likes/views",
                      "dislikes/views", "videoViewCount", "comments/subscriber", "likes/dislikes", "comments/views",
                      "elapsedtime", "videoDislikeCount", "dislikes/subscriber", "views/elapsedtime",
                      "VideoCommentCount"]
with open(file) as f:
    for line in f:
        data.append(json.loads(line))

for object in data[0]:

    channel = {}

    video = {}

    for attribute,valeur in object.items():
        if attribute in listattributechannel :
            channel[attribute] = valeur
    # print(channel)
    # ajouter a la db le dictionnaire channel
    x = mycol.insert_one(channel)

    for attribute, valeur in object.items():
        if attribute in listattributevideo:
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