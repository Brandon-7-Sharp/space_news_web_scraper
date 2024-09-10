# Python Web Scraper
## Description
This python program scrapes 10 Space related web pages for their information. It will not scrape ads, comments, or any other useless information.

## Getting Started:
### Setting Up An Environment:
First, you need to create a new enviroment with the requirements.yaml provided in this repo.

In the CMD, go to the location where you have this repo in your computer.

Then, create a new enviroment from the requirements.yaml provided in this repo, where my_yaml_env_name is the name you create for your enviroment.
```
conda create --name my_yaml_env_name --file requirements.yaml
```
Then make sure the enviroment is activated by typing the below code in the same location in the cmd, where my_yaml_env_name is the name you create for your enviroment.
```
git activate my_yaml_env_name
```

### Creating An Open AI Account:
First, go to the following link to create an account https://auth0.openai.com/u/signup/identifier?state=hKFo2SAwSV9uZXdRbXhKQXJOT3pZODhPc0lmSDlfVlpxLVlxSqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEdqTlMxRDZvb2s5SDBuVHBfemRtZkI2XzZNek1ONHlwo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q 

Choose the 'Continue with Google' or other 'Continue with' options to make creating the account as easy as possible.

### Generating an Open AI Key:
After creating an account, when loggin in choose the option 'API' as shown in the image below.
![image](https://github.com/Brandon-7-Sharp/python_web_scraper/assets/93329974/3a5f0389-15d9-45f8-9d95-985191d78f4b)

Next, click the option 'API keys' of the left side navigation bar as shown in the image below.
![image](https://github.com/Brandon-7-Sharp/python_web_scraper/assets/93329974/ab27c841-92de-4ee0-a55e-f430c84e9bbb)

Then click on the '+ Create New Secret Key' button. Give it a name and leave permissions set to 'All'.

MAKE SURE TO SAVE THE KEY THAT THEY GIVE YOU! DO NOT SHARE THIS KEY WITH ANYONE ELSE FOR SECURITY PURPOSES!

### Adding an Open AI Key to Windows Environment Path Variables:

For this part I am assuming you are using a Windows device.
First, we need to add the Open Ai key to our Windows system environment variables.
In the Windows search bar, type 'Edit System Environmnet Path Variables' and click on the option that appears below
![image](https://github.com/Brandon-7-Sharp/python_web_scraper/assets/93329974/1b292323-2380-47a8-8a65-34c506070c02)

Next, click on 'Environment Variables' as shown below.
![image](https://github.com/Brandon-7-Sharp/python_web_scraper/assets/93329974/f75d3e24-6d28-4ec0-bba9-5cebcf4f5601)

Under 'User Variables' click 'new.

Next, name the variable name 'OPENAI_API_KEY' and the variable value set to the OpenAI API Key you saved earlier.

Then click 'Ok' for all of the system tabs open.

### Using an Open AI Key:
First, for using OpenAi, you need to import 'OpenAI'.
```
from openai import OpenAI
```

Next, youu need to create an OpenAI Object, in my code I named it 'client'.
You will also need to set the OpenAI API Key to the path variable we set up earlier.
```
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
```

Lastly, you can send a request to OpenAI, where 'response' is what is given back from OpenAI, 'model' is the  version of gpt that you want to use, 'messages' is the information you want to send to OpenAI, 'role' as where the question should be formed as, and 'content' which is command or question sent to OpenAI.
```
response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Give a title and summarize the following article in 50 words or less: {paragraphs}" }])
```

## run.py:
run.py is the main python script for running this program. You should navigate to the folder that 'run.py' is located and type 'python .\run.py' to run the program.

### Imports:
We first import the python scripts from modules 1, 2, and 3 so we can acces the classes created in them.
Next we import OpenAI so we can send a request to summarize the website content.
Lastly, we import os to use for getting system paths.

```
import module_1.get_data as gd
import module_2.refine_data as rd
import module_3.summarize_data as sd
from openai import OpenAI
import os
```

### Code Body:
There are 3 main for loops that are used to iterate through text files for reading and writing data (Raw Data Files, Processed Data Files, Summarized Data Files).

First, we create variable that are the path locations for where we want the raw, processed, and summarized data to be located.
```
path_for_RAW = "/Data/raw/RawArticle"
path_for_PROCESSED = "/Data/processed/processedArticle"
path_for_SUMMARIZED = "/Data/summarized/SummarizedArticle"
```

Next, we create a WebLinkReader Object named 'web_link' and send in the 'Weblinks.txt' to have it set as the 'link' Object variable.
We also use the 'read_web_links()' function that returns the web links as values in 'webArray'.
```
web_link = gd.WebLinkReader("Weblinks.txt")
webArray: list[str] = web_link.read_web_links()
```

We then iterate through the 'webArray' for each web address, creating 10 files with the raw html data.
```
for i, link in enumerate(webArray):
    web_scraper_r.scrape_data(link, i, path_for_RAW)
```

Following, we create an Object from the FileScraper class named 'web_scraper_p' and we also create an Object from the WriteData class named 'writer'.
```
web_scraper_p = rd.FileScraper()
writer = rd.WriteData()
```

We then iterate through the 'webArray' again, creating a 'paragraphs' string that is the processed data from the raw html text file.
It is then written to the processed data text file.
```
for i, link in enumerate(webArray):
    paragraphs: str = web_scraper_p.scrape_data(i, path_for_RAW)
    writer.write_data(paragraphs, i, path_for_PROCESSED)
```

Next, we create an OpenAI Object named 'client', we set the OpenAI path for our API Key to our Windows Environment Path Value that we created earlier, and we create an Object of the WriteSummarized class named 'summarize'.
```
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
summarize = sd.WriteSummarized()
```

Lastly, we iterate through the 'webArray' again, opening the text file for the specified processed data and reading it into the 'paragraphs' string.
We then create a request to OpenAI, asking it to "Give a title and summarize the following article in 50 words or less: {paragraphs}" where 'paraghraphs' is the processed article.
And Finally, we use the 'write_summarized' function from the 'summarize' object to write the response from OpenAI.
```
for i, link in enumerate(webArray):
    with open(os.path.dirname(__file__) + path_for_PROCESSED + str(i + 1), "r") as file:
    paragraphs = file.read()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Give a title and summarize the following article in 50 words or less: {paragraphs}" }])

    summarize.write_summarized(response.choices[0].message.content, i, path_for_SUMMARIZED)
```

## get_data.py Explanation:

### Imports:
Imports os and requests.
```
import os
import requests
```

### Classes:
WebLinkReader Class: Has the '__init__(self, path: str) -> None' method that initializes each Object with the path of where the 'Weblinks.txt' is located. Has the 'read_web_links(self)' function that only takes in intself. The function opens the 'Weblinks.txt' file, reads the contents into an array, slitting the indexes by the commas between web addresses, and returns that array of web addresses.

WebScraper Class: Has the 'scrape_data(self, link: str, i: int, path_raw: str) -> None' function that takes in an object of WebScraper (self), the web address for a particular website (link), the index of which web address this is (i), and the path for where the raw txt files are stored (path_raw). The function uses the requests module to obtain the html of the specified web address, then opens the file path to where the raw data is going to be stored, iterates through a for loop inserting the data into the file, and finally closes the file.

## refine_data.py Explanation:

### Imports:
Imports os and beautifulsoup4 from bs4.
```
import os
from bs4 import BeautifulSoup
```

### Classes:
FileScraper Class: Has the function 'scrape_data(self, i: int, path_raw: str) -> str' that takes in an instance of the FileScraper class (self) and the index of which raw data text file (path_raw). It first opens the raw data file (path given from parameters), then it uses BeautifulSoup to parse the html in that file by using the BeautifulSoup function 'findAll('div', attrs={"id":"article-body"})' where in a div tag there is an id set to 'article-body'. It then returns all of that information as a string.

WriteData Class: Has the function 'write_data(self, paragraphs: str, i: int, path_pro: str) -> None' that takes in an instance of the WriteData class (self), a string with all of the processed data (paragraphs), the index of which processed data text file (i), and the path from where run.py is to the file wehre it will write to (path_raw). It first creates the full path of the file it will write the processed data to, then it opens that file and goes through a for loop writing the paragraphs into the processed text file, closing it afterwards.

## summarize_data.py

### Imports:
Imports os
```
import os
```

### Classes:
WriteSummarized Class: Has the function 'write_summarized(self, paragraphs: str, i: int, path_pro: str) -> None' that takes in an instance of WriteSummarized (self), the data in the processed text file (paragraphs), the index of which processed text file is being used (i), and the path to where the summarized data will be written to. It first creates the full path to the file it will write the summarized data to, opens that file, iterates through a for loop writing the summarized paraghraph and title created by open ai, and finally closes the file.


Uses requests to send an HTML get requests for the contents of the specified webpage.
```
webpage = requests.get("https://www.space.com/40547-spacex-rocket-evolution.html")
```
Creates a parse tree to extract data from HTML and sets it to soup.
```
soup = BeautifulSoup(webpage.text, "html.parser")
```
Looks through the HTML to find all the info in div tags where id=article-body
```
paragraphs = soup.findAll('div', attrs={"id":"article-body"})
```


## Output
The program will output 30 text files (10 with the raw html, 10 with the processed data that is readable, and 10 with summarized data by open ai) based on 10 different websites
