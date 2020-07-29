import time
from datetime import datetime as dt
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

siteN = int(input("Number of sites you want to block: "))

for i in range(0, siteN):
    website_l = []
    website = input("Enter the site url to block: ")
    website_l.append(website)

startTime = int(input("Enter the starting time to block the site: "))
endTime = int(input("Enter the end time to block the site: "))

while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,startTime) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,endTime)):
        with open(hosts_path,"r+") as file:
            content = file.read()
            for websites in website_l:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hosts_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_l):
                    file.write(line)
            file.truncate()
        print("Study time....")
    time.sleep(300)