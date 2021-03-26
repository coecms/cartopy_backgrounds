#!/bin/bash

for res in 360,180 720,360 1440,720 3600,1800
do
    IFS=',' read w h <<<"${res}"
    # Blue marble plus bathymetry
    echo curl "https://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=526312&cs=rgb&format=PNG&width=${w}&height=${h}" --output world_${m}_${w}x${h}.png
    curl "https://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=526312&cs=rgb&format=PNG&width=${w}&height=${h}" --output bluemarble_aug_${w}x${h}.png

    # Topography
    echo curl "https://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=196466&cs=rgb&format=PNG&width=${w}&height=${h}" --output bluemarble_aug_${w}x${h}.png
    curl "https://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=196466&cs=rgb&format=PNG&width=${w}&height=${h}" --output bluemarble_aug_${w}x${h}.png

done

wget "https://eoimages.gsfc.nasa.gov/images/imagerecords/147000/147190/eo_base_2020_clean_3600x1800.png"

for res in 360x180 720x360 1440x720 3600x1800
do
    echo convert eo_base_2020_clean_3600x1800.png -resize ${res} explorer_${res}.png
    convert eo_base_2020_clean_3600x1800.png -resize ${res} explorer_${res}.png
done


wget "https://eoimages.gsfc.nasa.gov/images/imagerecords/55000/55167/land_lights_16384.tif"

for res in 360x180 720x360 1440x720 3600x1800
do
    echo convert land_lights_16384.tif -filter Point -resize ${res}  lights_${res}.png
    convert land_lights_16384.tif -filter Point -resize ${res}  lights_${res}.png
done

