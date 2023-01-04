from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    # This just print content line by line without any formatting.
    # print(content) 

    soup = BeautifulSoup(content,'lxml')
    """
    # Here we created instance of Beautiful soup for better formatting
    print(soup.prettify())
    """


    # For finding specific html tags you can use find
    courses_Plans_Names = soup.findAll('h5')
    courses_Plans_Price = soup.findAll('button')
    # print(courses_Plans)
    
    for i,j in zip(courses_Plans_Price,courses_Plans_Names):
        print('{:20}'.format(j.text),"Get Now " ,(i.text).split()[-1])
