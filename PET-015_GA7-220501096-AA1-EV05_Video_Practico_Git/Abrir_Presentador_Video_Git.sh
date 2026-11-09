#!/bin/bash
# Lanzador de escritorio para el Presentador Interactivo de Git en Linux
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
xdg-open "$DIR/presentador_video_git.html" 2>/dev/null || sensible-browser "$DIR/presentador_video_git.html" 2>/dev/null || firefox "$DIR/presentador_video_git.html" &
