#!/bin/bash

# Reads the arguments into a JSON file as specified by `barathrum.py`
python barathrum.py "$@" > arguments.json

# Initialize the arguments according.
dagger=$(cat arguments.json | jq '.["dagger"]')
greater_bash=$(cat arguments.json | jq '.["greater_bash"]')

# Et voila! 
echo $dagger
echo $greater_bash
