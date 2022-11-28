import json

file =  open("favourite.json","w")

favouriteMovie = {
    "name" : "Hacksaw Ridge",
    "date" : 2016,
    "director" : "Mel Gibson",
    "main actor" : "Andrew Gardield",
    "genre" : ["war","drama","historical fiction"]
}

json.dump(favouriteMovie, file, indent = 6)