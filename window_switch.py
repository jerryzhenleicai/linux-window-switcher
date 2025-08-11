#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

# Copyright 2018 Zhenlei Cai (zcai@gaocan.com) 
# Licensed under the GNU General Public License v3
import subprocess

# Execute a command and capture its output
def run_get_output(cmd):
    result = subprocess.run(cmd.split(' '), capture_output=True, text=True, check=True)
    return  result.stdout

program_name = sys.argv[1] # the program to be focused

# get all windows matching the arg
cmd = 'xdotool search --onlyvisible ' + program_name
# print cmd
wins = list(sorted([x.strip() for x in run_get_output(cmd).split("\n") if x !='']))

wins = list(filter(lambda x : not 'Defaulting to search' in x , wins))

print("Matching wins" , wins)

if len(wins) > 0:
    # at least one candidate found , we need to check if the active window is among the candidates (for cycling)
    #wins = wins[2:]

    # Get the id of the active window
    active_window = run_get_output('xdotool getactivewindow')
    print('active', active_window)

    desired_window = -1
    if active_window not in wins:
        # if the active window is not among the candidate windows
        # ..just show the first candidate window
        desired_window = 0
    else:
        # we are already showing one of the candidate windows
        # show the *next* candidate in the list (cycling)
        desired_window = (wins.index(active_window)+1) % len(wins)


    print ('desired ', desired_window)
    # tell wmcontrol to display the next_window
    curr_window = None
    print("Showing ", wins[desired_window])
    os.system('xdotool windowactivate %s' % (wins[desired_window],) )

else : # no windows open which fit the pattern of program_name
    # print 'open new prog'
    os.system("%s &" % (program_name,)) # open new window
