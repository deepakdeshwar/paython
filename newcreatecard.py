#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import requests
import json
from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="my_user_agent")
import mysql.connector

   


def createfile(siteid,nameofsite,siteurl):
    sitestr="""
    site_url = siteurl
    opps_xpath =data($doc//html/body/section/ui-view/div/div[2]/div/ul/li/div/div/a//@href)
    nextlink_xpath =data($doc//nr)
    url_prefix = https://www.civcastusa.com
    cookie_url = 
    params = 
    js_url = 
    link_formatter = 
    method = POST
    scrapetype =com.instantmarkets.aggregator.parser.MultiListAggregator
    name = agencyname
    use_natty_response_date=true
    use_natty_start_date=true
    use_proxy= true
    page_wait= 20000
    scrapejstype= puppeteer
    #---------------------------------Details---------------------------------------#
    title = data($doc//ui-view/div[1]/div/div/div[1]/div[1])
    category = data($doc//na)
    solnum = data($doc//ui-view/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div[contains(.,'ID:')]/div[2])
    soltype = "Bid"
    postdate = data($doc//na)
    responsedate =data($doc//ui-view/div[3]/div/div/div/div[contains(.,'Bid Detail')]/div[2]/div[contains(.,'Date')]//span[contains(.,'2022')])
    agency = "agencyname"
    description = normalize-space(normalize-unicode(substring-after(data($doc//html/body/section/ui-view/div[3]/div/div/div),'Summary'),'NFKD'))
    address = normalize-space(data($doc//html/body/section/ui-view/div[3]/div/div/div/div[6]/div[1]/div/div[2]))
    zipcode =""
    attachmenturl= ""
    attachmentlabel= ""
    """
    aa=sitestr.replace('siteurl',siteurl)
    fp=aa.replace('agencyname',nameofsite)
    
    
    name=siteid+'_'+nameofsite.replace(' ','_')+".properties" 
    f = open(name, "w")
    f.write(fp)
    print("file craeted")
    f.close
    

def dbentry(siteid,nameofsite,siteurl):
    qu_str="""INSERT INTO aggregator.siteaggregator (SiteID, SiteName, SiteDescription, SiteShortName, DefaultCustomerName, SiteURL, SourceType,DefaultOpportunityLongitude, DefaultOpportunityLatitude, DefaultCustomerType, DefaultCountry, DefaultState, DefaultCity, DefaultTimeZone, SiteProperty, DefaultAggregatorClass, AggregatorEnabled, SiteAggregateFrequencyInMins, LastAggregateHashCode, IgnoreHashCodeMatch, LastRunTimestamp, ScreenShotEnabled, VerifySshot)
                           VALUES 
                           ('site_id', 'sitename', 'sitename', 'sitename', 'sitename', 'siteurl', 'Free', 'longe', 'late', 'Co-op', 
                           
                           'United States', 'Texas', '', 'America/Los_Angels', 'D:/IM/site-properties/', 
                           
                           'com.instantmarkets.aggregator.parser.CasperAggregator', 1, 1440, '', 1, '2021-11-11 09:09:09', 1, 1)"""

    name=siteid+'_'+nameofsite.replace(' ','_')+".properties" 
    
    qu_str=qu_str.replace('site_id',siteid)
    qu_str=qu_str.replace('sitename',nameofsite)
    qu_str=qu_str.replace('siteurl',siteurl)
    qu_str=qu_str.replace('D:/IM/site-properties/',"D:/IM/site-properties/"+name)
    
    try:
        loca = geolocator.geocode(nameofsite+' '+ 'USA')
        geolocator = Nominatim(user_agent="my_user_agent")
        qu_str=qu_str.replace('longe',str(loca.longitude))
        qu_str=qu_str.replace('late',str(loca.latitude))
    except:
        qu_str=qu_str.replace('longe','-76.2510408')
        qu_str=qu_str.replace('late','43.5128472')
 
     
        
    mySql_insert_query=qu_str
    mycursor.execute(mySql_insert_query)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    
def createnewcard(cardname):
    
    url = "https://api.trello.com/1/cards/"+"?key=488c82580e181fbd0d2cb9304c5550a2&token=52a1cad377e78618d2313a117ed65df324c35fccb34969cee2829a7db3355fec&idList=5acc5804a98e586d3405ab1d&name="+str(cardname)
    headers = {
       "Accept": "application/json"
        }
    query = {   
        }
    response = requests.request(
       "POST",
    url,
    headers=headers,
    params=query
    )
    
    
    

