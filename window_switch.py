#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import commands

# Copyright 2018 Zhenlei Cai (zcai@gaocan.com) 
# Licensed under the GNU General Public License v3

program_name = sys.argv[1] # the program to be focused

# get all windows matching the arg
cmd = 'xdotool search ' + program_name
# print cmd
wins = list(sorted([x.strip() for x in commands.getoutput(cmd).split("\n") if x !='']))

wins = filter(lambda x : not 'Defaulting to search' in x , wins)


if len(wins) > 0:
    # at least one candidate found , we need to check if the active window is among the candidates (for cycling)
    #wins = wins[2:]

    # Get the id of the active window
    active_window = commands.getoutput('xdotool getactivewindow')
    #print 'active', active_window

    next_window = -1
    if active_window not in wins:
        # if the active window is not among the candidate windows
        # ..just show the first candidate window
        next_window = 0
    else:
        # we are already showing one of the candidate windows
        # show the *next* candidate in the list (cycling)
        next_window = (wins.index(active_window)+1) % len(wins)


    # print 'next ', next_window
    # tell wmcontrol to display the next_window
    curr_window = None
    while True:
        os.system('xdotool windowactivate %s' % (wins[next_window],) )
        curr_window = commands.getoutput('xdotool getactivewindow')
        if curr_window == wins[next_window]:
            break

        next_window = (next_window+1) % len(wins)

else : # no windows open which fit the pattern of program_name
    # print 'open new prog'
    os.system("%s &" % (program_name,)) # open new window
