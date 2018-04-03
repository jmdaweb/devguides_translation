# -*- coding: utf-8 -*-
documentation = [
_(u"""# Make add-ons translatable throught the NVDA's translation system #"""),
"",_(u"""## Steps ##"""),
"",_(u"""1. Authors request the inclusion of an add-on in the translation system via the [NVDA add-ons mailing list](https://nvda-addons.groups.io/g/nvda-addons)."""),
_(u"""2. A member of the NVDA add-on team creates a repo for the add-on at"""),
_(u"""<https://bitbucket.org/nvdaaddonteam>"""),
_(u"""	- If the author has a Bitbucket account, s/he can request admin access to the add-on repo, and write access to [add-on files](https://bitbucket.org/nvdaaddonteam/addonFiles)."""),
_(u"""	- The add-on repo must contain a branch named stable, where authors or other people with write access to the repo should merge code considered stable when the add-on is updated. This branch is used to send translatable messages to, and receive l10n updates from, the [NVDA translation repo](http://subversion.assembla.com/svn/screenReaderTranslations)."""),
"",_(u"""3. Admins register the add-on and commit settings for translators from Exbi server (nvdal10n@exbi.nvaccess.org):"""),
_(u"""	- cd into mr"""),
_(u"""	- mr up"""),
_(u"""	- cd available.d"""),
_(u"""	- mr registerAddon addonRepoName"""),
_(u"""	- git push"""),
_(u"""	- cd into mr/addons/addonRepoName"""),
_(u"""	- mr addon2settings"""),
_(u"""	- cd ~/mr/srt"""),
_(u"""	- svn commit */settings -m \"Make blah add-on available for translation.\""""),
"",_(u"""4. edit addonFiles/automatic.crontab, so that l10n updates are merged into the stable branch, and translators receive new messages automatically."""),
_(u"""	- Copy one of the lines for one of the existing addons, just change the addon name and paste it in the correct section, commit and push."""),
_(u"""	- Note: Admins can perform the above process manually, running mr addon2svn and mr svn2addon from Exbi."""),
"",_(u"""## Related links ##"""),
"",_(u"""- [Adding a New Language to Ikiwiki](https://github.com/nvaccess/l10n-code/wiki/Adding-a-New-Language-to-Ikiwiki)"""),
"",_(u"""## Aknowledgements ##"""),
"",_(u"""This document is based on work and information provided by Mesar Hameed and James Teh."""),
"",_(u"""Thanks for making this possible."""),
]