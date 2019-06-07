import os
import csv
import string

#"id,title,url,isPaid,price,numSubscribers,numReviews,numPublishedLectures,instructionalLevel,contentInfo,publishedTime"
title = ["title"]
price = ["price"]
subscriberCount = ["subscriberCount"]
numberReviews = ["numberReviews"]
courseLengthString = ["courseLengthString"] 
courseLengthInt = ["courseLengthInt"]
percentReviews = ["percentReviews"]

csvpathInput = os.path.join("..", "Resource", "web_starter.csv")
csvpathOutput = os.path.join("..","Resource","udemy_stats.csv")

with open(csvpathInput,'r',encoding="utf8",newline="") as csvfileInput:
    csvreader = csv.reader(csvfileInput,delimiter=",")
    
    for row in csvreader:
        duration = str(row[9])
        numReview = int(row[6])
        numSubscriber = int(row[5])
        pcntReview = (numReview/numSubscriber)*100 

        title.append(row[1])
        price.append(row[4])
        subscriberCount.append(row[5])
        numberReviews.append(row[6])
        courseLengthString.append(row[9])
        courseLengthInt.append(duration[0:duration.find(" ")])
        percentReviews.append(pcntReview)

outputList = zip(title,price,subscriberCount,numberReviews,courseLengthString,courseLengthInt,percentReviews)

with open(csvpathOutput, 'w', newline="") as csvfileOutput:
    csvwriter = csv.writer(csvfileOutput, delimiter=',')
    csvwriter.writerows(outputList)
