# KoodousFinder
A simple tool to allows users to search for and analyze android apps for potential security threats and vulnerabilities

# Account and API Key
Create a Koodous account and get your api key https://koodous.com/settings/developers

# Arguments
  
  
|        Param        |          description                |
|----------------|-------------------------------|
| -h, --help     |`'Show this help message and exit'`            |
|--package-name  |`"General search for APK`s"`            |
|--app-name      |`Name of the app to search for`|

# Examples

koodous.py --package-name "app: Brata AND package: com.brata" <br>
koodous.py --package-name "package: com.google.android.videos AND trusted: true"<br>
koodous.py --package-name "com.metasploit"<br>
python3 koodous.py --app-name "WhatsApp MOD"<br>


![alt text for screen readers](https://raw.githubusercontent.com/teixeira0xfffff/KoodousFinder/main/assets/sample%202.png "sample search for Brata Malware")

# Modifiers for advanced search

|Attribute           |Modifier                          |Description                         |
|----------------|-------------------------------|-----------------------------|
|Hash           |`hash:`            |Performs the search depending on the automatically inserted hash. The admitted hashes are sha1, sha256 and md5.
|App name          |`app:`            |Searches for the specified app name. If it is a compound name, it can be searched enclosed in quotes, for example: app: "Whatsapp premium".          |
|Package name.          |`package:` |Searches the package name to see if it contains the indicated string, for example: package: com.whatsapp.|
|Name of the developer or company.          |`developer:` |Searches whether the company or developer field includes the indicated string, for example: developer: "WhatsApp Inc.".|
|Certificate         |`certificate:` |Searches the apps by their certificate. For example: cert: 60BBF1896747E313B240EE2A54679BB0CE4A5023 or certificate: 38A0F7D505FE18FEC64FBF343ECAAAF310DBD799.|

More information: https://docs.koodous.com/apks.html. <br>
#TODO

* Discord Integration
* Rulesets view
