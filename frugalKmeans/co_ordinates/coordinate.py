__author__ = 'vivek'


import requests
import json
import concurrent.futures
import csv
from time import sleep

MY_KEY="Your_google_co-ordinates_API_key"


def get_co_ordinates(address):
    
    sleep(0.2)
    URL_GEOCODE = "https://maps.googleapis.com/maps/api/geocode/json?region=in&key="+MY_KEY+"&address="
    #print URL_GEOCODE
    header_ = {"User-Agent": "console(coordinate)",}

    try:
        resp = requests.get(URL_GEOCODE + address, headers=header_)
    except:
        print "Network error"
        return -11

    
    try:
        json_response = json.loads(resp.text)
        # print json_response
        
        if json_response["status"]== "OK":
            results_list = json_response["results"]
            results_list_dict=results_list[0]
            results_list_dict_geodict=results_list_dict["geometry"]
            results_list_dict_geodict_locdict=results_list_dict_geodict["location"]
            lat=results_list_dict_geodict_locdict["lat"]
            lng=results_list_dict_geodict_locdict["lng"]
            addr=str(json_response['results'][0]['formatted_address'])

            fcsv = csv.writer(open("coordinate.csv", "ab+"))
            fcsv.writerow([address,addr, lat,lng])
            print address, addr , lat , lng
	    return 1
       	# print(decoded["title_approx"])
    except (ValueError, KeyError, TypeError):
        print "Error in Key/Value/Type"     





if __name__ == '__main__':
#	get_co_ordinates("Ashiyana, Lucknow, Uttar Pradesh, India")
    with open('sample_data.csv', 'rb') as f:
        reader = csv.reader(f)
        #restraunt_list = list(reader)
        restraunt_list = [c[0] for c in reader if c]
        edited_res_list=[(''.join(res_addr.split(',')[1:])).split("...", 1)[0]+" lucknow"  for res_addr in restraunt_list]

    executor = concurrent.futures.ProcessPoolExecutor(20)
    futures = [executor.submit(get_co_ordinates, res_addr) for res_addr in edited_res_list]
    concurrent.futures.wait(futures)


