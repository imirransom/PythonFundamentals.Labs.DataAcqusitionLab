import requests
url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/'
tokken = 'WqSwoxMEAbdGjwBOussoPXwHZibftJDh'
# The access key needs to be included in the header and needs to have 'token' as its key
head = {'token': tokken}

response = requests.get(url, headers=head)
print(response.status_code)

print(response.json())
