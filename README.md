# SendMerakiAlertsViaSkype
This is part of a project to have one Alert system for all network devices (Meraki Devices) in an organization. The main purpose of this application is to Check Meraki devices status in real time and sending text messages to a Skype chat when a device's status is changed (Online/Offline).

## Requirements
  **To use this application you need:**
  
    -	Python 3.7+
    -	Meraki API key
    -	Skype account
    -	Python libraries: skpy and meraki

The application scans all devices within an organization and store the status of each device in a dictionary (for example {“Device1, offline”}). Then it loops through the list of all devices stored in the dictionary and send an alert if any device is offline to a contact in your skype account (Your system admin Skype account). The script runs every 2 minutes and it can be changed based on how critical the impact is on your business. However, running high-volume API monitoring tasks in realtime can over throttle the system and lead to 429 errors (Read More https://developer.cisco.com/meraki/api-v1/#!rate-limit)

## Install and Setup
  1. Install required libraries on Python
    -	Meraki
      Pip install meraki
    -	Skpy
      Pip install skpy

  2. Meraki API Key (https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API)

## Using the application
  1.	Open the application with your Python IDLE https://www.python.org/downloads/
  2.  Edit Meraki API key value
  3.	Edit Organization ID value(How to get organization ID https://developer.cisco.com/meraki/api/#!get-organizations)
  4.	Get your system admin skype contact name(https://support.skype.com/en/faq/FA34793/how-do-i-view-someone-s-profile-in-skype )
  5.	Run the application

## Technologies used
  **The following technologies were used as part of this demo:**
  1.	Cisco Meraki MX devices
  2.	Cisco Meraki MS Devices
  3.	Cisco Meraki MR devices
  4.  Microsoft Skype

## License
Distributed under the MIT License. See LICENSE.txt for more information.
