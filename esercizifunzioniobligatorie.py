# ESERCIZIO 8.1

# def display_message (message:str):
#     print(message)

# display_message ("Tua madre puttana e tu zia nana pelata")

# ESERCIZIO 8.2

# def favorite_book (title:str):
#     print(f"One of my favorite book is {title}")

# favorite_book ("Meinkauf")

# ESERCIZIO 8.3

# def make_shirt (size:str , message:str):
#     print(f"le taglie disponibili sono {size} e il messaggio sulla maglia è '{message}' ")

# make_shirt ("XL" , "Vincere e vinceremo")

# ESERCIZIO 8.4

# def make_shirt (size = "L" , message = "I Love Python"):
#     print(f"le taglie disponibili sono {size} e il messaggio sulla maglia è '{message}' ")

# make_shirt()
# make_shirt ("M")
# make_shirt ("XL" , "W Il Duce")


# ESERCIZIO 8.5

# def describe_city (city:str , country:str):
#     print(f" {city} is in {country}")

# describe_city ("Auschwitz" , "Polonia")
# describe_city ("Pyongyang" , "Corea del Nord")
# describe_city ("Bagdad" , "Iraq")

# ESERCIZIO 8.6

# def city_country (city:str , country:str):
#     print(f"{city} , {country} ")

# city_country ("Auschwitz" , "Polonia")
# city_country ("Pyongyang" , "Corea del Nord")
# city_country ("Bagdad" , "Iraq")

# ESERCIZIO 8.7

# def make_album(artist_name:str,album_name:str,number_songs:int = None): 
#    if number_songs == None: 
#       return{"artist_name":artist_name,"album_name":album_name}
#    else: 
#      return{"artist_name": artist_name,"album_name":album_name,"number_songs":number_songs}
   
# print(make_album("tha sup","Le basi","8"))
# print(make_album("Adele","19"))
# print(make_album("Sam Smith","The Thrill of It All","14"))

# ESERCIZIO 8.8

# def make_album(artist, title):
#     album:dict = {"artist": artist, "title": title}   
#     return album

# while True:
#     artist:str = str(input("Artist: "))
#     title:str = str(input("Title: "))

#     album = make_album(artist, title)
#     print(album)

# ESERCIZIO 8.9

list_messagge: list = ["Labor march frei" , "I have a dream" , "Io rispetto l'omofobia"]

def show_messages (messaggi):

    for i in messaggi:

        print(i)

show_messages(list_messagge)


# ESERCIZIO 8.10

# lista_messaggi = ["Ciao","Come Stai","Tutto Bene?","A Presto!"]
# def send_messages(messaggi):

#     sent_messages=[]
#     upper_bound = len (messaggi)
#     print(f"{messaggi=}\n {sent_messages=}\n\n")
#     for i in range (upper_bound):
        
#         message = messaggi.pop(0)
#         sent_messages.append(message)

#         print(f"{messaggi=}\n {sent_messages=}\n\n")
# send_messages(lista_messaggi)

# ESERCIZIO 8.11

# lista_messaggi = ["Ciao","Come Stai","Tutto Bene?","A Presto!"]
# def send_messages(messaggi):

#     sent_messages=[]
#     upper_bound = len (messaggi)
#     print(f"{messaggi=}\n {sent_messages=}\n\n")
#     for i in range (upper_bound):
        
#         message = messaggi.pop(0)
#         sent_messages.append(message)

#         print(f"{messaggi=}\n {sent_messages=}\n\n")
# send_messages(lista_messaggi)

# ESERCIZIO 8.12

# sandwich_items : list = ["hamburger" , "Cacio cavallo" , "Nduja"]





