#!/bin/bash

source bin/activate
source config/settings.sh

grunt

python app.py

