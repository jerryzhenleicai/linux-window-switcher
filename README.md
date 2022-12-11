
For Linux and other X Window System based desktop OS, this Python script allows you to switch to any given window through a keyboard shortcut, which is in most cases faster than mouse clicking or Alt-Tab.

This tool depends on the xdotool utility from X Windows (apt install xdotool for Debian etc).

### INSTALL:

Just save this file somewhere on your disk.

### Run it:

To switch to the Chrome brower  or Emacs for examples, run

```console
python window_switch.py chrome
```

or

```console
python window_switch.py emacs
```

You can bind hot key shortcuts to these commands (in Gnome for example), so Ctl-Alt-G will switch to Chrome.
