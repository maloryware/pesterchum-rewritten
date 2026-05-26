<h1 align="center" style="font-family: 'Courier New';">
    <b>
        <img alt="PESTERCHUM" src="assets/img/repo/pcrw.png">
        </b>
    <a href="https://github.com/maloryware/pesterchum-rewritten/releases"><img alt="GitHub all releases" src="https://img.shields.io/github/downloads/maloryware/pesterchum-rewritten/total?style=for-the-badge"></a>
    <a href="https://discord.gg/BbHvdwN"><img alt="Community Discord" src="https://img.shields.io/discord/761299023121350726?color=blue&label=COMMUNITY%20DISCORD&logo=discord&style=for-the-badge"></a>
    <a href="https://discord.gg/eKbP6pvUmZ"><img alt="Support Discord" src="https://img.shields.io/discord/906250212362842143?color=blue&label=SUPPORT%20DISCORD&logo=discord&style=for-the-badge"></a>
    <br>
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/maloryware/pesterchum-rewritten?style=for-the-badge">
    <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/maloryware/pesterchum-rewritten?style=for-the-badge">
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge"></a>
</h1>
<img alt="PESTERCHUM" align="right" src="assets/img/repo/Pesterchum.png">

# Pesterchum Rewritten

*Pesterchum is an instant messaging client copying the look and feel of clients from Andrew Hussie's webcomic Homestuck.*

