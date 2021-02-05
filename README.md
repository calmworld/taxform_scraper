# taxform_scraper
### Using Python3 Scrapy

#### Python version: 
Python 3.9.1
#### Scrapy version:
Scrapy 2.4.1

#### No required dependencies, that is the magic that is scrapy!

#### To Run Scrapy spider: 
scrapy runspider irs.py

#### To Output Data as JSON - 2 ways:
- go to settings and uncomment FEED_URI & FEED_FORMAT.  
or  
- run the command: scrapy runspider irs.py -s FEED_URI=forms.json -s FEED_FORMAT=json 

#### To Control Page Count Results:
go to settings.py and adjust CLOSESPIDER_PAGECOUNT=100

#### To Check Page Count Results:
run the command: cat forms.json

#### To Export Data as CSV and XML:
simply replace json with either .csv or .xml

#### To Download PDF files:
- in download_pdf/standalone folder, run python3 main.py 2018 2020

#### Project Challenges:
- Getting min & max year was challenging becuase page source only indicated one tag "<td class="EndCellSpacer">".
- However there was "isDescending=true" in the href of the anchor tag, but that sorted all results, not a specific form.
- Getting PDF files to download into a specific folder with the file name. I managed to get scrapy to create the folder inside download_pdf/standalone.
- Getting specific range of years was challenging as well. 