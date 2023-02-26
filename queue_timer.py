from datetime import datetime
import pandas as pd
import csv

count = 0 #Lifetime queue counter will be featured in app. Also eases looping the program.

#Basic option picker stolen from the internet (https://tutorial.eyehunts.com/python/python-users-choose-from-the-list-example-code/)
def picker(options):
    for idx, item in enumerate(options):
        print("{} {}".format(idx+1, item))
        
    i = int(input("Your selection: "))
    try:
        if 0 < i <= len(options):
            return i-1
    except:
        pass    
    return None

while True:
    date = str(datetime.now().date())
    print("\nToday: ",date,"\n")
    
    #parks.csv contains data for a selection of roller coasters from three parks. This data is used to get a list of roller coasters at the selected park.
    coaster_data = pd.read_csv("parks.csv")
    parks = coaster_data["Park"].drop_duplicates()
    parks = parks.reset_index(drop=True)
    
    print("Choose a park from the list below:\n")
    parkchoice = picker(parks)
     
    parkchoice = parks[parkchoice]
    
    print("\n\nWelcome to {}! Choose a ride from the list below: \n".format(parkchoice))
    rides = coaster_data.loc[coaster_data['Park'] == parkchoice]
    rides = rides['Ride']
    rides = rides.reset_index(drop=True)
    
    ridechoice = picker(rides)
    ridechoice = rides[ridechoice]
    print("\nNow riding: {}\n\n".format(ridechoice))
    
    #Queue timer
    enter = 0
    exit = 0
    
    enterButton = int(input("Enter 1 to enter queue: "))
    if enterButton == 1:
        enter = datetime.now()
        print("Entered at: ",enter)
        
    exitButton = int(input("Enter 1 to exit queue: "))
    if exitButton == 1:
        exit = datetime.now()
        print("Exited at: ",exit)
        
    queueTime = exit - enter
    print("Time in queue: ",queueTime)
    
    #Store queue time info
    enter = str(enter)
    queueTime = str(queueTime)
    q = [parkchoice,ridechoice,date,enter,queueTime]
    f = open("queue_times.csv", 'a')
    w = csv.writer(f, lineterminator='\n')
    w.writerows([q])
    f.close()
    
    count += 1

    print("Queue time data saved. \nPress Q to ride again. Press E to exit.")
    again = input()
    if again == 'Q':
        continue
    elif again == 'E':
        print("\n\n")
        break