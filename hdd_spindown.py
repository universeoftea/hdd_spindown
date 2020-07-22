#!/usr/bin/python3
#
#   hdd_spindown.py
#
#   Copyright 2020, Emil Vejlens
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import subprocess

config_file = '/usr/local/etc/hdd_spindown.cfg'
timeout = 240 # This is ~20 min
apm_setting = 127 # Should be below 128 for spindown

def LoadHDDList(config_file):
    hdd_config = []
    f = open(config_file, 'r')
    for line in f:
        hdd_config.append( line.replace('\n','') )

    return hdd_config[:]

def RunHdparm(timeout, apm_setting, hdd):
    hdd = '/dev/disk/by-id/ata-' + hdd
    try:
        hdparm = subprocess.run(['hdparm', '-S', str(timeout), '-B', str(apm_setting), hdd], check=True)
    except CalledProcessError:
        print('There was an error executing: ', end='')
        print( ' '.join(['hdparm', '-S', str(timeout), '-B', str(apm_setting), hdd]) )


color_endc = '\033[0m'
color_okblue = '\033[94m'
for hdd in LoadHDDList(config_file):
    print(color_okblue, '\nSetting spindown on: ', color_endc, hdd)
    RunHdparm(timeout, apm_setting, hdd)


