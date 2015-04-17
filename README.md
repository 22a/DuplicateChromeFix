# Docky Duplicate Chrome Icon Fix

This is just a simple script for automating the [fix](http://kb.openstudioproject.com/content/fix-double-google-chrome-icon-docky-and-plank) for duplicate chrome icons in docky.

### Why Does This Exist?
I needed it. You may find this useful too if you're running [fauxS-X](https://github.com/c-brenn/FauxSX) or a similar desktop environment using [docky](www.go-docky.com/) and are experiencing double Google Chrome icons like these:
![Duplicate Example](http://22a.me/git/dockyFix/duplicate.png)

As the above [fix](http://kb.openstudioproject.com/content/fix-double-google-chrome-icon-docky-and-plank) shows, you could manually edit your desktop file and add the lines where necessary, or you could run this script. I write it because I had to manually edit the file every time I updated Chrome.

### How To Run
Clone repo and cd into it:

```sh
git clone {{repolink}}
cd swag
```
Run script as sudo user:

```sh
sudo python dsk_fix.py
```
