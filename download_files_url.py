
import wget
from pathlib import Path
import pandas as pd
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

#Step 3

from pathlib import Path

"""

download_links_list= ['https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls','http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'
                ,'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL.FE.IN?downloadformat=csv',
                'http://api.worldbank.org/v2/en/indicator/SP.POP.DPND?downloadformat=csv']


for i in range(0,len(download_links_list)):
    temp_url = download_links_list[i]
    if temp_url.find("kaggle") != -1:
       print("do kaggle download ", temp_url)
       #downloaded_without_problem.append("do kaggle download ")

    else:   
        temp_data = wget.download(temp_url)
        print("name_of_file :", temp_data)
        if Path(temp_data).is_file():
            print ("File exist")
        else:
            print ("File not exist")

"""            
#Step 4
"""
path_for_excel = "different_datasets.xlsx"
excel_file_in =  pd.read_excel(path_for_excel)
print(list(excel_file_in.columns).index('Downloadable Link'))
download_links_list = excel_file_in['Downloadable Link']
print(download_links_list)
download_links_list = list(download_links_list)
print(download_links_list)
downloaded_without_problem = []
for i in range(0,len(download_links_list)):
    temp_url = download_links_list[i]
    if temp_url.find("kaggle") != -1:
       print("do kaggle download ", temp_url)
       downloaded_without_problem.append("do kaggle download ")
       
    else:
        try:
            temp_data = wget.download(temp_url)
            print("name_of_file :", temp_data)
            if Path(temp_data).is_file():
                print ("File exist")
                downloaded_without_problem.append("File exist")
            else:
                print ("File not exist")
                downloaded_without_problem.append("File not exist")
        except:
            downloaded_without_problem.append("File not exist")
            
"""

#Step 5
path_for_excel = "different_datasets.xlsx"
excel_file_in =  pd.read_excel(path_for_excel)
print(list(excel_file_in.columns).index('Downloadable Link'))
download_links_list = excel_file_in['Downloadable Link']
names_of_datasets = list(excel_file_in['Name'])
print(download_links_list)
download_links_list = list(download_links_list)
print(download_links_list)
downloaded_without_problem = []
for i in range(0,len(download_links_list)):
    temp_url = download_links_list[i]
    if temp_url.find("kaggle") != -1:
       print("do kaggle download ", temp_url)
       downloaded_without_problem.append("do kaggle download ")
       
    else:
        try:
            temp_data = wget.download(temp_url)
            print("name_of_file :", temp_data)
            if Path(temp_data).is_file():
                print ("File exist")
                print("Name of data set which is downloaded: ",names_of_datasets[i])
                downloaded_without_problem.append("File exist")
            else:
                print ("File not exist")
                downloaded_without_problem.append("File not exist")
        except:
            downloaded_without_problem.append("File not exist")
            
#excel_file_out = excel_file_in.assign(download_situation = downloaded_without_problem) 
#print(excel_file_out.head)
#excel_file_out.to_excel("output.xlsx")  

