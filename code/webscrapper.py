#Working with websites
from bs4 import BeautifulSoup 

#Creating a driver to work with js 
import selenium.webdriver as webdriver

#opening and messing with json 
import json 

#Storing stuff to db 
import firebase_admin from firebase_admin
import credentials from firebase_admin
import firestore from google.cloud
import storage

#more url requests 
import urllib.request 
#general formatting fun 
import os, sys, io
from google.cloud import vision
from google.cloud.vision import types

#look up lat and long 
from uszipcode import SearchEngine

#credential Setup
googleCredentials = ""
fire_Storage_Bucket_url = ""


#Grab this from Google, they require this set up now
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= googleCredentials
#For printing out text that includes emojiis 
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#This class stores the data of an instagram object pulled
class IG_Entry: def __init__(self):
	self.timeStamp = 0
 	self.image = "www.google.com"
	shortlinkelf.id = 0 self.shortlink = "" 


#setup the db connection 
cred = credentials.Certificate(googleCredentials)
firebase_admin.initialize_app(cred,{
 'storageBucket': fire_Storage_Bucket_url}) 
db = firestore.client()

#This is for images imageStorage = storage.Client()
bucket = imageStorage.bucket(fire_Storage_Bucket_url)

#url for grabbing most recent posts on a tag 
baseUrl = "https://www.instagram.com/explore/tags/"
#Store overall data until cleaned 
baseList = list()
#url for grabbing potential location data from post 
basePageUrl = "https://www.instagram.com/p/"
#Use this to look at different tags 
tag = 'Junco'

#I am using Chrome, but whatever you use you need to install
# the correct driver or you'll get a funky error
driver = webdriver.Chrome() driver.get(baseUrl+tag + '/')

#Parse the html to get those jsons 
soup = BeautifulSoup(driver.page_source, "html.parser")

#The 6th scripts hides what we need 
scriptWeWant = soup.findAll("script")[7] stringText = "{" + str(scriptWeWant)[53:-10] 
testJson = json.loads(stringText)
#For each object on the page, we're gonna store it:
for i in range(0,(len(testJson['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'])-1)): 
	x = IG_Entry()
	x.timeStamp = testJson['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['taken_at_timestamp']
	x.image = testJson['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['display_url']
	x.id = testJson['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['id']
	x.shortlink = testJson['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['shortcode'] 
	baseList.append(x)

#Now, we have about 70 of the most recent posts in this tag.
#Let's see who has location data!
search = SearchEngine(simple_zipcode=True) 
client = vision.ImageAnnotatorClient() 
for page in baseList:
	driver.get(basePageUrl+page.shortlink) 
	soup = BeautifulSoup(driver.page_source, "html.parser")
	scriptWeWant = soup.findAll("script")[8]
	stringText = "{" + str(scriptWeWant)[53:-10]

 #Sometimes the json is empty, so need to check for that first before cutting
	if(len(stringText) > 100):
 		testJson = json.loads(stringText)
 		if testJson['entry_data']['PostPage'][0]['graphql']['shortcode_media']['location']:
			location = testJson['entry_data']['PostPage'][0]['graphql']['shortcode_media']['location']
 			if location and json.loads(location['address_json'])['country_code'] == "US":
				zipcode = json.loads(location['address_json'])['zip_code'].split(',')[0] 
				if len(zipcode) > 3: 
					loca = search.by_zipcode(zipcode).to_dict()
					lat = loca["lat"] 
					lon = loca["lng"] 
					if lon and lat: #Store image
						urllib.request.urlretrieve(page.image, page.shortlink+ ".jpg") 
						file_name = os.path.join(os.path.dirname(__file__),page.shortlink+ ".jpg")
 						with io.open(file_name, 'rb') as image_file:
							content = image_file.read()
							image = types.Image(content=content)
							response = client.label_detection(image=image)
							labels = response.label_annotations #Check if Junco in annotation 
							for label in labels:
								if label.description == "Bird":
									blob = bucket.blob(page.shortlink)
									blob.upload_from_filename(page.shortlink+ ".jpg")
									print("bird located!") 
									doc_ref = db.collection(u'BirdCV').document() doc_ref.set({u'timestamp': page.timeStamp,u'image': page.image, u'shortlink' :page.shortlink, u'lat' : lat,u'long' : lon, u'Verified': "True",u'Score': label.score, u'Topicality': label.topicality})

 driver.close()