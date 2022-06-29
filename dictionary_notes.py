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

print(countrys)

China = countrys.setdefault('China','Bejen')
canada = countrys.setdefault('Canada' ,'Ottowa')
print('countrys =',countrys)
print('China =' ,China)
print('canada =', canada)
print (countrys)

#countrys.setdefault ({'China': 'Bejen', 'Canada': 'Ottawa'})
#print(countrys)

### Activity 3 fav_songs

# keys: artist, song_name, genre, release_year

fav_songs = [
    {"George Benson":"Affirmation" : "Smooth Jazz":"1976",
    "Bob James":"Since I Fell For You":"Smooth Jazz":"1986",
    "Bob James" : "Raise The Roof" : "Smooth Jazz" : "1999",
    "Bony James" : "Joy Ride" : "Smooth Jazz" : "1999", 
    "Ron Fattorusso" : "No Es Facil" : "Latin Smooth Jazz" : "2004",
    "Incognito" : "Pieces Of A Dream" : "Smooth Jazz" : "1993",
    "Sade" : "Your Love Is King" : "Smooth Jazz & soul" : "1983",
    "Chris Botti" : "Good Morning Heartache" : "Jazz & RnB" : "2005",
    "Norman Brown" : "After The Storm" : "Smooth Jazz" : "1994",
    "Grover Washington Jr" : "Take Five" : "Smooth Jazz" : "1992"}
]

fav_songs = { 'Artist' : '', 'Song_name': '', 'Genre' : '', 'Release_year' : ''}
print (fav_songs)

#print (fav_songs.keys())

