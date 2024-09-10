######################################################################################
#
# FileScraper:
#   Class located in the refine_data.py file
#   Main task is using Beautiful Soup to grab only the paragraph data from the raw HTML
#       stored in the RawArticle# for each article. This refined data is then returned.
#
# WriteData:
#   Class located in the refine_data.py file
#   Main task is writing the refined data to a processedArticle# for each article's data
#
######################################################################################


import os
from bs4 import BeautifulSoup

# Class for refining the data that was obtained in the get_data
class FileScraper:
    # Method that reads the raw html in the rawArticle[i] file and uses BeautifulSoup to grab only the paragraphs of the webpage
    def scrape_data(self, i: int, path_raw: str) -> str:
        # Opens the file that has the raw data for the specified article
        fileToReadRaw = open(str(os.path.dirname(os.path.dirname(__file__))) + path_raw + str(i + 1))
        # Utilizing beautiful soup, we create an html parser 
        soup = BeautifulSoup(fileToReadRaw, "html.parser")
        # It goes into a div and accesses the information in the id where it equals "article-body" and stores that data in the paragraphs string
        paragraphs: str = soup.findAll('div', attrs={"id":"article-body"})
        # Returns a string will all the paragraph in
        return paragraphs
    
# Class for writing the refined data to a specified file
class WriteData:
    # Method that writes the refined data(gives as paragraphs variable) to the specified file
    def write_data(self, paragraphs: str, i: int, path_pro: str) -> None:
        # Finds the path for the specified file
        file_to_read_pro: str = str(os.path.dirname(os.path.dirname(__file__))) + path_pro + str(i+1)
        # Opens the file to be written to
        file1 = open(file_to_read_pro, "w")
        # Loops through the paragraphs in the paragraphs variable and writes them to the file
        for paragraph in paragraphs:
            file1.write(str(paragraph.text))
        # Closes the file
        file1.close()

