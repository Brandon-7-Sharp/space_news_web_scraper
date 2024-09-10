######################################################################################
#
# WriteSummarized:
#   Class located in the summarize_data.py file
#   Main task is writing the summarized data to a SummarizedArticle# for each article's summarized data
#
######################################################################################

import os

class WriteSummarized:
    # Method that writes the refined data(gives as paragraphs variable) to the specified file
    def write_summarized(self, paragraphs: str, i: int, path_pro: str) -> None:
        # Finds the path for the specified file
        file_to_read_pro: str = str(os.path.dirname(os.path.dirname(__file__))) + path_pro + str(i+1)
        # Opens the file to be written to
        file1 = open(file_to_read_pro, "w")
        # Loops through the paragraphs in the paragraphs variable and writes them to the file
        for paragraph in paragraphs:
            file1.write(str(paragraph))
        # Closes the file
        file1.close()