siteid=input('enter site id : ')
nameofsite=input('enter site ')
siteurl=input('enter url')

# Site id: 302, Site name: KFM Engineering and Design
c_name="Site id: "+ siteid + ", Site name:"+nameofsite

createfile(siteid,nameofsite,siteurl)
dbentry(siteid,nameofsite,siteurl)
createnewcard(c_name) 


    
    





# In[17]:


# import requests
# import json

# url = "https://api.trello.com/1/cards/"+"?key=488c82580e181fbd0d2cb9304c5550a2&token=52a1cad377e78618d2313a117ed65df324c35fccb34969cee2829a7db3355fec&idList=5acc5804a98e586d3405ab1d&name=test my card"

# headers = {
#    "Accept": "application/json"
# }

# query = {
   
# }

# response = requests.request(
#    "POST",
#    url,
#    headers=headers,
#    params=query
# )
# print(response)
# # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# In[ ]:


# import mysql.connector
# import requests
# # import datetime 

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="aggregator"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT siteid ,defaultcustomername, siteurl FROM siteaggregator")
# myresult = mycursor.fetchall()
# for x in myresult:
# #   print(x)


# In[36]:


# def createnewcard(cardname):
    
#     url = "https://api.trello.com/1/cards/"+"?key=488c82580e181fbd0d2cb9304c5550a2&token=52a1cad377e78618d2313a117ed65df324c35fccb34969cee2829a7db3355fec&idList=62455a7d22a1866c317638b0&name="+str(cardname)
#     headers = {
#        "Accept": "application/json"
#         }
#     query = {   
#         }
#     response = requests.request(
#        "POST",
#     url,
#     headers=headers,
#     params=query
#     )
# l1=["test1","test2","test3","test4","test5"]
# for i in l1:    
#     createnewcard(i)


# In[2]:


# import requests
# import json
# def createnewcard(cardname,url):
    
#     url = "https://api.trello.com/1/cards/"+"?key=488c82580e181fbd0d2cb9304c5550a2&token=52a1cad377e78618d2313a117ed65df324c35fccb34969cee2829a7db3355fec&idMembers=611b98af664e190fd53beef5&idList=5acc5804a98e586d3405ab1d&name="+str(cardname)+"&desc="+url
#     headers = {
#        "Accept": "application/json"
#         }
#     query = {   
#         }
#     response = requests.request(
#        "POST",
#     url,
#     headers=headers,
#     params=query
#     )
# # createnewcard("c_name",'testurl')    
    
