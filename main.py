#!/usr/bin/env python

import httplib, json

def main():
    APIKEY = "YOUR-API-KEY-GOES-HERE"
    CAP = 150.0
      
    headers = {"TekSavvy-APIKey": APIKEY}
    conn = httplib.HTTPSConnection("api.teksavvy.com")
    conn.request('GET', '/web/Usage/UsageSummaryRecords?$filter=IsCurrent%20eq%20true', '', headers)
    response = conn.getresponse()
    jsonData = response.read()
      
    data = json.loads(jsonData)
    print
    print 'Please Wait......Getting Information.....' 
    
    pd  = data["value"][0]["OnPeakDownload"]
    #pu  = data["value"][0]["OnPeakUpload"]
    #opd = data["value"][0]["OffPeakDownload"]
    #opu = data["value"][0]["OffPeakUpload"]
    sd  = data["value"][0]["StartDate"]
    ed  = data["value"][0]["EndDate"]
     
     
    print
    print str(sd[0:10]) + ' to ' + str(ed[0:10]) + ' :'
    print
    print 'Cap: %s' % (CAP)
    print 'Used: %s' % (pd)
    print 'Remaining: ' + str(CAP-pd)
    print
    x = raw_input('Press enter to exit ')
    return    


if __name__ == '__main__':
    main()

