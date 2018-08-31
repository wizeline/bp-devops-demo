#!/bin/ash

set -e

# -- app-manager starts ---
source /app-manager-env.sh
# -- app-manager ends ---

python api.py
