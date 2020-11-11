#Step 1

import wget
temp_url = 'https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls'
temp_data = wget.download(temp_url)
