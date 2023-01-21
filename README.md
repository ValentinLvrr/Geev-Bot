![banner_geev](https://www.don.fr/wp-content/uploads/2019/11/Image_Maureen-1.jpg)

# What is Geev?
[**Geev**]() is the Number 1 of platform for donating objects (books, clothing, furniture, etc.) between individuals in France.

# Installation & Configuration
### 1: Clone the repository
```
git clone https://github.com/ValentinLvrr/Geev-Bot
cd Geev-Bot
```

### 2: Edit [`config.py`](https://github.com/ValentinLvrr/Geev-Bot/blob/master/config.py)
![searchbar_geev](https://i.ibb.co/5ngn2Z6/Capture-d-cran-2023-01-18-213025.png)
```py
DISTANCE = str(15000)# 15km
CHANNEL_ID = 1234567890
INTERVAL = 60
GEEV_URL = '' + DISTANCE # coupez l'url de la page d'acceuille en incluant "&distance="
TOKEN = ""
```

# Launching
```
python3 bot.py
```

### Discord :
![result](https://i.ibb.co/cNt2XtQ/Capture-d-cran-2023-01-18-213332.png)

### Terminal :
![terminal_result](https://i.ibb.co/QndbXmn/Capture-d-cran-2023-01-19-083431.png)