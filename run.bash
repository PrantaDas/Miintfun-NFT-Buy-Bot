#!/bin/bash

# Getting the location of the script
echo "=> Getting the location of the script"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to the bot's directory
echo "=> Navigating to the bot's directory"
cd "$DIR"

# Run the Node.js application
echo "=> Checking the dependencies and installing"
pip install -r requirements.txt

# Running the bot.
echo "=> Starting the bot..."
python src/app.py
