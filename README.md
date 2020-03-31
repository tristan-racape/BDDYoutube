# BDDYoutube
## LAURENT Mathis, RACAPE Tristan, DURAND Erwan, GIRARD Lucie

## Construction de la base de données

### Dépendences

Vous aurez besoin de :

    Python 3
    pymongo : pip install pymongo
    apiclient.discovery : pip install --upgrade google-api-python-client

### Exécution des scripts

Pour construire la base de données, il faut d'abord télécharger ce dataset : https://drive.google.com/file/d/1uL0tHMoXIVKow1zM34bcAp2Ku139mFBo/view

Une fois téléchargé il faut placer ce dataset dans un dossier youtube_new (ou modifier l'emplacement dans le script).
Il faut ensuite générer une clé Youtube api V3 (https://developers.google.com/youtube/v3/getting-started?hl=fr) que vous placerez dans la variable api_key de script_channel.py et script_commentaire.py

puis exécuter dans l'ordre : 

    python insert_premier_dataset.py
    python script_channel.py
    python script_commentaire.py
    
Les exécutions peuvent être longues ou soumises à des dépassements de quotas par Youtube et vous n'êtes pas obligé d'exécuter les scripts jusqu'au bout. Par exemple, 50 000 itérations pour le 1er script sont suffisantes si le but est seulement de tester.

## Datasets utilisés

Pour notre projet de base de données nous avons choisi d'utiliser un dataset portant sur différentes variétés de chaînes Youtube.
Le dataset est au format .json et est disponible à cette adresse : https://data.world/sevenup13/youtube-video-and-channel-metadata/workspace/file?filename=YouTubeDataset_withChannelElapsed.json

Les différentes chaînes du dataset sont identifiées avec une URL de chaîne, et possèdent de nombreuses statistiques comme le nombre de vues totales, le nombre d'abonnés, le nombre de vidéos, une URL d'une video présente sur la chaîne, etc...

## SGBD utilisé

Pour gérer le dataset, nous avons choisi d'utiliser le SGBD MongoDB car il était plus adapté que CassandraDB pour gérer les fichiers .json puisque ce SGBD genère des index très optimisés pour le format JSON et peut donc atteindre des temps d'éxecutions aussi rapides qu'une base de donnée au format binaire.

Pour insérer le fichier .json dans le SGBD Mongo DB, nous avons utilisé un script python "insert_premier_dataset.py"


## Dataset lié

Nous avons lié notre dataset à un autre dataset portant sur des vidéos Youtube, qui référence un grand nombre de vidéos étant passées dans l'onglet "Tendances" de Youtube. Le lien entre les deux dataset se fait avec la colonne "videoID" qui est présente dans les deux dataset, qui est une URL de vidéo.
Nous pourrons regarder par exemple quelles vidéos présentes dans le premier dataset sont arrivés en tendances sur Youtube.
Il est disponible ici : https://www.kaggle.com/datasnaek/youtube-new


## Schéma des aggregats
![alt text](https://i.imgur.com/y9Ufmba.png)
    
## Requêtes intéréssantes

10 exemples de requêtes intéressantes sont présentes dans le fichier requete.txt

## Licences

Dataset principal : CC0 (Public domain)
