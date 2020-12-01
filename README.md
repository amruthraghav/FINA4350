# FINA4350 - Finding the Correlation of FED Speeches and Predicting the FED Fund Rate Decision using NLP and Sentiment Analysis


## 1. Project Description
Blog Post can be checked out here: https://financiallinguists.wordpress.com/

Please refer to the post for a comprehensive understanding, project overview and analysis result.

## 2. Create the directories

Run the following to create the directories


Please refer to the above link for Data with all the files: [link to Data!](https://drive.google.com/drive/folders/10QyQ-nvP4x7hPWwX5JCOkxCf6-NJ_ViS?usp=sharing)

## 3.Running the Files
1. Get data from FOMC Website by specifying which year.
   `python FomcGetData.py all 1980`
2 . Get calendar from FOMC Website.
   `python FomcGetCalendar.py 1980`
3. Get data from Quandl. Specify the API Key and the date (yyyy-mm-dd).
   `python QuandlGetData.py [the API Key] 1980-01-01`
4. To Run Notebook
    1. Go to top directory
    `cd ../src`
    2. Open and run notebooks
    `jupyter notebook`