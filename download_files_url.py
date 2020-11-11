
import wget

#Step 1
"""
import wget
temp_url = 'https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls'
temp_data = wget.download(temp_url)
"""

#Step 2
"""
download_links_list= ['https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls','http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'
                ,'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL.FE.IN?downloadformat=csv',
                'http://api.worldbank.org/v2/en/indicator/SP.POP.DPND?downloadformat=csv']



for i in range(0,len(download_links_list)):
       
    temp_url = download_links_list[i]
    if temp_url.find("kaggle") != -1:
       print("do kaggle download ", temp_url)
       downloaded_without_problem.append("do kaggle download ")

    else:   
        temp_data = wget.download(temp_url)
        print("name_of_file :", temp_data)


"""

#Step 2
from pathlib import Path
download_links_list= ['https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls','http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'
                ,'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL.FE.IN?downloadformat=csv',
                'http://api.worldbank.org/v2/en/indicator/SP.POP.DPND?downloadformat=csv']



for i in range(0,len(download_links_list)):
    temp_url = download_links_list[i]
    if temp_url.find("kaggle") != -1:
       print("do kaggle download ", temp_url)
       downloaded_without_problem.append("do kaggle download ")

    else:   
        temp_data = wget.download(temp_url)
        print("name_of_file :", temp_data)
        if Path(temp_data).is_file():
            print ("File exist")
        else:
            print ("File not exist")
