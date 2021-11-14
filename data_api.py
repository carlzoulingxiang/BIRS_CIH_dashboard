import pandas as pd
import requests

def request_data(url, querystring):
    
    headers = {
        'x-rapidapi-host': "goverlytics.p.rapidapi.com",
        'x-rapidapi-key': "4aa42e4379msh4870ef618e60c91p17993bjsn1dea73f0c84c"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    xx = dict(response.json())
    
    return xx


def handle_one(item):
    
    row_dict = {}
    
    for k,v in item.items():
        if type(v) == str:
            row_dict[k] = v
        elif type(v) == list:
            row_dict[k] = ",".join([str(vv) for vv in v])
        else:
            row_dict[k] = str(v)
            

    return pd.DataFrame([row_dict]).T


def handle_data(list_item):
    
    rst_df = []
    for i in list_item:
        rst_df.append(handle_one(i))
        
    return pd.concat(rst_df, axis=1)


def get_data_fed_legis():
    url = "https://goverlytics.p.rapidapi.com/federal-legislation/ca"
    querystring = {"include_summary":"true","include_text":"true","include_actions":"true","include_votes":"true", "page":1}
    cur_page = request_data(url, querystring)
    final_data = [handle_data(cur_page["data"])]


    while cur_page["pagination"]["next_url"]:
        print(cur_page["pagination"]["next_url"])
        querystring["page"] = querystring["page"] + 1
        final_data.append(handle_data(cur_page["data"]))
        cur_page = request_data(url, querystring)
        
        
    final_country_legistlation = pd.concat(final_data, axis=1).T.reset_index(drop=True)
    final_country_legistlation.to_excel("./data/federal_legislation.xlsx", index=False)


def get_data_fed_legtor():
    
    import requests

    url = "https://goverlytics.p.rapidapi.com/federal-legislators/ca"

    querystring = {"page":1}

    headers = {
        'x-rapidapi-host': "goverlytics.p.rapidapi.com",
        'x-rapidapi-key': "4aa42e4379msh4870ef618e60c91p17993bjsn1dea73f0c84c"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    cur_page = dict(response.json())

    final_data = [handle_data(cur_page["data"])]
    while cur_page["pagination"]["next_url"]:
        print(cur_page["pagination"]["next_url"])
        querystring["page"] = querystring["page"] + 1
        final_data.append(handle_data(cur_page["data"]))
        cur_page = request_data(url, querystring)
        
        
    final_country_legistlator = pd.concat(final_data, axis=1).T.reset_index(drop=True)
    final_country_legistlator.to_excel("./data/federal_legislator.xlsx", index=False)
    
    
def get_data_div_legis():

    import requests
    import pandas as pd

    url = "https://goverlytics.p.rapidapi.com/division-legislation/ca/{}"
    querystring = {"include_summary":"true","include_votes":"true","include_actions":"true","include_text":"true"}

    province_list = ["bc", "nl", "yt",]
    for province in province_list:
        print(province)
        
        url_pv = url.format(province)
        cur_page = request_data(url_pv, querystring)
        final_data = [handle_data(cur_page["data"])]

        
        while cur_page["pagination"]["next_url"]:
            print(cur_page["pagination"]["next_url"])
            next_url = cur_page["pagination"]["next_url"]
            final_data.append(handle_data(cur_page["data"]))
            cur_page = request_data(next_url, querystring={})
            
        
        final_province_legistlation = pd.concat(final_data, axis=1).T.reset_index(drop=True)
        # print(final_province_legistlation.region)
    
        final_province_legistlation.to_excel(f"./data/division-legislation-{province}.xlsx", index=False)


    province_list = ["pe", "ns", "nb", "qc", "on", "mb", "sk", "ab", "nt", "nu"]

    for province in province_list:
        print(province)
        
        url_pv = url.format(province)
        cur_page = request_data(url_pv, querystring)
        final_data = [handle_data(cur_page["data"])]

        
        while cur_page["pagination"]["next_url"]:
            print(cur_page["pagination"]["next_url"])
            next_url = "https://goverlytics.p.rapidapi.com" + cur_page["pagination"]["next_url"]
            final_data.append(handle_data(cur_page["data"]))
            cur_page = request_data(next_url, querystring={})
        
        
        final_province_legistlation = pd.concat(final_data, axis=1).T.reset_index(drop=True)

    final_province_legistlation.to_excel(f"./data/division-legislation-{province}.xlsx", index=False)
