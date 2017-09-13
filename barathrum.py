#!/usr/bin/env python
# -*- coding utf-8 -*-

"""
Barathrum needs the ancient scroll `FILE` in order to open the portal to the
etheral realm where the streets are laid with Etherum.

Feed a `FILE` to `barathrum.py` and it will check whether your `FILE` is worthy
of opening the portal.

Usage:
  barathrum.py FILE [-g BASHLVL] [-e HASTELVL] [-d] [-n]
  barathrum.py (-h | --help)
  barathrum.py --version

Options:
  -g --greater-bash=BASHLVL     Sets the level to knocking back enemies [default: 0].
  -n --nether-strike            Shifts into elemental realm and reappearing up close to the enemies.
  -e --empower-haste=HASTELVL   Increases speed and inspires nearby allies to keep up the pace [default: 1].
  -d --dagger                   Use the dagger to teleport a short distant.
  --version                     Show version.
  -h --help                     Show this screen.
"""

from __future__ import print_function
import json

from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Barathrum Example for cranium.sh - version 0.0.1')
    del arguments['--version']
    del arguments['--help']
    argdict = {}
    for k, v in arguments.items():
        if k.startswith('--'):
            k = k[2:].replace('-', '_')
        argdict[k] = v
    print(json.dumps(argdict))
