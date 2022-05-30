@Library('somelib')
print("code working")
import mysql.connector
import requests
import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_user_agent")


# import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
    
  password="root",
  database="aggregator"
)
mycursor = mydb.cursor()   


def createfile(siteid,nameofsite,siteurl,siteagg):
    ml_str="""
site_url = siteurl
opps_xpath =data($doc//na)
nextlink_xpath =data($doc//nr)
url_prefix = 
cookie_url = 
params = 
js_url = 
link_formatter = 
method = POST
scrapetype =com.instantmarkets.aggregator.parser.MultiListAggregator
name = agencyname
use_natty_response_date=true
use_natty_start_date=true
#use_proxy= true
#page_wait= 20000
scrapejstype= puppeteer
#---------------------------------Details---------------------------------------#
title = data($doc//na)
category = data($doc//na)
solnum = data($doc//na)
soltype = "Bid"
postdate = data($doc//na)
responsedate =data($doc//na)
agency = "agencyname"
description = normalize-space(normalize-unicode(data($doc//na)'NFKD'))
address =data($doc//na)
zipcode =""
attachmenturl= ""
attachmentlabel= ""
    """
    sp_str="""
site_url =siteurl
opps_xpath =
nextlink_xpath = data($doc//na)
url_prefix = 
cookie_url = 
add_details_xpath = 
params = 
next_params = 
js_url = 
link_formatter = 
method = GET
scrapetype =com.instantmarkets.aggregator.parser.SinglePageAggregator
name = agencyname
use_natty_response_date=true
use_natty_start_date=true
# page_wait=5000
scrapejstype=puppeteer
# use_proxy=true
#--------------------------------- Details ----------------------------------------#
title = data($doc//na)
solnum = data($doc//na)
soltype = data($doc//na)
postdate = data($doc//na)
responsedate =data($doc//na) 
agency = agencyname
description = normalize-space(data($doc//na))
category = data($doc//na)
address = data($doc//na)
zipcode = data($doc//na)    
  
    """
    
    cf_str="""
       
site_url= siteurl
opps_xpath = 
nextlink_xpath = data($doc//na)
url_prefix = 
cookie_url = 
add_details_xpath =//a[contains(.,'Notice to Bidders')]//@href
params = 
next_params = 
js_url = 
link_formatter = 
method = GET
scrapetype = com.instantmarkets.aggregator.parser.CombinationFileAggregator
name = agencyname
use_natty_response_date=true
use_natty_start_date=true
binary_variable=
#--------------------------------- Details ----------------------------------------#
title =data($doc//na)
solnum = data($doc//na)
soltype = "Bid Notification"
postdate =  data($doc//na)
responsedate =data($doc//na)
agency = "agencyname"
description = data($doc//na)
category =data($doc//na)
address = data($doc//na)
zipcode = data($doc//na)    
    """
    
    c_str="""
    
site_url=siteurl
opps_xpath = 
nextlink_xpath = data($doc//nr)
add_details_xpath =
url_prefix =
cookie_url = 
params = 
js_url = 
link_formatter = 
method = GET
scrapetype = com.instantmarkets.aggregator.parser.CombinationAggregator
name = agencyname
use_natty_response_date=true
use_natty_start_date=true
section1=
section2=
#--------------------------------- Details ----------------------------------------#
title =data($doc//na)
solnum = data($doc//na)
soltype = "Bid"
agency = "agencyname"
postdate =data($doc//na)
responsedate =data($doc//na)
description =data($doc//na)
category = data($doc//na)
address = data($doc//na)
zipcode =data($doc//na)
    
    """
    
    b_str="""
    
    
site_url=  siteurl
opps_xpath = data($doc//na)
nextlink_xpath = data($doc//nr)
url_prefix = 
cookie_url = 
link_formatter = 
method = get
scrapetype = com.instantmarkets.aggregator.parser.BinaryFileAggregator
name = agencyname
use_natty_response_date = true
use_natty_start_date=true
# page_wait=30000
# use_proxy=true
scrapejstype=puppeteer
#--------------------------------- Details ----------------------------------------#
title = -
solnum = -
soltype = Bid
postdate = -
responsedate = -
agency = agencyname
description = -
category = -
address = -
zipcode =-

    
    """
    if(siteagg=='spa' or siteagg=='SinglePageAggregator' ):
        sitestr=sp_str
        
    elif(siteagg=='mla' or siteagg=='MultiListAggregator'):
        sitestr=ml_str
    
    elif(siteagg=='ca'  or siteagg=='CombinationAggregator'):
        sitestr=c_str
    
    elif(siteagg=='cfa' or siteagg=='CombinationFileAggregator'):
        sitestr=cf_str
    
    elif(siteagg=='bfa'  or siteagg=='BinaryFileAggregator'):
        sitestr=b_str
    else:
        sitestr=ml_str
    
    
    
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
    
    
siteagg=input('enter siteaggrigator name : ')
siteid=input('enter site id : ')
nameofsite=input('enter site name or source name ')
siteurl=input('enter url')


# Site id: 302, Site name: KFM Engineering and Design
c_name="Site id: "+ siteid + ", Site name:"+nameofsite

createfile(siteid,nameofsite,siteurl,siteagg)
dbentry(siteid,nameofsite,siteurl)
createnewcard(c_name) 