This repository is a clean, modernized version of [ghostDunk's Pesterchum](https://github.com/illuminatedwax/pesterchum/), based on [Lumi's Fork (Pesterchum Alt Servers)](https://github.com/Dpeta/pesterchum-alt-servers/releases), written from the ground up.

Some resources have been reused, such as themes and fonts.

## PLANNED FEATURES
<details>
<summary> Every feature from Lumi's Fork <b>[click to expand]</b>: </summary>

 - Updated dependencies; [Python 2 --> Python 3](https://www.python.org/doc/sunset-python-2/) // [Qt4 --> Qt5 & Qt6](https://www.qt.io/blog/2014/11/27/qt-4-8-x-support-to-be-extended-for-another-year)
 - Server Selection GUI
 - Client -> Server [TLS/SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) encryption
 - UTF-8 encoded text (emojis, non-western characters)
 - IRCv3 metadata protocol usage for privacy ("`previously any IRC user could see who you were messaging since it would send out a public GETMOOD request`")
 *- Tentative support for communicating color and timeline via [IRCv3 Message Tags/TAGMSG](https://ircv3.net/specs/extensions/message-tags#the-tagmsg-tag-only-message)
 - Expanded quirk customization: **Gradients**, **smilies/links exclusion**
 - Theme 
 - Funky [win95-theme](https://www.pesterchum.xyz/img/win95.png) by [cubicSimulation](https://twitter.com/cubicSimulation) <img width="24" src="themes/win95chum/trayiconpng">
 - Works better with high resolutions since size scales via Qt's [high DPI scaling](https://doc.qt.io/qt-6/highdpi.html) (https://github.com/Dpeta/pesterchum-alt-servers/issues/66)
 - Usable with Wayland on Linux, it used to break because of the way Pesterchum set its window position
 - Excecutables build with PyInstaller, allows for a smaller release filesize + dlls can be include with the binary
 - Lots of fixes for miscellaneous crashes/issues. . . check out the <a href="CHANGELOG.md">CHANGELOG</a>! :3
</details>
 - Built-in auto-updater


[CHANGELOG.md]: https://github.com/Dpeta/pesterchum-alt-servers/blob/main/CHANGELOG.md
[TODO.md]: https://github.com/Dpeta/pesterchum-alt-servers/blob/main/TODO.md

## INSTALLATION <img width="40" src="assets/smilies/headbonk.gif">

TBA

## DOCUMENTATION <img width="40" src="assets/smilies/theprofessor.png">

### Old Documentation
Additional, old resources, provided both because they still provide useful information, and for archival.
 - <a href="docs/themes.txt">HOW TO MAKE YOUR OWN THEME</a>
 - <a href="docs/trollquirks.mkdn">Canon troll quirk guide (REGEXP REPLACE)</a>
 - <a href="docs/PYQUIRKS.mkdn">Guide for setting up Python quirk functions</a>

Files available in [assets/docs/legacy](assets/docs/legacy).


### Wiki
I've been adding some info to [the wiki](https://github.com/Dpeta/pesterchum-alt-servers/wiki), the available pages as of me updating this readme are:
 - [Handle registration and ownership (nickServ)](https://github.com/Dpeta/pesterchum-alt-servers/wiki/Handle-registration-and-ownership)
 - [Memo registration and ownership (chanServ)](https://github.com/Dpeta/pesterchum-alt-servers/wiki/Memo-registration-and-ownership)

Some useful off-repo guides:
 - [How to register your handle with nickServ](https://squidmaid.tumblr.com/post/67595522089/how-to-register-your-pesterchum-handle-the-actual)
 - [Collection of gradient quirk function guides](https://paste.0xfc.de/?e60df5a155e93583#AmcgN9cRnCcBycmVMvw6KJ1YLKPXGbaSzZLbgAhoNCQD
)

The old READMEs are also preserved in the [docs](docs) folder:
- <a href="assets/docs/legacy/README-pesterchum.mkdn"> illuminatedWax's README</a>
- <a href="assets/docs/legacy/README-karxi.mkdn "> karxi's README</a>
- <a href="assets/docs/legacy/TODO.mkdn "> karxi's TODO</a>
- <a href="assets/docs/legacy/CHANGELOG-karxi.mkdn "> karxi's CHANGELOG</a>

## RUNNING FROM SOURCE <img src="assets/smilies/tab.gif">

TBA

### DEPENDENCIES
 - **[Python 3]**
     - Ideally 3.8 or later. Though older versions may still work, I don't intend to test them.
 - **[PySide6]**
	- PyQt5 support will not be provided for this version, as the intention is to start fresh and define a new baseline.
    - PyQt6 bindings have been replaced with PySide (official Python Qt bindings).
 - (Optional) **[certifi]**
 	- Provides alternative root certificates for TLS certificate validation. 
	- Useful for MacOS, as Python doesn't use the system-provided certificates because of MacOS' outdated SSL library. Also miscellaneous systems without usable root certificates.
 
### WALKTHROUGH

TBA
 
## FREEZE / BUILD <img src="assets/themes/win95chum/admin.png">

TBA

## SMILIES <img height="32" alt="pesterchum 'WHAT DID YOU DO' smilie" src="assets/smilies/whatdidyoudo.gif">

| Text                 | Smilie                                                                                              |
|:---------------------|:----------------------------------------------------------------------------------------------------|
| `:rancorous:`        | <img alt=':rancorous: pesterchum smilie/emote' src='assets/smilies/pc_rancorous.png'>               |
| `:apple:`            | <img alt=':apple: pesterchum smilie/emote' src='assets/smilies/apple.png'>                          |
| `:bathearst:`        | <img alt=':bathearst: pesterchum smilie/emote' src='assets/smilies/bathearst.png'>                  |
| `:cathearst:`        | <img alt=':cathearst: pesterchum smilie/emote' src='assets/smilies/cathearst.png'>                  |
| `:woeful:`           | <img alt=':woeful: pesterchum smilie/emote' src='assets/smilies/pc_bemused.png'>                    |
| `:sorrow:`           | <img alt=':sorrow: pesterchum smilie/emote' src='assets/smilies/blacktear.png'>                     |
| `:pleasant:`         | <img alt=':pleasant: pesterchum smilie/emote' src='assets/smilies/pc_pleasant.png'>                 |
| `:blueghost:`        | <img alt=':blueghost: pesterchum smilie/emote' src='assets/smilies/blueslimer.gif'>                 |
| `:slimer:`           | <img alt=':slimer: pesterchum smilie/emote' src='assets/smilies/slimer.gif'>                        |
| `:candycorn:`        | <img alt=':candycorn: pesterchum smilie/emote' src='assets/smilies/candycorn.png'>                  |
| `:cheer:`            | <img alt=':cheer: pesterchum smilie/emote' src='assets/smilies/cheer.gif'>                          |
| `:duhjohn:`          | <img alt=':duhjohn: pesterchum smilie/emote' src='assets/smilies/confusedjohn.gif'>                 |
| `:datrump:`          | <img alt=':datrump: pesterchum smilie/emote' src='assets/smilies/datrump.png'>                      |
| `:facepalm:`         | <img alt=':facepalm: pesterchum smilie/emote' src='assets/smilies/facepalm.png'>                    |
| `:bonk:`             | <img alt=':bonk: pesterchum smilie/emote' src='assets/smilies/headbonk.gif'>                        |
| `:mspa:`             | <img alt=':mspa: pesterchum smilie/emote' src='assets/smilies/mspa_face.png'>                       |
| `:gun:`              | <img alt=':gun: pesterchum smilie/emote' src='assets/smilies/mspa_reader.gif'>                      |
| `:cal:`              | <img alt=':cal: pesterchum smilie/emote' src='assets/smilies/lilcal.png'>                           |
| `:amazedfirman:`     | <img alt=':amazedfirman: pesterchum smilie/emote' src='assets/smilies/pc_amazedfirman.png'>         |
| `:amazed:`           | <img alt=':amazed: pesterchum smilie/emote' src='assets/smilies/pc_amazed.png'>                     |
| `:chummy:`           | <img alt=':chummy: pesterchum smilie/emote' src='assets/smilies/pc_chummy.png'>                     |
| `:cool:`             | <img alt=':cool: pesterchum smilie/emote' src='assets/smilies/pccool.png'>                          |
| `:smooth:`           | <img alt=':smooth: pesterchum smilie/emote' src='assets/smilies/pccool.png'>                        |
| `:distraughtfirman:` | <img alt=':distraughtfirman: pesterchum smilie/emote' src='assets/smilies/pc_distraughtfirman.png'> |
| `:distraught:`       | <img alt=':distraught: pesterchum smilie/emote' src='assets/smilies/pc_distraught.png'>             |
| `:insolent:`         | <img alt=':insolent: pesterchum smilie/emote' src='assets/smilies/pc_insolent.png'>                 |
| `:bemused:`          | <img alt=':bemused: pesterchum smilie/emote' src='assets/smilies/pc_bemused.png'>                   |
| `:3:`                | <img alt=':3: pesterchum smilie/emote' src='assets/smilies/pckitty.png'>                            |
| `:mystified:`        | <img alt=':mystified: pesterchum smilie/emote' src='assets/smilies/pc_mystified.png'>               |
| `:pranky:`           | <img alt=':pranky: pesterchum smilie/emote' src='assets/smilies/pc_pranky.png'>                     |
| `:tense:`            | <img alt=':tense: pesterchum smilie/emote' src='assets/smilies/pc_tense.png'>                       |
| `:record:`           | <img alt=':record: pesterchum smilie/emote' src='assets/smilies/record.gif'>                        |
| `:squiddle:`         | <img alt=':squiddle: pesterchum smilie/emote' src='assets/smilies/squiddle.gif'>                    |
| `:tab:`              | <img alt=':tab: pesterchum smilie/emote' src='assets/smilies/tab.gif'>                              |
| `:beetip:`           | <img alt=':beetip: pesterchum smilie/emote' src='assets/smilies/theprofessor.png'>                  |
| `:flipout:`          | <img alt=':flipout: pesterchum smilie/emote' src='assets/smilies/weasel.gif'>                       |
| `:befuddled:`        | <img alt=':befuddled: pesterchum smilie/emote' src='assets/smilies/what.png'>                       |
| `:pumpkin:`          | <img alt=':pumpkin: pesterchum smilie/emote' src='assets/smilies/whatpumpkin.png'>                  |
| `:trollcool:`        | <img alt=':trollcool: pesterchum smilie/emote' src='assets/smilies/trollcool.png'>                  |
| `:jadecry:`          | <img alt=':jadecry: pesterchum smilie/emote' src='assets/smilies/jadespritehead.gif'>               |
| `:ecstatic:`         | <img alt=':ecstatic: pesterchum smilie/emote' src='assets/smilies/ecstatic.png'>                    |
| `:relaxed:`          | <img alt=':relaxed: pesterchum smilie/emote' src='assets/smilies/relaxed.png'>                      |
| `:discontent:`       | <img alt=':discontent: pesterchum smilie/emote' src='assets/smilies/discontent.png'>                |
| `:devious:`          | <img alt=':devious: pesterchum smilie/emote' src='assets/smilies/devious.png'>                      |
| `:sleek:`            | <img alt=':sleek: pesterchum smilie/emote' src='assets/smilies/sleek.png'>                          |
| `:detestful:`        | <img alt=':detestful: pesterchum smilie/emote' src='assets/smilies/detestful.png'>                  |
| `:mirthful:`         | <img alt=':mirthful: pesterchum smilie/emote' src='assets/smilies/mirthful.png'>                    |
| `:manipulative:`     | <img alt=':manipulative: pesterchum smilie/emote' src='assets/smilies/manipulative.png'>            |
| `:vigorous:`         | <img alt=':vigorous: pesterchum smilie/emote' src='assets/smilies/vigorous.png'>                    |
| `:perky:`            | <img alt=':perky: pesterchum smilie/emote' src='assets/smilies/perky.png'>                          |
| `:acceptant:`        | <img alt=':acceptant: pesterchum smilie/emote' src='assets/smilies/acceptant.png'>                  |
| `:olliesouty:`       | <img alt=':olliesouty: pesterchum smilie/emote' src='assets/smilies/olliesouty.gif'>                |
| `:billiards:`        | <img alt=':billiards: pesterchum smilie/emote' src='assets/smilies/poolballS.gif'>                  |
| `:billiardslarge:`   | <img alt=':billiardslarge: pesterchum smilie/emote' src='assets/smilies/poolballL.gif'>             |
| `:whatdidyoudo:`     | <img alt=':whatdidyoudo: pesterchum smilie/emote' src='assets/smilies/whatdidyoudo.gif'>            |
| `:brocool:`          | <img alt=':brocool: pesterchum smilie/emote' src='assets/smilies/pcstrider.png'>                    |
| `:trollbro:`         | <img alt=':trollbro: pesterchum smilie/emote' src='assets/smilies/trollbro.png'>                    |
| `:playagame:`        | <img alt=':playagame: pesterchum smilie/emote' src='assets/smilies/saw.gif'>                        |
| `:trollc00l:`        | <img alt=':trollc00l: pesterchum smilie/emote' src='assets/smilies/trollc00l.gif'>                  |
| `:suckers:`          | <img alt=':suckers: pesterchum smilie/emote' src='assets/smilies/Suckers.gif'>                      |
| `:scorpio:`          | <img alt=':scorpio: pesterchum smilie/emote' src='assets/smilies/scorpio.gif'>                      |
| `:shades:`           | <img alt=':shades: pesterchum smilie/emote' src='assets/smilies/shades.png'>                        |
| `:honk:`             | <img alt=':honk: pesterchum smilie/emote' src='assets/smilies/honk.png'>                            |
