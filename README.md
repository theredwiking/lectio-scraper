# lectio-scraper
A way to interact with lectio through programming

## Technologies
- `Programming language`: [Python 3.10.4](https://www.python.org/downloads/)
- `package manager`: [pip]()
- `Os`: [Popos 22.04](https://pop.system76.com/)
- `Browser`: [Firefox](https://www.mozilla.org/en-US/firefox/download/thanks/)

## Env file
The env file is used to store personal credentials and information

### Base url
to find the url to to your lectio and see the url it should look something like this https://www.lectio.dk/lectio/___/login.aspx

The number there is between lectio/ and /login.aspx is your schools id, past that into the .env there the url is mostly setup

### Student id
To get your student id to go your schedule, and look at the url is should look almost like this https://www.lectio.dk/lectio/___/SkemaNy.aspx?type=elev&elevid= 

The 3 ___ is to symbolise yoour school uniq id and the row of numbers that come after elevid= is your student id copy that and past it into .env at STUDENTID


## Setup
Guide in setting the project up

1. Clone project 
```bash
git clone https://github.com/theredwiking/lectio-scraper.git
```
2. Install dependencies 
```bash 
pip3 install selenium python-dotenv
```
3. Rename .env.example to .env and populate information
4. Try running the project
```bash 
python3 main.py
```

## Resources
1. [AttributeError](https://pythoninoffice.com/fixing-attributeerror-webdriver-object-has-no-attribute-find_element_by_xpath/)