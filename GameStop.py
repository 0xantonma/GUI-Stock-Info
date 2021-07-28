import requests
import json
import Constants

class Stock:

    def realTimePrice(index_name):
        # Real-time Price
        url = "https://twelve-data1.p.rapidapi.com/price"
        querystring = {"symbol": index_name, "format": "json", "outputsize": "30"}
        headers = {
            'x-rapidapi-key': Constants.RAPID_SERVICE_API_KEY,
            'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)

        jsonDecoded = json.loads(response.text)
        return jsonDecoded


    def timeSeries(index_name):
        url2 = "https://twelve-data1.p.rapidapi.com/time_series"

        querystring2 = {"symbol": index_name, "interval": "1day", "outputsize": "5", "format": "json"}

        headers2 = {
            'x-rapidapi-key': Constants.RAPID_SERVICE_API_KEY,
            'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
        }

        response2 = requests.request("GET", url2, headers=headers2, params=querystring2)
        jsonDecoded2 = json.loads(response2.text)
        return jsonDecoded2['values']


    def betaIndicator(index_name):
        url = "https://twelve-data1.p.rapidapi.com/beta"

        querystring = {"interval": "1day", "symbol": index_name, "format": "json", "series_type_2": "close",
                       "series_type_1": "open", "time_period": "9", "outputsize": "10"}

        headers = {
            'x-rapidapi-key': Constants.RAPID_SERVICE_API_KEY,
            'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        jsonDecoded = json.loads(response.text)
        return jsonDecoded['values']