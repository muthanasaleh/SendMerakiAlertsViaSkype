import meraki
import time
from skpy import Skype
sk = Skype("xxxx@xx.xx", "xxxxx") # Your Skype email address and password
ch = sk.contacts["live:xxxxxx"].chat # A skype contact name which is going to receive the notification
OfficeStatus = {}
APStatus = {}
OldStatus=[]
dashboard = meraki.DashboardAPI("xxxxxxxxxxxxxxxxxxxxxx")#Your API key
SecurityDevices_OrgID="xxxxxxxxxxxxxxxxx" #Your Security Devices organization ID
WirelessDevices_OrgID="xxxxxxxxxxxxxxxxxxxxxx" #Your Wireless Devices organization ID


#Get Security Devices status 
def getOfficeStatus():
        Office_Status = dashboard.organizations.getOrganizationDevicesStatuses(
            SecurityDevices_OrgID, total_pages='all')
        
        for item in Office_Status:
                        OfficeName=item['name']
                        OfficeStatus[OfficeName]= item['status']
        return OfficeStatus

#Get Wireless Devices status
def getAPsStatus():
        AP_Status = dashboard.organizations.getOrganizationDevicesStatuses(
            WirelessDevices_OrgID, total_pages='all')   
        for item in AP_Status:
                APName=item['name']
                APStatus[APName]= item['status']
        return APStatus

def getStatus():
        try:
                print("Scanning Seucirty Devices")
                Offices_Status=getOfficeStatus()
                for x, y in Offices_Status.items():
                    if(y=="offline"):     
                            if(not(x + " is "+ y) in OldStatus):
                                OldStatus.append(x + " is "+ y)
                                print(x + " is "+ y)
                                ch.sendMsg(x + " is "+ y)
                    else:
                        if((x + " is offline") in OldStatus):
                            ch.sendMsg(x + " is back "+ y)
                            OldStatus.remove((x + " is offline"))
                time.sleep(60)
                print("Scanning Wireless Devices")
                APs_Status=getAPsStatus()
                for i, j in APs_Status.items():
                    if(j=="offline"):     
                            if(not(i + " is "+ j) in OldStatus):
                                OldStatus.append(i + " is "+ j)
                                print(i + " is "+ j)
                                ch.sendMsg(i + " is "+ j)
                    else:
                        if((i + " is offline") in OldStatus):
                            ch.sendMsg(i + " is back "+ j)
                            OldStatus.remove((i + " is offline"))
                return OldStatus
        except:
              print("Request timeout------waiting for 60 seconds")
                            
while True:
        getStatus()
        time.sleep(120)

        
