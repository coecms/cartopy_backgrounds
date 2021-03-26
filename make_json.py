#/usr/bin/env python

import json

formats = { 
        "1.0deg":  "360x180", 
        "0.5deg":  "720x360", 
        "0.25deg": "1440x720", 
        "0.1deg": "3600x1800",
        "low":  "360x180", 
        "medium":  "720x360", 
        "high": "1440x720", 
        "extrahigh": "3600x1800",
        }

months = { 
        "01" : "January", 
        "02" : "February", 
        "03" : "March", 
        "04" : "April", 
        "05" : "May", 
        "06" : "June", 
        "07" : "July", 
        "08" : "August", 
        "09" : "September", 
        "10" : "October", 
        "11" : "November", 
        "12" : "December", 
        }

months = { "08" : "August" }

data = {}
data['__comment__'] = "JSON file specifying the image to use for blue marble background images. Read in by cartopy.mpl.geoaxes.read_user_background_images."

for m in months:
    BM = {}
    BM["__comment__"] = "Blue Marble Next Generation, {}".format(months[m])
    BM["__source__"]  = "https://neo.sci.gsfc.nasa.gov/view.php?datasetId=BlueMarbleNG"
    BM["__projection__"] = "PlateCarree"

    for f in formats:
        BM[f] = "bluemarble_{}_{}.png".format(months[m].lower()[0:3],formats[f])

    # data['bluemarble_{}'.format(months[m].lower())] = BM
    data['bluemarble'] = BM


explorer = {}
explorer["__comment__"] = "Explorer Base Map: This map was developed to provide the underlying base for the Earth Observatory Explorer browse tool"
explorer["__source__"]  = "https://visibleearth.nasa.gov/images/147190/explorer-base-map/147191l"
explorer["__projection__"] = "PlateCarree"

for f in formats:
    explorer[f] = "explorer_{}.png".format(formats[f])

data['explorer'] = explorer


lights = {}
lights["__comment__"] = "Earth's City Lights"
lights["__source__"]  = "https://visibleearth.nasa.gov/images/55167/earths-city-lights/55170l"
lights["__projection__"] = "PlateCarree"

for f in formats:
    lights[f] = "lights_{}.png".format(formats[f])

data['lights'] = lights


with open('images.json', 'w') as f:
    json.dump(data, f, indent=4)

