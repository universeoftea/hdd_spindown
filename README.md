A simple python script to set the spindown time of harddrives to 20 minutes at boot.

Depends on:
*hdparm*
*python3*
*systemd*

Simply drop *hdd_spindown.py* to */usr/local/bin/* and *hdd_spindown.cfg* to */usr/local/etc/* and add the ID of the HDDs to the *.cfg* file. There are two example IDs currently in the file. The id is based on the path to the block device, which should be something like */dev/disk/by-id/ata-[ID]* (Without the square brackets).

The *hdd_spindown.service* file should live in */etc/systemd/system/*
Simply run the following commands to add the service once the files are copied:

*systemctl daemon-reload*
*systemctl enable hdd_spindown.service*

If you're too lazy to wait for the next reboot (I am):

*systemctl start hdd_spindown.service*

Feel free to adjust paths and timeout period in the python script itself.

### COPYRIGHT & LICENSE ###

    *hdparm*, *python3* and *systemd* are not affiliated with this program.
    They are distributed separately with their respective license and copyright.


    Copyright 2020, Emil Vejlens

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
