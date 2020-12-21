import os
import csv

#Opens the txt file and grabs data to be formated into an exported csv file
#ckresnye Spring 2019

def txtToCsv():
    txtFile = open("ebd_daejun_relJan-2019.txt", "r", encoding="utf8")
    with open("textBigUS.csv", "w", newline='',encoding="utf8") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter = ",", quotechar ="\"", quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(["ID", "observations","age","country","countryCode",
                           "localType","latitude","longitude","obsDate","observerID","sampNumber","duration","effortArea","observerNums",
                           "speciesReported","groupID","tripComment","speciesComment"])
        i = 0
        #This loop grabs each individual entry from the text files and maps it to a column
        for entry in txtFile:
            newEntry = {}
            newEntry["global"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]
            
            newEntry["editDay"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["taxCat"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]
            entry = entry[entry.find("\t")+1:]
            
            newEntry["commonName"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["sciName"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]
            entry = entry[entry.find("\t")+1:]
            entry = entry[entry.find("\t")+1:]

            newEntry["observations"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]
            entry = entry[entry.find("\t")+1:]
            entry = entry[entry.find("\t")+1:]

            newEntry["age"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["country"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["countryCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["state"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["stateCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]
            
            newEntry["county"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["countyCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["ibaCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["bcrCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["usfwsCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["next"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["atlasBlock"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["localID"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["localType"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["latitude"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["longitude"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["next"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["obsDate"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["observerID"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["sampNumber"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["protocolType"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["protocolCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["projectCode"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["next"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["duration"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["effortArea"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["observerNums"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["speciesReported"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["groupID"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["hasMedia"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]
            
            newEntry["approved"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["reviewed"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["reason"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["tripComment"] = entry[0:entry.find("\t")]
            entry = entry[entry.find("\t")+1:]

            newEntry["speciesComment"] = entry[0:entry.find("\t")]

            if newEntry["countryCode"] == "US":
                csvWriter.writerow([i, newEntry["observations"],newEntry["age"],newEntry["country"],newEntry["countryCode"], newEntry["localType"], newEntry["latitude"],newEntry["longitude"],
                                    newEntry["obsDate"], newEntry["observerID"], newEntry["sampNumber"],  newEntry["duration"], newEntry["effortArea"], newEntry["observerNums"], newEntry["speciesReported"],
                                    newEntry["groupID"],newEntry["tripComment"], newEntry["speciesComment"]])
                i += 1
        print("I added " + str(i) + " records to the csv")
            

txtToCsv()
