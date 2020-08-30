"""
python3 -m venv 'name'-env
'name'-env\Scripts\activate.bat
pip install bs4
pip install requests
pip install matplotlib
"""
"""I learned how to do this from: https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184"""

from bs4 import BeautifulSoup
import requests
import csv

for i in range(1, 50):
    if i > 10:
        i += 1
    if i > 25:
        i +=1
    if i > 35
        i +=1
    #idea for urls: once into 9:45+ range, start skipping pages, bc there's a TON of people running in that range, need to narrow it down to get to 10:50 range
    # takes approx 3mins to run per page (on laptop); as loop currently set, have 22 pages
    url = 'https://www.athletic.net/TrackAndField/Division/Event.aspx?DivID=98249&Event=60&filter=12&page=' + str(i) + '&restrict=1'
    response = requests.get(url, timeout = 5)
    content = BeautifulSoup(response.content, "html.parser")

    i = 0
    sophList = []
    senList = []

    for results in content.find_all('a', href = True):
    
        resultURL = results.get('href')
    
        if "Athlete" in resultURL:
            i +=1
            # this break is for testing; stops the code at one athlete
        
            #this section of code opens each athlete's bio to find their PR's
            url2 = "https://www.athletic.net/TrackAndField/" + resultURL
        
            #this next section searches the pages brought by the code in the above section for times
            response2 = requests.get(url2, timeout = 5)
            content2 = BeautifulSoup(response2.content, "html.parser")
            #print(content2)
        
            seasonRecordSB = content2.find("div", attrs={"uib-collapse": "seasonRecordsCollapsed"})
            seasonTablesList = seasonRecordSB.find_all("table", attrs = {"class":"table table-sm histEvent"})
        
            for table in seasonTablesList:
                header = table.find("h5").getText()
            
                if "3200" in header:
                
                    for line in table.find_all("tr", attrs={"class":"L4 histSeason"}):
                    
                        try:
                            for year in line.find_all("td", attrs={"style":"width: 115px;"}):
                        
                                year = year.getText()
                        
                                if "2017 Outdoor" in year:
                                    timeLine = line.find('a')
                                    time = timeLine.getText()
                                
                                    sophList.append(time)
                                    print(time)
                            
                                try:
                                    if "2019 Outdoor" in year:
                                        timeLine = line.find('a')
                                        time = timeLine.getText()
                                
                                        senList.append(time)
                                        print(time)
                                except:
                                    print("error")
                        except:
                            print("error")

rows = zip(sophList,senList)

with open("times.csv", 'w') as file:
    wr = csv.writer(file)
    wr.writerow(("sophTimes", "seniorTimes"))
    for row in rows:
        wr.writerow(row)
file.close()
