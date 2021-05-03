#!/bin/bash
set -euo pipefail

current_dir=$(pwd)
docker run --rm -it -v "$current_dir:/app" clang_codegen "$@"
