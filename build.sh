#!/bin/bash
pandoc --slide-level 2 --template=custom.beamer --toc -t beamer RL.md -o RL.pdf
pdfnup RL.pdf --nup 2x3 --no-landscape --keepinfo --paper A4 --frame true --scale 0.9 --suffix "nup"