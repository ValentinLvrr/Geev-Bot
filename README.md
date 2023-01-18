![banner_geev](https://www.don.fr/wp-content/uploads/2019/11/Image_Maureen-1.jpg)

# Qu-es ce que Geev ?
[**Geev**]() est la plateforme n°1 de don d'objets ( livres, vetements, meubles, ...) entre particuliers en France.

# En quoi consiste le robot
Le Geev-Bot va dénicher toutes les nouvelles annonces publiées dans un rayon de x km autour de chez vous.

# Installation & Configuration
### 1: Clonner le repo
```
git clone https://github.com/ValentinLvrr/Geev-Bot
cd Geev-Bot
```

### 2: Editer le fichier `config.py`
![searchbar_geev](https://i.ibb.co/5ngn2Z6/Capture-d-cran-2023-01-18-213025.png)
```py
DISTANCE = str(15000)# 15km
CHANNEL_ID = 1234567890
INTERVAL = 60
GEEV_URL = '' + DISTANCE # coupez l'url de la page d'acceuille en incluant "&distance="
TOKEN = ""
```

# Lancement
Après avoir configuré le robot dans le fichier `config.py` :
```
python bot.py
```

![resultat](https://i.ibb.co/cNt2XtQ/Capture-d-cran-2023-01-18-213332.png)