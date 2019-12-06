# -*- coding: utf-8 -*-
documentation = [
_(u"""# Using AppVeyor to manage NVDA add-ons """),
"",_(u"""## Procedure to build and attach nvda-addon files to releases on GitHub"""),
"",_(u"""This can be used to automate the building of NVDA add-ons (binaries with the .nvda-addon extension), which will be uploaded from Appveyor to GitHub, and attached to the created release."""),
"",_(u"""It works for add-ons based on the [Add-on Template](https://github.com/nvdaaddons/addontemplate)."""),
"",_(u"""### Setting AppVeyor for add-ons"""),
"",_(u"""1. Get the code of an add-on."""),
"",_(u"""	Example:"""),
"",_(u"""	```"""),
_(u"""	git clone https://github.com/username/repo"""),
"",_(u"""	git pull"""),
_(u"""	```"""),
_(u"""2. In the root of the add-on folder (where the sconstruct file is placed), paste this [AppVeyor configuration file](https://gist.github.com/nvdaes/a486e45b98566d530688f6da9ce75f84/raw/d05b620185a58327b39da1215cf3c13c01249031/appveyor.yml) (appveyor.yml)."""),
"",_(u"""3. If you don't have it, [create a personal API access token](https://github.com/settings/tokens) and [encrypt it](https://ci.appveyor.com/tools/encrypt)."""),
"",_(u"""	Note: you could need to set the following token scopes to avoid  inconvenience when releasing tags:"""),
"",_(u"""	- notifications"""),
_(u"""	- public_repo"""),
_(u"""	- repo:status"""),
_(u"""	- repo_deployment"""),
"",_(u"""4. In the appveyor.yml file, replace the value provided for the secure key with your encrypted token. For instance, instead of"""),
"",_(u"""	```"""),
_(u"""	  auth_token:"""),
_(u"""	    secure: 3yxF2EQ/wfLKNEobcRfdNL6srjXjoMdRa/LSQ7z2PJNqOL3IEyiFtlnxxHeIQskH"""),
_(u"""	```"""),
"",_(u"""	```"""),
_(u"""	  auth_token:"""),
_(u"""	    secure: yourEncryptedToken"""),
_(u"""	```"""),
"",_(u"""	Now, you can paste your appveyor.yml file to any add-on posted on your GitHub account."""),
"",_(u"""5. [Sign in with AppVeyor](https://www.appveyor.com/)."""),
"",_(u"""6. From AppVeyor, select New Project. (If needed, choose GitHub and authorize it)."""),
"",_(u"""7. Locate the name of the repo you're interested in, move the mouse over it (for instance pressing NVDA+numpadDivide or NVDA+shift+m), and activate the \"Add\" link below."""),
"",_(u"""### Releasing"""),
"",_(u"""To post a new release of an add-on, you can create a tag and push it to GitHub:"""),
"",_(u"""Example"""),
"",_(u"""```"""),
_(u"""git tag 1.0"""),
"",_(u"""git push origin 1.0"""),
_(u"""```"""),
"",_(u"""Now, the release will be created and binary-1.0.nvda-addon will be attached on GitHub."""),
"",_(u"""Bonus track: Also, Abdel has created an [appveyorForFTP.yml file](https://gist.githubusercontent.com/nvdaes/a486e45b98566d530688f6da9ce75f84/raw/46236e04b02de117f9edbb30aaf626692116b6c3/appveyorForFTP.yml) for releasing using an FTP server."""),
"",_(u"""## Personal deployment environment"""),
"",_(u"""In the example above, we've described how to introduce the encrypted key of your GitHub personal token in the appveyor.yml file."""),
"",_(u"""If you want to keep this personal key, without sharing it in your repo, you can create a personal deployment environment."""),
"",_(u"""For that, go to [your appveyor environment page](https://ci.appveyor.com/environments) and click on the \"New environment\" link."""),
"",_(u"""Once in the new environment creation page, we describe below the procedure for creating a deployment for GitHub, as well as an FTP deployment:"""),
"",_(u"""### Creating a personal deployment environment for GitHub"""),
"",_(u"""To create a personal deployment environment for GitHub, you should make the following choices."""),
"",_(u"""The $(REPO_NAME) environment variable used in the release description was created in the before_deploy section of [this appveyor.yml configuration file](https://gist.githubusercontent.com/abdel792/708a787bb79b265c32b66e363e9cb5c1/raw/3757add3bd8a3d872453f949109b38769d28592d/appveyor.yml)."""),
"",_(u"""You must use this personal deployment environment with its appropriate configuration file so that it can recognize the name of the add-on in its description."""),
"",_(u"""1. Provider: GitHub Releases"""),
"",_(u"""2. Environment name: GitHub_deployment"""),
"",_(u"""3. Tag name: $(APPVEYOR_REPO_TAG_NAME)"""),
"",_(u"""4. Release name: Release $(APPVEYOR_REPO_TAG_NAME)"""),
"",_(u"""5. Release description: This is the release $(APPVEYOR_REPO_TAG_NAME) of the $(REPO_NAME) addon for the NVDA screen reader built and uploaded to GitHub using Appveyor."""),
"",_(u"""6. GitHub authentication token: Your personal GitHub token. (Warning: This is your personal GitHub token, not your encrypted key with Appveyor)"""),
"",_(u"""7. Repository name: Leave empty, this field is optional"""),
_(u""" """),
_(u"""8. Artifact(s) to deploy: addon"""),
"",_(u"""This done, submit your form by validating \"Add environment\" button."""),
"",_(u"""### Creating a personal deployment environment for FTP"""),
"",_(u"""To create a personal deployment environment for FTP, you should make the following choices:"""),
"",_(u"""1. Provider: FTP """),
"",_(u"""2. Environment name: ftp_deployment"""),
"",_(u"""3. Protocol: FTP """),
"",_(u"""4. Host: Your host."""),
"",_(u"""5. Active mode: Leave empty, this field is optional """),
"",_(u"""6. Username: Your username"""),
"",_(u"""7. Password: Your password"""),
"",_(u"""8. Remote folder: The name of the folder that will contain the add-on on your FTP server. (It can be something like /nvda-addons or /add-ons)"""),
"",_(u"""9. Artifact(s): addon"""),
"",_(u"""10. Application: Leave empty, this field is optional"""),
_(u""" """),
_(u"""11. Use alternative FTP library (beta): Leave empty, this field is optional """),
"",_(u"""This done, submit your form by validating \"Add environment\" button."""),
"",_(u"""### Adding the deploy section for personal environments"""),
"",_(u"""Once your personal environment has been added, you'll just have to add the following deploy section to your appveyor.yml file, mentioning only the name you have chosen for your environment"""),
"",_(u"""1. For GitHub deployment:"""),
"",_(u"""	```"""),
_(u"""	deploy:"""),
_(u"""	- provider: Environment"""),
_(u"""	  name: GitHub_deployment"""),
_(u"""	  on:"""),
_(u"""	    APPVEYOR_REPO_TAG: true"""),
_(u"""	```"""),
_(u"""	Example of [appveyor configuration file for GitHub personal deployment environment](https://gist.githubusercontent.com/abdel792/708a787bb79b265c32b66e363e9cb5c1/raw/3757add3bd8a3d872453f949109b38769d28592d/appveyor.yml)"""),
_(u"""2. For FTP deployment:"""),
"",_(u"""	```"""),
_(u"""	deploy:"""),
_(u"""	- provider: Environment"""),
_(u"""	  name: ftp_deployment"""),
_(u"""	  on:"""),
_(u"""	    APPVEYOR_REPO_TAG: true"""),
_(u"""	```"""),
_(u"""	Example of [appveyor configuration file for FTP personal deployment environment](https://gist.githubusercontent.com/abdel792/58c7fa82c44df08b06d2674bb8bd6c70/raw/75eede89b1702df923d36fdccc2ccc47b7046cc1/appveyorForFTP.yml)"""),
"","",_(u"""## Procedure to receive notifications about commits"""),
"",_(u"""For notifications about push events (recommended for add-ons review), please see:"""),
_(u"""https://github.com/nvdaaddons/nvdaaddons.github.io/wiki/githubWebhooks"""),
"",_(u"""Anyway, if you want to use AppVeyor: """),
"",_(u"""1. Create an email address to receive notifications. For instance, you may use the [groups.io email integration](https://groups.io/static/features)."""),
"",_(u"""2. In the appveyor.yml file, add these lines:"""),
"",_(u"""	```"""),
"",_(u"""	notifications:"""),
_(u"""	  - provider: Email"""),
_(u"""	    to:"""),
_(u"""	      - notificationsEmailAddress.example.com"""),
"",_(u"""	```"""),
"",_(u"""	Replace notificationsEmailAddress.example.com with a valid email address."""),
"",_(u"""	Here is a [topic in groups.io mailing list as a real example](https://nvdaes.groups.io/g/NVDAADDONSCOMMITS/topic/build_completed/27377767)."""),
"",_(u"""## References"""),
"",_(u"""- [Appveyor.yml reference](https://www.appveyor.com/docs/appveyor-yml/)"""),
_(u"""- [Publishing artifacts to GitHub Releases | AppVeyor](https://www.appveyor.com/docs/deployment/github/#configuring-in-appveyoryml)"""),
_(u"""- [Syntax of the release name value in the deploy section of the appveyor.yml configuration file](http://help.appveyor.com/discussions/questions/9221-syntax-of-the-release-name-value-in-the-deploy-section-of-the-appveyoryml-configuration-file)"""),
_(u"""- [mesa/appveyor.yml at master · anholt/mesa](https://github.com/anholt/mesa/blob/master/appveyor.yml)"""),
_(u"""- [Discussion on the NVDA add-ons mailing list](https://nvda-addons.groups.io/g/nvda-addons/topic/6220467)"""),
_(u"""- [Updates for appveyor by Abdel on the NVDA add-ons mailing list](https://nvda-addons.groups.io/g/nvda-addons/topic/31686195#7943)"""),
"",_(u"""## Acknowledgements"""),
"",_(u"""Thanks to @abdel792, @derekriemer and @tuukao for making this possible."""),
]