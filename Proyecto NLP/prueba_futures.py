import pandas as pd
import snscrape.modules.twitter as sntwitter
import time
from concurrent.futures import ThreadPoolExecutor



def process_1():
    attributes_container = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('respuesta since:2022-04-15 until:2022-07-16').get_items()):
        if i>1000000:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    data1 = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    data1.to_csv('data1.csv')
    
        
def process_2():
    attributes_container = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('respuesta since:2021-04-15 until:2021-07-16').get_items()):
        if i>1000000:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    data2 = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    data2.to_csv('data2.csv')
    
def process_3():
    attributes_container = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('respuesta since:2020-04-15 until:2020-07-18').get_items()):
        if i>1000000:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    data3 = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    data3.to_csv('data3.csv')


def process_4():
    attributes_container = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('respuesta since:2019-04-16 until:2019-07-18').get_items()):
        if i>1000000:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    data4 = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    data4.to_csv('data4.csv')


def process_5():
    attributes_container = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('respuesta since:2018-04-16 until:2018-07-18').get_items()):
        if i>1000000:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    data5 = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    data5.to_csv('data5.csv')


def process_6():
    attributes_container = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('respuesta since:2017-04-16 until:2017-07-18').get_items()):
        if i>1000000:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    data6 = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    data6.to_csv('data6.csv')


start = time.perf_counter()



processes = [process_1, process_2, process_3, process_4,process_5, process_6]

def run_io_tasks_in_parallel():
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(proc) for proc in processes]
        for running_task in running_tasks:
            running_task.result()

run_io_tasks_in_parallel()



data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')
data3 = pd.read_csv('data3.csv')
data4 = pd.read_csv('data4.csv')
data5 = pd.read_csv('data5.csv')
data6 = pd.read_csv('data6.csv')

data_final = data1.concat(data2,data3,data4,data5,data6)
print(data_final)
data_final.to_csv('data_final.csv')


        
end = time.perf_counter()
print(f'Finished in {round(end-start, 2)} seconds') 

