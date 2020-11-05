from datetime import date
import numpy as np
import pandas as pd
import pickle
import sys

from fomc_get_data.FomcMinutes import FomcMinutes
from fomc_get_data.FomcSpeech import FomcSpeech

def download_data(fomc, start_year):
    df = fomc.get_contents(start_year)
    print("Shape of the downloaded data: ", df.shape)
    print("The first 5 rows of the data: \n", df.head())
    print("The last 5 rows of the data: \n", df.tail())
    fomc.pickle_dump_df(filename = fomc.content_type + ".pickle")
    fomc.save_texts(prefix = fomc.content_type + "/FOMC_" + fomc.content_type + "_")

if __name__ == '__main__':
    
    args = sys.argv[1:]

    if len(args) == 0:
        start_year = 1990
    else:
        start_year = int(args[0])
    
    if (start_year < 1980) or (start_year > 2020):
        
        print("Please specify the first argument as starting year between 1980 and 2020")
        sys.exit(1)

    print("Scraping: minutes")
    fomc = FomcMinutes()
    download_data(fomc, start_year)

    print("Scraping: speeches")
    fomc = FomcSpeech()
    download_data(fomc, start_year)
