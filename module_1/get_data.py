######################################################################################
#
# WebLinkReader:
#   Class located in the get_data.py file
#   Main task for this class is to read the weblinks stored in the Weblinks.txt file and 
#       write the strings to an array, which it returns.
#
# WebScraper:
#   Class located in the get_data.py file
#   Main task is going to the websites stored in the webArray, and writing their raw HTML
#       data to individual files labeled RawArticle# in the Data->Raw directory
#
######################################################################################

import os
import requests

# Class for getting the web links in a txt file and storing them in an array
class WebLinkReader:
    # Initializes a WebLinkReader object with a var link that stores the path to the Weblinks.txt file
    def __init__(self, path: str) -> None:
        self.link = str(os.path.dirname(os.path.dirname(__file__))) + "/" + path
        # sefl.file = 

    # Reads the links in the text file from self.link, and returns them in a string
    def read_web_links(self):
        # Opens the file for reading to read the weblinks
        file = open(self.link, "r")
        # Creates an array that reads the file and splits the data where there are commas
        webArray: list[str] = (file.read()).split(",")
        # Removes the last index that has nothing in it
        webArray.pop()
        return webArray
    
# Class for reading the raw data of a wblink and storing it in a file
class WebScraper:
    # Method that scrapes the raw HTML from the given weblinks and stores them in individual files
    def scrape_data(self, link: str, i: int, path_raw: str) -> None:
        # Get request for the html in the webpage
        webpage: str = requests.get(link).text
        # Opens the file Article[i+1] to write the data, i is the iteration of the loop
        file1 = open(str(os.path.dirname(os.path.dirname(__file__))) + path_raw + str(i + 1), "w", encoding="utf-8")
        # Adds the paragraph data to the text file
        for paragraph in webpage:
            file1.write(str(paragraph))
        # Closes the file
        file1.close()

