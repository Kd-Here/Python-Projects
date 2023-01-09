from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text.content)

""" 
#My approach to find company name
soup = BeautifulSoup(html_text,'lxml')

Jobs = soup.find_all("h3",class_="joblist-comp-name")
for i in Jobs:
    print(i.text.strip())

"""

print("Give the skill that you are not familiar with")
unfamiliar_skill = input()
unfm_s = unfamiliar_skill.split()
print("Filtering the list as per you unfamiliar skills",unfamiliar_skill,"\n")
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    flag = True
    published_date = job.find("span",class_="sim-posted").span.text
    if "few" in published_date:
        company_name = job.find("h3",class_="joblist-comp-name").text.replace(" ","")
        skills = job.find('span',class_="srp-skills").text.replace(" ","")
        link = job.header.h2.a['href']
        for i in unfm_s:
            if i not in skills:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            print(f"""Compnay Names: {company_name.strip()}\nSkills: {skills.strip()}\nLink:{link}""")
            print("\n")
        