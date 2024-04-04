# KoodousFinder
A simple tool to allows users to search for and analyze android apps for potential security threats and vulnerabilities

[![Test and Build](https://github.com/HuntDownProject/KoodousFinder/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/HuntDownProject/KoodousFinder/actions/workflows/pipeline.yaml)

# Account and API Key
Create a Koodous account and get your api key https://koodous.com/settings/developers

# Install

$ pip install koodousfinder

# Arguments
  
  
|        Param        |          description                |
|----------------|-------------------------------|
| -h, --help     |`'Show this help message and exit'`           |
|--package-name  |`"General search for APK's"`            |
|--app-name      |`Name of the app to search for`|
|--stix      |`Output for Structured Threat Information Expression (STIX™) format`|

# Examples

```
$ koodousfinder --package-name "app: Brata AND package: com.brata"
$ koodousfinder --package-name "package: com.google.android.videos AND trusted: true"
$ koodousfinder --package-name "com.metasploit"
$ koodousfinder --app-name "WhatsApp MOD"
```

![alt text for screen readers](https://raw.githubusercontent.com/teixeira0xfffff/KoodousFinder/main/assets/view2.png "sample search for Brata Malware")


Getting the output using `--stix`, running:

```
$ koodousfinder --package-name "com.ymwhatsapp" --stix
```

Will produce a output like:

```json
{
  "type": "bundle",
  "id": "bundle--d6f5709d-76ed-4f3f-a7cb-0bff0ad4adb5",
  "objects": [
    {
      "type": "file",
      "spec_version": "2.1",
      "id": "file--1bcdb4b2-c520-5d5e-a7d7-2615f6b14de3",
      "hashes": {
        "SHA-256": "e1d1f716097fc10f3f739d5e98d24d181c450ef2ddee799806530f04d699e8be"
      },
      "size": 57578320,
      "name": "WhatsApp => com.ymwhatsapp"
    },
    {
      "type": "indicator",
      "spec_version": "2.1",
      "id": "indicator--83abdc4a-aea3-4c16-ba34-0b45eb67417b",
      "created": "2023-06-21T01:57:24.294625Z",
      "modified": "2023-06-21T01:57:24.294625Z",
      "name": "WhatsApp => com.ymwhatsapp",
      "pattern": "[file:hashes.sha256 = 'e1d1f716097fc10f3f739d5e98d24d181c450ef2ddee799806530f04d699e8be']",
      "pattern_type": "stix",
      "pattern_version": "2.1",
      "valid_from": "2023-06-21T01:57:24.294625Z",
      "external_references": [
        {
          "source_name": "koodous.com",
          "url": "https://developer.koodous.com/apks/e1d1f716097fc10f3f739d5e98d24d181c450ef2ddee799806530f04d699e8be/"
        }
      ]
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--76d6b634-ba0f-4378-ad69-14f93d8022e3",
      "created": "2023-06-21T01:57:24.310246Z",
      "modified": "2023-06-21T01:57:24.310246Z",
      "relationship_type": "based-on",
      "source_ref": "indicator--83abdc4a-aea3-4c16-ba34-0b45eb67417b",
      "target_ref": "file--1bcdb4b2-c520-5d5e-a7d7-2615f6b14de3"
    },
    {
      "type": "grouping",
      "spec_version": "2.1",
      "id": "grouping--2b73de17-1a0b-46bf-aca2-f910873f886c",
      "created": "2023-06-21T01:57:24.363709Z",
      "modified": "2023-06-21T01:57:24.363709Z",
      "name": "Hunting for com.ymwhatsapp",
      "context": "Koodous search used: com.ymwhatsapp",
      "object_refs": [
        "file--1bcdb4b2-c520-5d5e-a7d7-2615f6b14de3",
        "indicator--83abdc4a-aea3-4c16-ba34-0b45eb67417b",
        "relationship--76d6b634-ba0f-4378-ad69-14f93d8022e3"
      ]
    }
  ]
}
```

# Modifiers for advanced search

|Attribute           |Modifier                          |Description                         |
|----------------|-------------------------------|-----------------------------|
|Hash           |`hash:`            |Performs the search depending on the automatically inserted hash. The admitted hashes are sha1, sha256 and md5.
|App name          |`app:`            |Searches for the specified app name. If it is a compound name, it can be searched enclosed in quotes, for example: app: "Whatsapp premium".          |
|Package name.          |`package:` |Searches the package name to see if it contains the indicated string, for example: package: com.whatsapp.|
|Name of the developer or company.          |`developer:` |Searches whether the company or developer field includes the indicated string, for example: developer: "WhatsApp Inc.".|
|Certificate         |`certificate:` |Searches the apps by their certificate. For example: cert: 60BBF1896747E313B240EE2A54679BB0CE4A5023 or certificate: 38A0F7D505FE18FEC64FBF343ECAAAF310DBD799.|

More information: https://docs.koodous.com/apks.html. <br>

# TODO

* Discord Integration
* Rulesets view
