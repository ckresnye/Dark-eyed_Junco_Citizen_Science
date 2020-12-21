# Dark-eyed_Junco_Citizen_Science
Python project exploring the accuracy of tagged social media data regarding the range and migration habits of the dark-eyed junco bird.

## Project Overview
This project consists of four components:
* Importing and Analyzing known bird sighting range from the [EBird](https://ebird.org/home) dataset
* Webscrapping Instagram for posts tagging dark-eyed juncos
* Using Google Cloud's computer vision API to verify the scrapped image contains a bird
* Comparing the known ranges with the social media tagged posts

## About the Dark-eyed Junco
The dark-eyed junco is a common sparrow found across north america. This small bird was chosen as the first species for this project as its broad range and population size may lead to more bird watchers observing it and posting about it on social media. 

<img src="https://github.com/ckresnye/Dark-eyed_Junco_Citizen_Science/blob/main/images/dark-eyed-junco-range.jpg" alt="Dark Eyed Junco Range" width="300px">

## Project Parts
### Importing verified Data Points
The first step was to cleanup the data to be analyzed, and format it for further analysis. This involved converting txt files provided by Ebird to CSV, as shown in the file dataFormatter.py.

### Webscraping for Junco Posts with Verification
The second step was to grab new data points from Instagram with a webscrapper (file webscrapper.py). This pulls the posts that are tagged "junco", filters results to those with location data, then verifies the image contains a bird using Google Cloud's Vision API. This program also uses a zipcode lookup for locations. If images are found to contain birds, the image and data are stored in firebase storage.

### Comparing Results
TODO - write up in progress

## Project Results
TODO - write up in progress

## Future Work
TBD - write up in progress
