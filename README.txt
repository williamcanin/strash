# sTrash

[ ABOUT ]

  sTrash is a simple script for Linux with the function to safely remove FILES
from the recycle bin with no chance of recovery for Linux.

[ DEPENDENCIES ]

  * All distros
  -- shred
  * Arch Linux
  -- python >= 3.9
  -- gio (glib2)
  * Debian
  -- python3 >= 3.9
  -- python3-tk
  -- libglib2.0-dev

[ INSTALL ]

  $ git clone --single-branch https://github.com/williamcanin/strash.git; cd strash
  $ sudo make install

[UNINSTALL]

  $ cd strash
  $ sudo make uninstall

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
    "runtests.sh" will run the "sTrash" tests (strash/strash.py).

    The Python module used for testing is the **unittest**.

[ LICENSE ]

  https://github.com/williamcanin/strash/blob/main/LICENSE

 © sTrash. William C. Canin. All rights reserved. ®
