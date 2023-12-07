import requests

response = requests.get('https://www.ncei.noaa.gov/cdo-web/api/v2/locations')
print(response.status_code)
