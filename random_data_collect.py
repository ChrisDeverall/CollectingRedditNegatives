import pandas as pd
from psaw import PushshiftAPI 
import numpy as np
import datetime
import time
import sys

def get_random_posts(start_date, end_date, number_splits, subreddit_df, filename):
    #pass dates as datetime objects
    

    time_intervals = np.round(np.linspace(int(time.mktime(start_date.timetuple())), int(time.mktime(end_date.timetuple())),number_splits)).astype(int)
    api = PushshiftAPI()
    
    for index in range(number_splits-1):
        print(index)
        start_time = time_intervals[index]
        end_time = time_intervals[index+1]
        sub_reddit_rand = np.random.choice(subreddit_df.index, p=subreddit_df["chance"])
        print(sub_reddit_rand)
        gen = api.search_submissions(subreddit = sub_reddit_rand,
                         limit=100,
                         before = end_time,
                         after = start_time)
        
        new_selftext_list = []
        new_title_list = []
        new_id_list = []
        new_date_list = []
        for post in gen:
            try:
                this_selftext= post.selftext
                this_title = post.title
                this_id = post.id
                this_date = post.created_utc

                
                new_selftext_list.append(this_selftext)
                new_title_list.append(this_title)
                new_id_list.append(this_id)
                new_date_list.append(this_date)
                
            except:
                print("Error")
        
        
        append_df = pd.DataFrame([new_selftext_list, new_title_list, new_id_list, new_date_list]).T
        
        
        with open(filename, 'a') as f:
            append_df.to_csv(f, header=False)

        print(len(new_selftext_list))
    return



start_year = int(sys.argv[1])
start_month = int(sys.argv[2])
start_day = int(sys.argv[3])

end_year = int(sys.argv[4])
end_month = int(sys.argv[5])
end_day = int(sys.argv[6])

n_splits = int(sys.argv[7])

filename = sys.argv[8]

subreddit_df = pd.read_csv("ranked_subreddits.csv")[["chance","subreddit_name"]].set_index("subreddit_name")

get_random_posts(datetime.date(start_year,start_month,start_day), datetime.date(end_year,end_month,end_day), n_splits, subreddit_df, filename)


#To get 8 sets of 100 posts from Jan 1 2020 to Jan 30 2020 and append data to file "my_negatives.csv", type: python3 random_data_collect.py 2020 1 1 2020 1 30 8 my_negatives.csv
