from apiclient.discovery import build
import pymongo
import json

api_key = "AIzaSyCJPH-OV7sq1MJM8_8rJhlDKMBP--dHQuo" # clé de l'api youtube

youtube = build('youtube','v3',developerKey=api_key)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["videos"]

listChannel = mycol.find()

listChannelId = mycol.find({}, {'channelId':1, '_id':0})

for channel in listChannel:
    for video in channel['video'][0:1]:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            maxResults=10,
            videoId=video['videoId']
        )
        try:
            response = request.execute()
        except Exception as e:
            raise
        
        commentList = []
        if response['items']:
            for comment in response['items']:

                newCommentaire = {}

                newCommentaire['authorChannelId'] = comment['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
                newCommentaire['authorDisplayName'] = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                newCommentaire['text'] = comment['snippet']['topLevelComment']['snippet']['textDisplay']
                newCommentaire['publishedAt'] = comment['snippet']['topLevelComment']['snippet']['publishedAt']
                commentList.append(newCommentaire)

        mycol.update_one({'video':{'$elemMatch':{'videoId': video['videoId']}}},{'$set':{'video.$.topComment': commentList}})
        print("comments added")
