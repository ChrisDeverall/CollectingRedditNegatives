import csv   
from psaw import PushshiftAPI 
import time
import datetime 


#Anurag please use 2017 - 2019 and Kunal change the years to 2015 (beginning) - 2017 (ending)
beginning = int(time.mktime(datetime.date(2017,1,1).timetuple()))
ending = int(time.mktime(datetime.date(2019,1,1).timetuple()))


api = PushshiftAPI()

gen = api.search_submissions(subreddit ="depression",filter=['author',"created_utc"], limit =10000000, max_results_per_request=500, after = beginning, before = ending)
counter=0
for post in gen:
    try:
        author = post.author
        created_utc = post.created_utc
        counter+=1
        fields=[str(author),str(created_utc)]
        

    except Exception as e:
        print(e)
        
    with open("positive_authors.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    if counter % 1000==0:
        print(counter)
        