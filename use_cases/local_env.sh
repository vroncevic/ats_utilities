#!/usr/bin/env bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)
PARENT_DIR=$(dirname "$SCRIPT_DIR")

export PYTHONPATH="${PARENT_DIR}:${PYTHONPATH}"
echo "PYTHONPATH updated: $PYTHONPATH"
