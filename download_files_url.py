
import wget
from pathlib import Path
import pandas as pd

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
            

