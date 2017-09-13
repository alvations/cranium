# Cranium: Bashing CLI arguments

Because I'm sick of writing `argparse`, similar/related to:

 - [argparse-bash](https://github.com/nhoffman/argparse-bash)
 - [docopt](http://docopt.org)
 - [jq](https://stedolan.github.io/jq)

The idea is

 - write argument parsing documentation using `docopt` (in Python)
 - use Python `docopt` to parse the arguments when calling a bash script


Dependencies
====

```
apt-get install jq  # `brew install jq` for Mac OS
apt-get install pip # `brew install pip` for Mac OS
pip install docopt
```

Usage
====



QnA
====

**Q:** Why don't you use the [`docopt` for bash](https://github.com/docopt/docopts) directly?

**A:** Cos I don't want to retype what's in the docstring and initialize the arguments individually. Also, I find it really ugly to have `#?` and `##?` on every line of comment (my personal preference, no offense intended).

----

**Q:** Why don't you use [`argparse-bash`] that also uses Python?

**A:** Cos I can't write my arguments `--help` message in the docstring.

----

**Q:** Is there really a need to ask `Bash` to call `Python` to use `docopt` just to convert the arguments to `JSON` and read it through `jq` in shell?

**A:** Nope, no need to but I just prefer to read JSON files as opposed to writing `argparse` in shell.


----

**Q:** Don't we still have to write the `docopt` docstring in Python to read our customized arguments options?

**A:** Yes, doesn't that make you arguments parsing the `--help` messages more beautiful?
