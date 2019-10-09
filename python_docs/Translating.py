# -*- coding: utf-8 -*-
documentation = [
_(u"""# NVDA Translation and Localization"""),
"",_(u"""Thank you for considering to localize NVDA to your language, or improving an existing translation."""),
_(u"""In order to support multiple languages/locales, NVDA must be translated and data specific to the locale must be provided."""),
_(u"""There are several tasks to be done, and this document hopes to give you an overview and guide you through the process."""),
"","",_(u"""## Translation Mailing List"""),
_(u"""Translators should subscribe to the [NVDA translations mailing list](https://groups.io/g/nvda-translations)"""),
_(u"""hosted at Groups.IO."""),
"",_(u"""It is an English low trafic list devoted for the discussion of translation. """),
_(u"""Important messages that relate to translators will also be sent here, i.e. before official NVDA releases, to remind translators to make sure their localization is up to date."""),
"",_(u"""## Important Dates"""),
"",_(u"""Translators should ensure their translation is up to date by (UTC 00:00 on 14 February, 14 May, 14 August and 14 November) in order for it to be included in the upcoming final release, with this being delayed up to three days for some releases. Work submitted after this time will not be included in the upcoming release.  A reminder will be sent three to five days prior to end of this period. For further information please see the ReleaseProcess page."""),
"",_(u"""## Translation Status"""),
"",_(u"""Status for existing NVDA localizations are provided below. If you would like to improve or would like to work on a new language, please write to the NVDA translations email list."""),
_(u"""Information updated as of September 2019 (2019.2)."""),
_(u"""When 2019.2 is listed in the last updated column, it means that the localization is fully up to date and will be ready for the next release. For the purposes of the information below, \"up to date\" refers to interface translation of at least 90%."""),
"",_(u"""| Language | Status | Last updated |"""),
_(u"""|------------|----------|----------------|"""),
_(u"""| af_ZA: Afrikaans | Not complete/out of date, maintainer needed. | Oct 2009 |"""),
_(u"""| am: Amharic | Not complete/out of date, maintainer needed. | Jul 2012 |"""),
_(u"""| an: Aragonese | nearly complete. | 2019.2 |"""),
_(u"""| ar: Arabic | Up to date. | 2019.2 |"""),
_(u"""| bg: Bulgarian | Up to date. | 2019.2 |"""),
_(u"""| CA: Catalan | not complete. | 2018.4 |"""),
_(u"""| CKB: Central Kurdish | Not complete/out of date, maintainer needed. | n.a. |"""),
_(u"""| cs: Czech | Documentation incomplete from Sept 2017. The NVDA interface is Up to date. | 2019.2 | """),
_(u"""| da: Danish | Up to date. | 2019.2 | """),
_(u"""| de: German | Up to date. | 2019.2 | """),
_(u"""| de_CH: Swiss German | Not complete/out of date, maintainer needed. | 2018.3 | """),
_(u"""| el: Greek | The NVDA interface is nearly complete. Documentation is out of date from Nov 2017| 2019.1 |"""),
_(u"""| es: Spanish | Up to date. | 2019.1 | """),
_(u"""| es_CO: Spanish (Columbia) | Not complete/out of date, maintainer needed. | Jul 2016|"""),
_(u"""| fa: Farsi | Up to date. | 2019.2 |"""),
_(u"""| fi: Finnish | Up to date. | 2019.2 | """),
_(u"""| fr: French | Up to date. | 2019.2 | """),
_(u"""| ga: Gaeilge (Ireland) | Interface: work in progress. | Dez 2018 |"""),
_(u"""| gl: Galician | Up to date. | 2019.2 | """),
_(u"""| he: Hebrew | Documentation from Feb 2017. NVDA interface Up to date. | 2019.2 |"""),
_(u"""| hi: Hindi | NVDA interface up to date | 2019.2 |"""),
_(u"""| hr: Croatian | Up to date. | 2019.2 |"""),
_(u"""| hu: Hungarian | Up to date. | 2018.3 |"""),
_(u"""| is: Icelandic | Not complete, intermittent, help needed. | Apr 2013 |"""),
_(u"""| it: Italian | Up to date. | 2018.3 | """),
_(u"""| ja: Japanese | Up to date. | 2018.3 | """),
_(u"""| ka: Georgian | Not complete/out of date, maintainer needed. | May 2015 |"""),
_(u"""| kmr: Northern Kurdish | In progress. | N/A |"""),
_(u"""| kn: Kannada | Out of date, help needed. | Date unknown |"""),
_(u"""| ko: Korean | Up to date. | 2018.3 |"""),
_(u"""| ky: Kyrgyz | Up to date. | 2018.3 |"""),
_(u"""| lt: Lithuanian | Out of date, help needed. | 2016 |"""),
_(u"""| lv: Latvian | Out of date, help needed. | 2016 |"""),
_(u"""| mk: Macedonian | Up to date. | 2017.4 |"""),
_(u"""| mn: Mongolian | Up to date. | 2018.2 |"""),
_(u"""| my: Burmese | Up to date. | 2018.3 |"""),
_(u"""| nb_NO: Norwegian | Out of date. | 2012 |"""),
_(u"""| ne: Nepali  | Translator deceased. | 2016 |"""),
_(u"""| nl: Dutch | Up to date. | 2018.3 |"""),
_(u"""| Pa: Punjabi | Not complete, help needed. | Nov 2014 |"""),
_(u"""| pl: Polish | Up to date. | 2018.3 |"""),
_(u"""| pt_BR: Portuguese (Brazil) | Up to date. | 2018.3 |"""),
_(u"""| pt_PT: Portuguese (Portugal) | Up to date. | 2018.3 |"""),
_(u"""| ro: Romanian | Up to date. | 2018.3 |"""),
_(u"""| ru: Russian | Up to date. | 2018.3 |"""),
_(u"""| sk: Slovak | Up to date. | 2018.2 |"""),
_(u"""| sl: Slovenian | Up to date. | 2018.3 |"""),
_(u"""| sq: Albanian | Not complete/out of date, maintainer needed. | Jul 2011 |"""),
_(u"""| sr: Serbian | Interface Up to date, documentation not complete. | 2018.3 |"""),
_(u"""| sv: Swedish | Not complete/out of date. | May 2015 |"""),
_(u"""| ta: Tamil | Up to date. | 2018.3 |"""),
_(u"""| th: Tai | Out of date. | Feb 2011 |"""),
_(u"""| tr: Turkish | Up to date. | 2018.3 |"""),
_(u"""| uk: Ukranian | Up to date. | 2018.3 |"""),
_(u"""| ur: Urdu | Incomplete, barely translated. | 2016 |"""),
_(u"""| vi: Vietnamese | Up to date. | 2018.3 |"""),
_(u"""| zh_CN: Simplified Chinese | Up to date. | 2018.3 |"""),
_(u"""| zh_HK: Traditional Chinese Hong Kong | Up to date. | 2018.3 |"""),
_(u"""| zh_TW: Traditional Chinese Taiwan | Up to date. | 2018.3 |"""),
"",_(u"""## New Localization"""),
_(u"""Start by subscribing to the translation list above, so that you can get help and advice."""),
"",_(u"""It is recommended that you use our new more automated workflow, which will allow you to focus only on translation. See [the automated workflow section](#advantages-of-the-automatic-workflow-process ) below."""),
"",_(u"""If you still wish to go through the manual process, then follow the instructions on the [[TranslatingUsingManualProcess]] page after first reading [Files to be Localized](#files-to-be-localized) below."""),
"",_(u"""## Improving an Existing Localization"""),
_(u"""You should contact the existing maintainer of your language, and discuss your suggestions and changes. Together you should be able to agree on the best translation and terms to be used, and the necessary changes can be made."""),
"",_(u"""You can send an email to the translation mailing list to find out the correct person. """),
"",_(u"""If your language is no longer maintained, you can request to be the new maintainer for the language."""),
"",_(u"""## Files to be Localized"""),
_(u"""These files are listed in order of importance."""),
"",_(u"""- nvda.po: NVDA's interface messages, see [[TranslatingTheInterface]] page for more info."""),
_(u"""- characterDescriptions.dic: names of characters in your language, see [[TranslatingCharacterDescriptions]] for more info."""),
_(u"""- symbols.dic: names of symbols and punctuation in your language, see [[TranslatingSymbols]] for more information."""),
_(u"""- userGuide.t2t: the User Guide, see [[TranslatingUserGuide]] for more information."""),
_(u"""- changes.t2t (optional): a list of changes between releases, see [[TranslatingChanges]] for more information."""),
_(u"""- Add-ons (optional): a set of optional features that users can install, see [[TranslatingAddons]] for more information."""),
"",_(u"""## Advantages of the Automatic Workflow Process"""),
_(u"""- No need of a full NVDA development environment."""),
_(u"""- You will be sent an email or twitter message when your po file needs updating."""),
_(u"""- You will be sent an email or twitter message when your userGuide or changes file needs to be updated."""),
_(u"""- Automatic generation of html from t2t files, so that you can check the correctness of your t2t markup."""),
_(u"""- Automatically generated difference and word difference between previous and new versions, to help you quickly find the changes."""),
_(u"""- A higher quality User Guide since the difference files encourage you to keep the English and your localization closely updated."""),
_(u"""- Translation becomes many small tasks instead a big rush near a deadline. Maybe 10 minutes per week on average."""),
_(u"""- It is easier to contribute, since each work unit is self contained."""),
_(u"""- Your translation is regularly and automatically included into NVDA snapshots."""),
_(u"""- Instead of following nvda-dev mailing list emails, you can just subscribe to nvda translations and important messages related to translation will be sent there."""),
_(u"""- Auto generated structure difference between the English and your localized user guide, to quickly spot missing paragraphs, tables and lists."""),
_(u"""- Automatic checking of po files, making sure that there are no mistakes that could cause any runtime errors."""),
"",_(u"""If you want to follow the automatic workflow process, visit the [[TranslatingUsingAutomaticProcess]] page."""),
"",_(u"""## Missing information"""),
_(u"""Please feel free to update this or any subsequent page with any tips or hints that you feel may be of use to other translators."""),
"",_(u"""### Missing Sections"""),
_(u"""If someone could add Sites for Gestures.ini, it'll be done."""),
]