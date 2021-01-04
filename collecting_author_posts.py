import pandas as pd
from psaw import PushshiftAPI 
import numpy as np
import csv

def get_author_posts(list_of_authors, filename):
    

    api = PushshiftAPI()
    counter = 0
    post_counter = 0
    for author in list_of_authors:
        gen = api.search_submissions(author=author,filter=['author',"created_utc","selftext","title", "id","num_comments","subreddit"], limit =20, after = 1420070400)
        
        for post in gen:
            try:
                this_selftext= post.selftext
                if this_selftext!="" and this_selftext !=" " and this_selftext !="[removed]":
                    this_title = post.title
                    this_id = post.id
                    this_date = post.created_utc
                    this_author = post.author
                    this_num_comments = post.num_comments
                    # this_link = post.link
                    this_subreddit = post.subreddit
                    fields = [str(this_selftext),str(this_title),str(this_id),str(this_date),str(this_author),str(this_num_comments),str(this_subreddit)]
                    with open(filename, "a") as f:
                        writer = csv.writer(f)
                        writer.writerow(fields)
                    post_counter+=1
            except Exception as e:
                print(e)

        if counter%50==0:
            print("author count:", counter)
            print("post count:", post_counter)
            print()
        counter +=1
    return

#anurag, please use this use the below command for your set of authors:
# new_authors = list(pd.read_csv("anurag_authors.csv")["author"])

new_authors = list(pd.read_csv("kunal_authors.csv")["author"])
get_author_posts(new_authors, "author_posts.csv")