from apiclient.discovery import build
import pymongo
import json

api_key = YOUR API KEY HERE # clé de l'api youtube

youtube = build('youtube','v3',developerKey=api_key)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"] #the database
mycol = mydb["videos"] # the collection

listChannel = mycol.find() # list of all channel with all attributes

listChannelId = mycol.find({}, {'channelId':1, '_id':0}) # list of all channel ID

for channel in listChannel:
    for video in channel['video']: # for all vidéos in the channel
        request = youtube.commentThreads().list(
            part="snippet,replies",
            maxResults=10,
            videoId=video['videoId']
        ) # request of 10 first comments of the vidéo
        try:
            response = request.execute()
        except Exception as e:
            print(e)

        commentList = []
        if response['items']: # if a video have comments
            for comment in response['items']: # we put all comments in a list

                newCommentaire = {}

                newCommentaire['authorChannelId'] = comment['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
                newCommentaire['authorDisplayName'] = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                newCommentaire['text'] = comment['snippet']['topLevelComment']['snippet']['textDisplay']
                newCommentaire['publishedAt'] = comment['snippet']['topLevelComment']['snippet']['publishedAt']
                commentList.append(newCommentaire)

        mycol.update_one({'video':{'$elemMatch':{'videoId': video['videoId']}}},{'$set':{'video.$.topComment': commentList}}) # we update the video with the comments
        print("comments added")
