import requests, random, os, threading, time, json
from random import choice
from time import sleep

count = 0
thread1 = []
p = []
token = "UR TOKEN HERE DONT COME TO DMS AND ASK ME : MEN WHERE TF I PUT THE TOKEN PLS SAY !!" # Put the token with the gcs so i can log your token and destroy your account
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

                  [1] - Add user to groups        |  [4] - Group scraper        |  [7] - Send msg to groups (bug)
                  [2] - Remove user from groups   |  [5] - Rename all groups    |  [8] - Muli Group Creator
                  [3] - Count the groups          |  [6] - Scrape Proxies       |  [9] - Info
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
        count+=1
    except Exception as e:
        print(f"[!] Failed to add user to {gcs}")
    print(f'{userid} added to [{gcs}]')
    os.system(f"title Added to {count} groups")
    time.sleep(2)

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
    time.sleep(2)


# Count the groups from groups.txt
def countgroups():
    f = open("Data/groups.txt", "r")
    grps = 0
    for lines in f:
        if line != "\n":
            grps += 1
    f.close()
    print(f"There are {grps} groups")
    time.sleep(2)

# Rename the groups
def rename():
    headers = {"Authorization" : token, "Content-Type" : "application/json"}
    url = f'https://discord.com/api/v9/channels/{gcs}'
    payload = {"name": f'{name}'}
    try:
        requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'http://' + getProxy()})
    except Exception as e:
        print(f"[!] Failed to rename {gcs}")
    time.sleep(2)

# Scrape groups that's in the acc 
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
    time.sleep(2)

# Scrape http proxy from proxyscrape
def scrapeproxy():
    print("Getting proxies..")
    f = open("Data/proxies.txt", 'wb')
    r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
    f.write(r1.content)
    f.close()
    print("Done")
    time.sleep(2)

# Send message to all groups (bugged)
def sendmsg():
    headers = {"Authorization" : token}
    url = f'https://discord.com/api/v9/channels/{gcs}/messages'
    payload = {"content": message,
               "nonce": gcs}
    try:
        requests.post(url=url, headers=headers, json=payload,proxies={"http": 'http://' + getProxy()})
        print(f'Sent message to {gcs}')
    except Exception as e:
        print(f'Failed to send message to {gcs}')

# Info about the spammer
def info():
    print("> Made by Dreamyy#1337, https://github.com/dreamywashere, dreamy.miami.\n> Special thanks to pix, gowixx, for helping me with it a bit <3")
    time.sleep(5)

# Yes i fucked my mind 2 hrs trying to figure out how can i do it and i failed and i raged over my keyboard :D
def multicreator():
    print("No ty")
    time.sleep(2)
    # Nutin cuz my brain is dead rn


while True:
    clear()
    menu()
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

    elif option == 6:
        scrapeproxy()

    elif option == 7:
        message = input("Message > ")
        for gcs in p:
            thread = threading.Thread(target=sendmsg, args=(), daemon=True)
            thread.start()
            thread1.append(thread)
        for thread in thread1:
            thread.join()
    elif option == 8:
        multicreator()

    elif option == 9:
        info()

    else:
        print('Invalid Choice')
    

# Skidders on top, if u skid it and sell it for owo coins at least puy #Dreamy at the top <3