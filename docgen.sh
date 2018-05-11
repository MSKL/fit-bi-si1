#!/usr/bin/env bash
# This file is used to regenerate the sphinx autodoc

rm -r sphinx/*
sphinx-apidoc -F -A "Matyáš Skalický" -H "SpravujKlub" -f -M -o sphinx spravujklub
echo " " >> sphinx/conf.py
echo "import os" >> sphinx/conf.py
echo "import sys" >> sphinx/conf.py
echo "sys.path.insert(0, '/Users/matya/fit-bi-si1')" >> sphinx/conf.py
echo "sys.path.insert(0, '/Users/matya/fit-bi-si1/spravujklub')" >> sphinx/conf.py

