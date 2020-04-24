# Summary Of Data:
import requests
from bs4 import BeautifulSoup
import pandas as pd

labels = []
data = []

url = "Add url Of Desired Stock"

request = requests.get(url)
response = request.status_code
if response == 200:
    pass
else:
    print("Server responded with", response)
soup = BeautifulSoup(request.content, "html.parser")
table = soup.find("div", id="quote-summary")
rows = table.find_all("tr")
for row in rows:
    labels.append(str(row.find_all("td")[0].text))
    data.append(str(row.find_all("td")[1].text))
cols = {"Field": labels, "Data": data}
df = pd.DataFrame(cols)

df.to_csv("Price_Summary.csv")

# Historical Data:
import pandas as pd
import requests
from bs4 import BeautifulSoup

Date = []
Open = []
High = []
Low = []
Close = []
Adj_Close = []
Volume = []

url = "Add url Of Desired Stock"

request = requests.get(url)
response = request.status_code
if response == 200:
    pass
else:
    print("Server responded with", response)
soup = BeautifulSoup(request.content, "html.parser")
table = soup.find("table", class_="W(100%) M(0)")
rows = table.find_all("tr", class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")

for row in rows:
    Date.append(str(row.find_all("span")[0].text))
    Open.append(str(row.find_all("span")[1].text))
    High.append(str(row.find_all("span")[2].text))
    Low.append(str(row.find_all("span")[3].text))
    Close.append(str(row.find_all("span")[4].text))
    Adj_Close.append(str(row.find_all("span")[5].text))
    Volume.append(str(row.find_all("span")[6].text))

cols = {
    "Date": Date,
    "Open": Open,
    "High": High,
    "Low": Low,
    "Close": Close,
    "Adj Close": Adj_Close,
    "Volume": Volume,
}
df = pd.DataFrame(cols)

df.to_csv("Stock_Data.csv")

