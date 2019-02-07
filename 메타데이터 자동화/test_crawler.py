from bs4 import BeautifulSoup
import urllib.request
count = 0
with urllib.request.urlopen("http://factcheck.snu.ac.kr/") as url:
    doc = url.read()
    soup = BeautifulSoup(doc, "html.parser")
    divisions = soup.find_all("div", class_="prg fcItem_li")
    for division in divisions:
        print(division)
        print(division.a.text)
        print(division.a["href"])
        count += 1
print(count)