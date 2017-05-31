#!/bin/bash

echo Se tomará una fotografía.
sleep 2s
fswebcam --no-banner foto.png
echo Fotografía tomada.
sleep 1s
echo Ahora se procesará la fotografía tomada, por favor espere.
sleep 2s
python Main.py
