# Automatic docky chrome duplicate fix spurred by manual solution from here:
# http://kb.openstudioproject.com/content/fix-double-google-chrome-icon-docky-and-plank

import fileinput

# Section end identifiers
comparison = ['X-Ayatana-Desktop-Shortcuts=NewWindow;NewIncognito', 'TargetEnvironment=Unity']

for line in fileinput.input('/usr/share/applications/google-chrome.desktop', inplace=1):
  print line,
  for string in comparison:
    if line.startswith(string):
      print 'StartupWMClass=Google-chrome-stable'
