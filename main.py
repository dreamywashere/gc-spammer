import requests, random, os, threading, time
from random import choice
from time import sleep

count = 0
p = []
thread1 = []
token = "TOKEN HERE" # Put the token with the gcs
proxies = open("Data/proxies.txt").read().splitlines()
for line in open("Data/groups.txt"):
    p.append(line.strip("\n"))
userid = 0

# Clear console
def clear():
    os.system("cls||clear")

# Main menu
def menu():
    print(f"""
                 [<3] Developed by Dreamyy#1337, https://dreamy.miami

                 [!] Token Loaded: {token[:20]}************************...

                  [1] - Add user to groups        |      [4] - Group scraper
                  [2] - Remove user from groups   |      [5] - Rename all groups
                  [3] - Count the groups          |
    """)

# Get random proxy from proxies.txt
def getProxy():
    return random.choice(proxies)

# Add user to group
def add():
    global count
    headers = {"Authorization" : token}
    url = f'https://discord.com/api/v9/channels/{gcs}/recipients/{userid}'
    try:
        requests.put(url, headers=headers, proxies={"http": 'http://' + getProxy()})
        print(getProxy())
        count+=1
    except Exception as e:
        print(f"[!] Failed to add user to {gcs}")
    print(f'{userid} added to [{gcs}]')
    os.system(f"title Added to {count} groups")

# Remove user from group
def remove():
    global count
    headers = {"Authorization" : token,
               "Content-Type" : "application/json"}
    url = f'https://discord.com/api/v9/channels/{gcs}/recipients/{userid}'
    try:
        requests.delete(url, headers=headers, proxies={"http": 'http://' + getProxy()})
        count+=1
    except Exception as e:
        print(f"[!] Failed to remove user from {gcs}")
    print(f'Removed user from {gcs}')
    os.system(f"title Removed from {count}")


# Count the groups from groups.txt
def countgroups():
    f = open("groups.txt", "r")
    grps = 0
    for lines in f:
        if line != "\n":
            grps += 1
    f.close()
    print(f"There are {grps} groups")
    input()

# Rename the groups
def rename():
    headers = {"Authorization" : token, "Content-Type" : "application/json"}
    url = f'https://discord.com/api/v9/channels/{gcs}'
    payload = {"name": f'{name}'}
    try:
        requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'http://' + getProxy()})
    except Exception as e:
        print(f"[!] Failed to rename {gcs}")

def scraper():
    s = open("scrapedgcs.txt", "w")
    headers = {"Authorization": token}
    url = "https://discord.com/api/v9/users/@me/channels"
    try:
        groups = requests.get(url=url, headers=headers).json()
        for channel in groups:
            if(channel['type'] == 3): 
                print('[!] Scraped ' + channel['id'])
                s.write(channel['id'] + "\n")
    except Exception as e:
        print("[!] Failed to scrape!")

# Call the main menu function
menu()

# Option system
option = int(input('> '))
if option == 1:
    userid = input("Target ID > ")
    for gcs in p:
        thread = threading.Thread(target=add, args=(), daemon=True)
        thread.start()
        thread1.append(thread)
    for thread in thread1:
        thread.join()
elif option == 2:
    userid = input("Target ID > ")
    for gcs in p:
        thread = threading.Thread(target=remove, args=(), daemon=True)
        thread.start()
        thread1.append(thread)
    for thread in thread1:
        thread.join()
elif option == 3:
    countgroups()
elif option == 4:
    scraper()
elif option == 5:
    name = input("Name > ")
    for gcs in p:
        thread = threading.Thread(target=rename, args=(), daemon=True)
        thread.start()
        thread1.append(thread)
    for thread in thread1:
        thread.join()
else:
    print('Invalid Choice')



