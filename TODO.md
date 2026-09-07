beta, core features:
- [ ] data system (user, config)
- [ ] home widget
- [ ] settings widget
- [ ] userlist widget
- [ ] chat widget
- [ ] memo widget
- [ ] data system (theme)
- [ ] irc functionality
- [ ] pyinstaller packaging

bugs:
- n/a

late-stage core features:
- quirks
- in-message smilies
- ssl/tls encryption

super late-stage features:
- auto-updater

bonus:
- broadcast text color info thru metadata (+ builtin gradient support) -- maybe server-cached?
- enable text color toggling & background color control for text that blends with the theme
- persistent chat history
- user list sorting
- profile migration
- opening pesterchum with a running instance prompts user to select
  whether they want to open a new instance, or open their running one
- tts/stt for accessibility


bugs present in alt-servers:
- SSLEof (beats me)
- unplugged audio devices are entirely forgotten (store preferences, go by order, skip unavailable during selection)
- quirk panel breaking when a quirk script is removed (will become obsolete with built-in gradients)
