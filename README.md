
# Indeed Job Data Scraper
Using Selinium we scraped job listings from Indeed. The code is working on 09-01-2024 and can stop working if Indeed.com decides to change the class names or ids.


## Run Locally

Clone the project

```bash
  git clone https://github.com/hs414171/AST_CONSULTING.git
```

Go to the project directory

```bash
  cd AST_CONSULTING
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the scraper

```bash
  python3 test.py
```

Additionally the code to transfer the saved excel file to mongo DB and cleaning of data is done. The job_data is the main file and cleaned_data is the clean file.
another ipynb is created which is an assignment given by the company



## Screenshots

### MongoDb Screenshot of the data 
![App Screenshot](https://i.ibb.co/2ZrYD90/scrap1.png)


## Authors

- [@hs414171](https://github.com/hs414171)
