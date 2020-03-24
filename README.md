# BDDYoutube
## LAURENT Mathis, RACAPE Tristan, DURAND Erwan, GIRARD Lucie

## Datasets utilisés

Pour notre projet de base de données nous avons choisi d'utiliser un dataset portant sur différentes variétés de chaînes Youtube.
Le dataset est au format .json et est disponible à cette adresse : https://data.world/sevenup13/youtube-video-and-channel-metadata/workspace/file?filename=YouTubeDataset_withChannelElapsed.json

Les différentes chaînes du dataset sont identifiées avec une URL de chaîne, et possèdent de nombreuses statistiques comme le nombre de vues totales, le nombre d'abonnés, le nombre de vidéos, une URL d'une video présente sur la chaîne, etc...

## SGBD utilisé

Pour gérer le dataset, nous avons choisi d'utiliser le SGBD MongoDB car il était plus adapté que CassandraDB pour gérer les fichiers .json puisque ce SGBD genère des index très optimisés pour le format JSON et peut donc atteindre des temps d'éxecutions aussi rapides qu'une base de donnée au format binaire.

Pour insérer le fichier .json dans le SGBD Mongo DB, nous avons utilisé un script python "notes.py"



## Dataset lié

Nous avons lié notre dataset à un autre dataset portant sur des vidéos Youtube, qui référence un grand nombre de vidéos étant passées dans l'onglet "Tendances" de Youtube. Le lien entre les deux dataset se fait avec la colonne "videoID" qui est présente dans les deux dataset, qui est une URL de vidéo.
Nous pourrons regarder par exemple quelles vidéos présentes dans le premier dataset sont arrivés en tendances sur Youtube.


## Table de faits
![alt text](https://i.imgur.com/WxRBm7w.png)

## Schéma des aggregats
![alt text](https://i.imgur.com/y9Ufmba.png)


## Construction de la base de données
#### Détails de la création

(à remplir)

#### Script d'insertion

(à remplir)

#### Script de fusion avec le deuxième dataset

(à remplir)

#### Script d'insertion avec l'API

(à remplir)



## Requêtes intéréssantes

(à remplir)


## Licences

(à remplir)
