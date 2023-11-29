#!/usr/bin/env bash
set -e
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export LOCAL_DATA_FILE="$SCRIPT_DIR/local_data.json"
source "$SCRIPT_DIR/../../venv/bin/activate"
source "$SCRIPT_DIR/secrets.sh"
python "$SCRIPT_DIR/main.py"
