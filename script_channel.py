from apiclient.discovery import build
import pymongo
import json

api_key = YOUR API KEY HERE # clé de l'api youtube

youtube = build('youtube','v3',developerKey=api_key)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"] # the database
mycol = mydb["videos"] # the collection


listChannelId = mycol.find({}, {'channelId':1, '_id':0}) # requete de toute les chaines étant actuellement dans la bd

for id in listChannelId:
    print("id :"+id['channelId'])
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=id['channelId']
    ) # on utilise l'id des chaines pour faire une requetes de toutes les informations à l'api youtube
    response = request.execute()
    if response['items']:
        newChaineAttribut = {"$set": {"name": response['items'][0]['snippet']['title'], "description": response['items'][0]['snippet']['description']}}
        #INSERER ICI DANS LA BASE NOSQL LES INFOS
        mycol.update_one({'channelId': id['channelId']}, newChaineAttribut)
