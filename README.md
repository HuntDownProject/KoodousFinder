# KoodousFinder
A simple tool to allows users to search for and analyze android apps for potential security threats and vulnerabilities

# Account and API Key
Create a Koodous account and get your api key https://koodous.com/settings/developers


# Arguments
  
  
|        Param        |          description                |
|----------------|-------------------------------|
| -h, --help     |`'Show this help message and exit'`            |
|--package-name  |`"Package name of the APK to search for"`            |
|--app-name      |`Name of the app to search for`|

![alt text for screen readers](https://raw.githubusercontent.com/teixeira0xfffff/KoodousFinder/main/assets/view.png "sample search")

# Examples

koodous.py --package-name "app: Brata AND package: com.brata" <br>
koodous.py --package-name "package: com.google.android.videos AND trusted: true"<br>
koodous.py --package-name "com.metasploit"<br>
python3 koodous.py --app-name "WhatsApp MOD"<br>

#TODO

* Discord Integration
* Rulesets view
