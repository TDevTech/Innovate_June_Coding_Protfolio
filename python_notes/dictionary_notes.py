# this is dictionary_notes.py

# print ("This is dictionaries")

# my_giraffe = {
#     "name"  : "Sela",
#     "breed" : "Masai",
#     "colour" : "Yallow & Black",
#     "mood"  : "funny"
# }
# print (my_giraffe ["breed"])
# print (f'My Giraffe {my_giraffe ["name"]} is a bit {my_giraffe ["mood"]} today\n')

# ## list variable do not updates , Keys variables to updates becoase uses View Object...
# ## when print it.

# #my_giraffe = my_giraffe.keys()
# print (my_giraffe.keys())

# my_giraffe ["age"] =6
# print(my_giraffe)
# print(my_giraffe.values())
# print(my_giraffe.items())
# print(my_giraffe.get("colour"))
# print(my_giraffe.get("legs","this key doesn't exist"))
# #print(my_giraffe["legs"])

# my_giraffe.update({"legs":"4"})
# my_giraffe.update({"food":"Vegetarian"})
# print(my_giraffe)

# my_giraffe.pop("food")
# print(my_giraffe)
## To find use git method with Keys veriables

## Activity 2

countrys = {
    "United Kingdom" : "London",
    "France" :"Paris",
    "Germany" : "Berlin",
    "Spain" : "Madrid",
    "Italy" : "Rome"}

# print(countrys)

# China = countrys.setdefault('China','Bejen')
# canada = countrys.setdefault('Canada' ,'Ottowa')
# print('countrys =',countrys)
# print('China =' ,China)
# print('canada =', canada)
# print (countrys)

#countrys.setdefault ({'China': 'Bejen', 'Canada': 'Ottawa'})
#print(countrys)
###
for i in countrys.items():
    print (i)
###
print (list(countrys))
###
for x in countrys.keys():
    print(x + ":" + countrys[x])
###
countrys.update ({
            "United Kingdom" : "English",
            "France" :"French",
            "Germany" : "Berlin",
            "Spain" : "Spanish",
            "Italy" : "Italian" })


### Activity 3 fav_songs

# keys: artist, song_name, genre, release_year

fav_songs = {
    "George Benson":["Affirmation", "Smooth Jazz", "1976"],
    "Bob James":"Since I Fell For You":"Smooth Jazz":"1986",
    "Bob James":"Raise The Roof":"Smooth Jazz":"1999",
    "Bony James":"Joy Ride":"Smooth Jazz":"1999", 
    "Ron Fattorusso": "No Es Facil" : "Latin Smooth Jazz" : "2004",
    "Incognito":"Pieces Of A Dream" : "Smooth Jazz" : "1993",
    "Sade":"Your Love Is King" : "Smooth Jazz & soul" : "1983",
    "Chris Botti":"Good Morning Heartache" : "Jazz & RnB" : "2005",
    "Norman Brown":"After The Storm" : "Smooth Jazz" : "1994",
    "Grover Washington Jr":"Take Five" : "Smooth Jazz" : "1992"}


