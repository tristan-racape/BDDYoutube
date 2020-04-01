import pymongo
import json

# parametrage mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["videos"]

# lecture du fichier json initial de notre projet
file = 'youtube_new/YouTubeDataset_withChannelElapsed.json'
data = []

# liste des atribbuts d'une chaine youtube (correspondant a certains champs dans le json)
listattributechannel = ["channelViewCount", "subscriberCount","videoCount", "channelelapsedtime","channelCommentCount",
                        "totvideos/videocount", "channelId", "totviews/totsubs", "totalviews/channelelapsedtime"]

# liste des atribbuts d'une video youtube (correspondant a certains champs dans le json)
listattributevideo = ["videoId", "videoCategoryId", "views/subscribers", "likes/subscriber", "likes/views",
                      "dislikes/views", "videoViewCount", "comments/subscriber", "likes/dislikes", "comments/views",
                      "elapsedtime", "videoDislikeCount", "dislikes/subscriber", "views/elapsedtime",
                      "VideoCommentCount"]

# ouverture du fichier json afin de pouvoir iterer a l'interieur
with open(file) as f:
    for line in f:
        data.append(json.loads(line))
        
# pour chaque ligne on recupere les champs qui nous interessent et on les integre dans le dictionnaire correspodnant (channel ou video)
for object in data[0]:

    channel = {}

    video = {}

    for attribute,value in object.items():
        if attribute in listattributechannel :
            channel[attribute] = value

    # ajout a la database du dictionnaire channel
    x = mycol.insert_one(channel)

    for attribute, value in object.items():
        if attribute in listattributevideo:
            video[attribute] = value
        if attribute == "channelId":
            myquery = {attribute: value}
        if attribute == "videoPublished":
            myquery2 = {attribute: value}
            video[attribute] = value

    # PUSH le dictionnaire video dans la database
    # on utilise une requete pour mettre la video a l'interieur du channel dans le champ video
    newvideo = {"$push": {"video": video}}
    mycol.update_one(myquery, newvideo)

myclient.close()
