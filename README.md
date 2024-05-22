## Intro 
In order to learn Python and topics related to Data Science, I decided to create this project. The main task of this project is to retrieve all links to games from Wikipedia that 
were released for the SNES console. Next, to download the full content of the page and filter the data exclusively to the table containing key information such as:
* game title
* release date in the North America region
* release date in the PAL region
* release date in JP region

Using listed data (along with a few additional ones like unique Wiki link for specific title), the project's task is to generate a CSV file that enables obtaining complete results, 
sorted by release date for selected region. The resulting list should allow for playing the games in chronological order.

## Project details
I’ve created this project with VS Code. It should not be dependent on it, but I had to add a couple of config files that might be linked to a VS Code, so it might be advised for 
building it.   The file hierarchy is not ideal, which I will address in a second project that I will build based on WikiWebScraper. In any case, the project currently consists of the
following folder hierarchy:
- .vscode/ - a folder containing pytest configuration
- models/ - a folder consisting of files that are models
- src/ - a folder containing files (mainly) processing data
- tests/ - files containing unit tests
- main directory -  includes main.py (starting point), configuration files, and samples.py, which is a good guide for using BeautifulSoup

## Requirements
* BeautifulSoup
* aiohttp
* pytest
* pytest-cov

## Unit tests
The project is covered by unit tests at 98%. It is not large, hence such a value. On the other hand, some functionality ended up in main.py that should be separated and 
tested (particularly regarding data retrieval from Wikipedia). 
 
## Commands 

Running unit tests:
```
pytest
```

Running code coverage:
```
pytest --cov=models --cov=src --cov-report html
```

## Conclusions about the project and the issues with the structure of data retrieved from Wikipedia
I wanted to include as many new topics as possible, that’s why I decided to fetch the data from Wiki not by API, but with web scraping. In a short time, it has come to my attention 
that the data retrieved from Wikipedia has an incorrect structure which resulted in bad outcomes. To obtain required information from the table in the HTML code, I’m looking for key 
values, like “Release:” or “SNES:”. The problem is, it appears that Wikipedia does not have any standards regarding data formatting, which makes regular expressions unable to read 
data for each title using a single pattern. 

Another problem is that the dates recorded on Wikipedia pages do not follow a single format. Additionally, the dates do not always include the day or month, which also had to be considered. 
All of this made it necessary for me to use regular expressions to process the data far too extensively, which I am not happy about. Not all the data is complete, precisely due to the lack 
of a uniform data recording standard.

I aimed to develop an application where more than one platform could be selected, and a list of games could be obtained by sorting the data according to releases. 
The data structure somewhat prevented this, so I will try to develop it in the next project, based on a different source equivalent to Wikipedia.
Additionally, I would like to include features that were missing in WikiWebScraper—such as an architectural pattern, a UI layer (QT?), and the ability to select different platforms. 
Furthermore, I would use more sensible regular expressions (possibly in smaller quantities).

Nevertheless, I did everything to complete this project. I wanted to learn as much as possible from it and cover it with tests. Even though it is not perfect, I am satisfied with the results.