# fav_songs = {
            # # 'track00' : { 'Artist''null','Song_name':'','Genre' :'','Release_year':''},
            # # 'track01' : { 'Artist':'George Benson','Song_name':'Affirmation','Genre' :'Smooth Jazz','Release_year':'1976'},
            # # 'track02' : [ 'Artist':'Bob James','Song_name':'Since I Fell For You','Genre' :'Smooth Jazz','Release_year':'1986'],
            # # 'track03' : [ 'Artist':'Bob James','Song_name':'Raise The Roof','Genre' :'Smooth Jazz','Release_year':'1999'],
            # # 'track04' : [ 'Artist':'Bony James','Song_name':'Joy Ride','Genre' :'','Release_year':'1999'],
            # # 'track05' : [ 'Artist':'Ron Fattorusso','Song_name':'No Es Facil','Genre' :'Latin Smooth Jazz','Release_year':'2004'],
            # # 'track06' : [ 'Artist':'Incognito','Song_name':'Pieces Of A Dream','Genre' :'Smooth Jazz','Release_year':'1993'],
            # # 'track07' : [ 'Artist':'Sade','Song_name':'Love Is King','Genre' :'Smooth Jazz & soul','Release_year':'1983'],
            # # 'track08' : [ 'Artist':'Chris Botti','Song_name':'Good Morning Heartache','Genre' :'Jazz & RnB','Release_year':'2005'],
            # # 'track09' : [ 'Artist':'Norman Brown','Song_name':'After The Storm','Genre' :'Smooth Jazz','Release_year':'1994'],
            # # 'track10' : [ 'Artist':'Grover Washington Jr','Song_name':'Take Five','Genre' :'Smooth Jazz','Release_year':'1992']
            # }
#import string

# keys = { 'Artist':'','Song_name':'','Genre' :'','Release_year':''}


# track00 = {'Artist':'null','Song_name':'none','Genre' :'none','Release_year':'null'} 
# track01 = { 'Artist':'George Benson','Song_name':'Affirmation','Genre' :'Smooth Jazz','Release_year':'1976'}
# track02 = { 'Artist':'Bob James','Song_name':'Since I Fell For You','Genre' :'Smooth Jazz','Release_year':'1986'}
# track03 = { 'Artist':'Bob James','Song_name':'Raise The Roof','Genre' :'Smooth Jazz','Release_year':'1999'}
# track04 = { 'Artist':'Bony James','Song_name':'Joy Ride','Genre' :'','Release_year':'1999'}
# track05 = { 'Artist':'Ron Fattorusso','Song_name':'No Es Facil','Genre' :'Latin Smooth Jazz','Release_year':'2004'}
# track06 = { 'Artist':'Incognito','Song_name':'Pieces Of A Dream','Genre' :'Smooth Jazz','Release_year':'1993'}
# track07 = { 'Artist':'Sade','Song_name':'Love Is King','Genre' :'Smooth Jazz & soul','Release_year':'1983'}
# track08 = { 'Artist':'Chris Botti','Song_name':'Good Morning Heartache','Genre' :'Jazz & RnB','Release_year':'2005'}
# track09 = { 'Artist':'Norman Brown','Song_name':'After The Storm','Genre' :'Smooth Jazz','Release_year':'1994'}
# track10 = { 'Artist':'Grover Washington Jr','Song_name':'Take Five','Genre' :'Smooth Jazz','Release_year':'1992'}

# fav_songs = [track00, track01, track02]
# #keys = { 'Artist':'','Song_name':'','Genre' :'','Release_year':''}
# print (fav_songs)

#print (fav_songs.keys())

# print("Keys before Dictionary Updation:")
# keys = fav_songs.keys()
# print(keys)

# fav_songs.update({'Artist':'David Sanborn', 'Song_name':' Maputo', 'Genre':'Smooth Jazz', 'Release_year':'1983'})
# print ("\n After songs dictionary is updated: ")
# print (keys)

fav_songs = {'Artist':'George Benson','Song_name':'Affirmation','Genre' :'Smooth Jazz','Release_year':1976 }
print (fav_songs)

print (fav_songs['Artist'])

print (fav_songs.keys())

fav_songs['Time'] = '6:00'
print (fav_songs)
#del fav_songs['Time'] = '6:00'
#print (fav_songs)

songs_dict = { 
            "Artist":"Bob James",
            "Song_name":"Raise The Roof",
            "Genre" :"Smooth Jazz",
            "Release_year":1999
            }
    print (songs_dict)


songs_dic.append({
            "Artist":"George Benson",
            "Song_name":"Affirmation",
            "Genre" :"Smooth Jazz",
            "Release_year": "1976" })
    print (songs_dict)