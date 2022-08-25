# Strash

[ ABOUT ]

  Strash is a simple script for Linux with the function to safely remove FILES
from the recycle bin with no chance of recovery.

[ VERSION ]

  Current: 1.0.3

[ DEPENDENCIES ]

  * Linux System
  * find
  * sed
  * gio (glib2)
  * shred

[ INSTALL ]

  # make install

[UNINSTALL]

  # make uninstall

[ USAGE ]

  For information on how to use it, run the command below:

    $ strash -h

[ DEVELOPER ]

  Preparing machine for development:

  A - Create a virtual machine:

    $ git clone --single-branch https://github.com/williamcanin/strash.git; cd strash
    $ python3 -m venv .venv

  B - Enable virtual machine:

    $ . venv/bin/activate

  Tests:

    The file to run tests can be found in the "tests" folder. The file
    "runtests.sh" will run the "Strash" tests (strash/strash.py).

    The Python module used for testing is the **unittest**.

[ LICENSE ]

  https://github.com/williamcanin/strash/blob/main/LICENSE

 © Strash. William C. Canin. All rights reserved. ®