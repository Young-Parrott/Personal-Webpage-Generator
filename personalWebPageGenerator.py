## write a program that asks the user for his or her name, 
## then asks the user to enter a sentence that describes himself or herself.
## Once the user has entered the requested input, the program should create an html file, 
## containing the input for a simple Web page.
import webbrowser
import os
from urllib.request import pathname2url

def generateHTMLFile(n, d):
    
    #open file
    html_file = open('webpage.html', 'w')
    if(html_file):
        #generate html to go into file with arguement data
        html_code = """<!DOCTYPE html>
                     <html>
                     <head>
                     <title> {} </title>
                     </head>
                     <body>
                     <h1> {} </h1>
                     <p> {} </p>
                     </body>
                     </html>"""
        .format(n,n,d)
    else:
        print('Error opening html_file.')
                
    #write html code to file   
    html_file.write(html_code)
    #close the file
    html_file.close()
    

def main():
    print('''This project generates a simple HTML Web Page in a file called webpage.html using the name and description you provide for yourself. ''')
    try:
        #gather input
        name = input('What is your name?: ')
        description = input('Describe yourself.: ')
        
        #call html genterator function
        generateHTMLFile(name, description)
        
        #open the file in the webbrowser
        url = 'file:{}'.format(pathname2url(os.path.abspath('webpage.html')))

        webbrowser.open(url)
        

    except OSError as err:
        print(err)

#call main
if __name__ == '__main__':
    main()