# cno=["760","810","811","814","815","878","887","893","465","468","476","479","480","483","949","1022","989","1027","1059","1064","1086","1131","1136","1140","1330","1375","1506","1507","1523","1563","1564","1647","1005","1657","38","1734","1835","1869","582","6453","6454","6455","6456","6457","6458","6459","6460","6461","6462","6463","6464","6465"]
# cnm=["Tabor Associates Inc","Talley Landscape Architects Inc","Tarrant Regional Water District","TBG Partners","Teague Nall Perkins","Teague Nall Perkins inc","Team Phillips Inc","TEDSI Infrastructure Group Inc","Tellepsen Services","Terra Associates Inc","terralab landscape architects llc","Texas Land Engineers Inc","Fain Group Inc","Goodman Corporation","Grounds Guys","DBA BUGCO Pest Control","Thonhoff Consulting Engineers","TNP","TNP Inc","Top Site Civil Group LLC","TPE","TranSystems","TRC Engineers Inc","Trihydro Corporation","Trinity River Authority of Texas","Turnkey Tract","Two Fifteen Consulting","Underwood Inc","Upper Trinity Regional Water District","Utility Engineering Group PLLC","Val Verde County","Venturi Engineers LLC","Versa Infrastructure LLC","Vigil and Associates","Vogler and Spencer Engineering Inc","Vogt Engineering","Volkert Inc","Walker Partners LLC","Wall Engineering","Walter P Moore","Walter P Moore Associates","Ward Getz and Associates PLLC","Wasteline Engineering Inc","WaterEngineers Inc","Waterscape Consultants Inc","Weishuhn Engineering Inc","Westfall Engineering","Whiteley Oliver Engineering","Whitewater Springs WSC","Willis Environmental Engineering Inc","Wiss Janney Elstner Associates","WTC Inc"]
# url=["https://www.civcastusa.com/publishers/5f7cbc19d3961e0acc52c9ff","https://www.civcastusa.com/publishers/5867858301ec5a4c60e43132","https://www.civcastusa.com/publishers/586784c601ec5a48d476fa3d","https://www.civcastusa.com/publishers/5e73bc2b78fe7b1778202423","https://www.civcastusa.com/publishers/61af7556caa9791354c6fa63","https://www.civcastusa.com/publishers/61cc8bfefa21d7145864b151","https://www.civcastusa.com/publishers/586787de01ec5a48f88d5422","https://www.civcastusa.com/publishers/5867823301ec5a0f80c78121","https://www.civcastusa.com/publishers/601c27fb78f2280fe81437da","https://www.civcastusa.com/publishers/5a73351299434a2c10889ddb","https://www.civcastusa.com/publishers/5867886b01ec5a4118fa9520","https://www.civcastusa.com/publishers/586785ba01ec5a46d8e433fa","https://www.civcastusa.com/publishers/586781f301ec5a4a5800934b","https://www.civcastusa.com/publishers/5a270e3099434a5fe8bbbd3d","https://www.civcastusa.com/publishers/61520939e2b76d04e8c2b5b0","https://www.civcastusa.com/publishers/61dd95af7bdcd7054cd49bf7","https://www.civcastusa.com/publishers/58bd780299434a21bcf0b9f6","https://www.civcastusa.com/publishers/5a21c6af99434a5550fc1ea2","https://www.civcastusa.com/publishers/61e9e2a9bf70781668c8c45a","https://www.civcastusa.com/publishers/60ad1831a6193a0e804a1b5b","https://www.civcastusa.com/publishers/60f9bfae97720c09cc0f9f14","https://www.civcastusa.com/publishers/613275d5179dbd1584b71acf","https://www.civcastusa.com/publishers/5867863501ec5a0d8cb9372d","https://www.civcastusa.com/publishers/5ed69c9054c1431780b18189","https://www.civcastusa.com/publishers/5d6017908289a31a1c7febe1","https://www.civcastusa.com/publishers/621065289c000417b86858a5","https://www.civcastusa.com/publishers/5867887701ec5a4d2cd0da91","https://www.civcastusa.com/publishers/586786c901ec5a452cce02ab","https://www.civcastusa.com/publishers/5d1514c7fc5f5e166c7a4f2e","https://www.civcastusa.com/publishers/618ad853e47ded0480329ce7","https://www.civcastusa.com/publishers/5e8f7071f2f25c0a646e511f","https://www.civcastusa.com/publishers/586783cc01ec5a4da83d3a24","https://www.civcastusa.com/publishers/5e3f148dc0ed3117c8d77e95","https://www.civcastusa.com/publishers/6054c683eafe9e16208750aa","https://www.civcastusa.com/publishers/5867844301ec5a4354dc92df","https://www.civcastusa.com/publishers/5f10633d8088a1027cde7c98","https://www.civcastusa.com/publishers/61859836a8b0930f6c9ebe7f","https://www.civcastusa.com/publishers/586783ae01ec5a4ef46592eb","https://www.civcastusa.com/publishers/586781cb01ec5a109875729d","https://www.civcastusa.com/publishers/586786ea01ec5a2ea4b926f6","https://www.civcastusa.com/publishers/609c1db1e015e90df8a2a1d2","https://www.civcastusa.com/publishers/5867868601ec5a41bc202207","https://www.civcastusa.com/publishers/5867826901ec5a3de4779168","https://www.civcastusa.com/publishers/5867864701ec5a0d8cb93831","https://www.civcastusa.com/publishers/5e0e2326bf098d072cf0066d","https://www.civcastusa.com/publishers/5f3ea104d9675e119427e238","https://www.civcastusa.com/publishers/601d953be25251167caac753","https://www.civcastusa.com/publishers/60be8b5db8a36401e0d64e48","https://www.civcastusa.com/publishers/6078402539a4bc17dc442b67","https://www.civcastusa.com/publishers/60f58bded82dca051468c8c7","https://www.civcastusa.com/publishers/61e0332e49a3c4096cf02686","https://www.civcastusa.com/publishers/5867833001ec5a39f071f388"]

# for  in range(len(cno)):
#     c_name="Site id: "+ cno[i] + ", Site name:"+cnm[i]
#     createnewcard(c_name,url[i])



# In[ ]:




