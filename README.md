# Cranium: Bashing CLI arguments

Because I'm sick of writing `argparse`.

The idea is to

 1. Write argument parsing documentation using `docopt` (in Python)
 2. Use Python `docopt` to parse the arguments and save them as JSON and
 3. Read the JSON file in the shell script


Dependencies
====

```
apt-get install jq  # `brew install jq` for Mac OS
apt-get install pip # `brew install pip` for Mac OS
pip install docopt
```

Usage
====

**Step 1**:

Create a Python file with arguments options and usage definitions that
follows the Python `docopt` style guide, e.g. in `barathrum.py`:

```python
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
```

**Step 2:**

Copy+paste the `main()` function below into the Python file as such:


```python
from __future__ import print_function
import json

from docopt import docopt

if __name__ == '__main__':
    # Remeber to change the version measge and name =)
    arguments = docopt(__doc__, version='Barathrum Example for cranium.sh - version 0.0.1')
    argdict = {}
    for k, v in arguments.items():
        if k.startswith('--'):
            k = k[2:].replace('-', '_')
        argdict[k] = v
    print(json.dumgitps(argdict))
```

**Step 3:**

In your shell script, use the `"$@"` operator to pass all the arguments to the
Python script with `docopt` you've previously written:

```shell
# Input the arguments into a JSON file as specified by `barathrum.py`
python barathrum.py "$@" > arguments.json
```

Then, you can read the variables individually as such:

```shell
# Initialize the arguments according.
dagger=$(cat arguments.json | jq '.["dagger"]')
greater_bash=$(cat arguments.json | jq '.["greater_bash"]')
```


QnA
====

**Q: Why don't you use the [`docopt` for bash](https://github.com/docopt/docopts) directly?**

**A:** Cos I don't want to retype what's in the docstring and initialize the arguments individually. Also, I find it really ugly to have `#?` and `##?` on every line of comment (my personal preference, no offense intended).

----

**Q: Why don't you use [`argparse-bash`](https://github.com/nhoffman/argparse-bash) that also uses Python?**

**A:** Cos I can't write my arguments `--help` message in the docstring.

----

**Q: Is there really a need to ask `Bash` to call `Python` to use `docopt` just to convert the arguments to `JSON` and read it through `jq` in shell?**

**A:** Nope, no need to but I just prefer to read JSON files as opposed to writing `argparse` in shell.


----

**Q: Don't we still have to write the `docopt` docstring in Python to read our customized arguments options?**

**A:** Yes, doesn't that make you arguments parsing the `--help` messages more beautiful?


Similar / Related to
====

 - [argparse-bash](https://github.com/nhoffman/argparse-bash)
 - [docopt](http://docopt.org)
 - [jq](https://stedolan.github.io/jq)
