# from bs4 import BeautifulSoup
# import requests

# content = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# soup = BeautifulSoup(content,"lxml")
# User_skill = input("Your skill set:-\n")
# userskill = User_skill.lower().split()
# Jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

# for job in Jobs:
#     skills = job.find('span',class_="srp-skills").text.replace(" ","")
#     for i in userskill:
#             if i in skills:
#                 Company_name = job.find('h3',class_="joblist-comp-name")
#                 Term = job.find("ul",class_="top-jd-dtl clearfix").li.text
#                 Description = job.find('span',class_="srp-skills")
#                 companies = Company_name.text.replace(" ","")
#                 description = Description.text.replace(" ","")
#                 link = job.find('a')
#                 print("\n")
#                 print("Company Name:-",companies.strip())
#                 print("Skills:-",description.strip())
#                 print("Duration:",Term.replace("card_travel",""))
#                 print("Link:-",link.get("href"),end="")
#                 break

# a = ['python','aws','git']
# ins = input().split()
# flag = 0
# print(ins)
# for i in ins:
#     if i not in a:
#         print("hi")
#     else:
#         print("Contains your unknow branch")


