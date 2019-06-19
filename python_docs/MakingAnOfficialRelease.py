# -*- coding: utf-8 -*-
documentation = [
_(u"""# Making an Official Release"""),
"",_(u"""The following instructions are for the release manager and detail how to make an official release."""),
"",_(u"""## Betas"""),
_(u"""* At a point where master is healthy (all checks passing and no known regressions): Merge master into beta."""),
_(u"""* At least one week after the last merge of master into beta, tag beta1. E.g. release-2019.1beta1. Tagging the beta will make the beta show up on the snapshots page, and the auto update system to start offering it to those checking for betas."""),
_(u"""* Periodically look at recent issues filed, specifically looking for those with p1, crash or appcrash labels."""),
_(u"""* Periodically look for prs based on beta and ensure they are reviewed and then approved/merged or rejected. """),
_(u"""* After the final beta, call a translation freeze for 2 weeks. No more commits should be made to the beta branch at this time."""),
_(u"""* As prs based on the beta branch are merged, periodically tag further betas. """),
"",_(u"""## Release candidates"""),
_(u"""* Ensure it is safe to release an rc by looking at recent issues filed, specifically looking for those with p1, crash or appcrash labels."""),
_(u"""* If this is rc1, update translations:"""),
_(u"""    1. Log into exbi and su to nvdal10n."""),
_(u"""    2. `cd ~/mr/mainNVDACode`"""),
_(u"""    3. `mr up`"""),
_(u"""    4. `cd ../srt`"""),
_(u"""    5. `mr up`"""),
_(u"""    6. `mr svn2nvda`"""),
_(u"""* If this is rc1, reset the rc branch to beta. Otherwise, merge rc into beta if necessary."""),
_(u"""* For all other RCs, look for any prs based on rc, and review and approve/merge or reject them."""),
_(u"""* Create an annotated tag for the release with a \"release-\" prefix; e.g. release-2016.1rc1."""),
_(u"""* This will start an AppVeyor build, so wait for the build to complete. As part of this, the release will be staged."""),
_(u"""* Publish the staged release. On exbi, su to the nvaccess user and run `nvdaRelease`"""),
_(u"""* If this is an rc, make a blog post on www.nvaccess.org, placing it in the Development category. It should never be placed in the News category."""),
_(u"""    * Use a previous blog post as a base."""),
_(u"""    * If this is not the first pre-release, include a list of changes since the last pre-release."""),
_(u"""* Spread the word via the nvda-devel and nvda-translations lists and Twitter."""),
_(u"""* Scan the launcher executable with [VirusTotal](http://www.virustotal.com/). Just submit the direct download URL."""),
"",_(u"""If this is a final release:"""),
_(u"""* Mark the release milestone as done on GitHub."""),
_(u"""* Change the milestone set for issues and pull requests automatically closed by GitHub to the next release:"""),
_(u"""    1. Get the milestone id for the new release. The easiest way to do this is to go to https://github.com/nvaccess/nvda/milestones and look at the link URL for the relevant milestone. The number at the end is the id."""),
_(u"""    2. On exbi, edit ~nvaccess/data/nvaServer.conf."""),
_(u"""    3. In the `[nvdaGithub]` section, change the value of `autoCloseMilestone` to the milestone id obtained in step 1."""),
_(u"""    4. Reload uwsgi so the change takes effect: `sudo systemctl reload uwsgi`"""),
_(u"""* Make a blog post on www.nvaccess.org in the Releases category."""),
_(u"""* Post on Facebook."""),
_(u"""* Post to the NV Access News email list."""),
_(u"""* If it hasn't been done already, prepare for the next version (after the one just published) in master:"""),
_(u"""    1. In `source/versionInfo.py`, update the `version_year` and/or `version_major` variables for the next version. If the next version is the first version for that year (e.g. 2018.1), also update `copyrightYears`."""),
_(u"""    2. Add a heading for the next version in `user_docs/en/changes.t2t`."""),
]