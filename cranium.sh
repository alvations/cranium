#!/bin/bash

# Reads the arguments into a JSON file as specified by `barathrum.py`
python barathrum.py "$@" > arguments.json

# Initialize the arguments according.
dagger=$(cat arguments.json | jq '.["dagger"]')
greater_bash=$(cat arguments.json | jq '.["greater_bash"]')
greater_bash=$(cat arguments.json | jq '.["greater_bash"]' | sed -e 's/^"//' -e 's/"$//')

# Et voila!
echo $dagger
echo $greater_bash

# You can change the variable name too!
e=$(cat arguments.json | jq '.["empower_haste"]')
echo $e


# Or you can read all the variables as such:
# (Credits goes to Chepner, see https://stackoverflow.com/a/46187922/610569)
while read -r name value; do
   declare "$name=$value"
done < <(cat arguments.json | jq -r 'to_entries[] | "\(.key) \(.value)"')


# Et voila!
echo $empower_haste
echo $greater_bash
