import requests
from bs4 import BeautifulSoup as bs


#https://telegram.dog/sjprojects
def telegram(username):
    try:
        base_url = f"https://telegram.dog/{username}"
        r = requests.get(base_url).text
        soup = bs(r,'html.parser')
        member_count = soup.find("div",class_="tgme_page_extra").text.replace(" ","").split("subscribers")[0]
        #print(member_count)
        channel_name = soup.find("div",class_="tgme_page_title").text.replace("\n","")
        #print(channel_name)
        description = soup.find("div",class_="tgme_page_description").text
        #print(description)
        dp = soup.find("img",class_="tgme_page_photo_image")['src']
        #print(dp['src'])

        data = {}
        data['name'] = channel_name #can be used as group also
        data['subs'] = member_count
        data['description'] = description
        data['image'] = dp
        return data
    except Exception as e:
        return {"status":False,"erorr":e}


telegram("sjprojects")