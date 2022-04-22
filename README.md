[![Pylint](https://github.com/THE-ORONCO/weirdBirbDiscordBot/actions/workflows/pylint.yml/badge.svg?branch=master)](https://github.com/THE-ORONCO/weirdBirbDiscordBot/actions/workflows/pylint.yml)
# Weird-Birb-Bot
Just a weird birb being a bot on any discord server you want.

# TODO
- [ ] explain how to use / install / start
- [ ] fix `bash ./setup.sh` for windows
- [ ] maybe create setup script to inject stuff like bot token & command character etc. into a .env file
- [ ] find ideas for functionality
  - [ ] intelligent CTF-time scraping including discord links etc. from organizers website
  - [ ] file watching for cogs with pyinotify & automatic reloading with bot.reload_extension("name") on file changes
  - [ ] shit list of users who are bad and automatic suspension / kicking / banning on that
  - [ ] depending on command automatic deletion of invoking message and old results
- [ ] proper setup script
  - [ ] TODO do some string sanitation
  - [ ] TODO maybe split up secret and public information for integration with other services later on
  - [ ] TODO allow for the creation of an empty .env file with only the required variables / default values
- [ ] add unit testing
- [ ] add automatic deployment (maybe to server or raspberry)