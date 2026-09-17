#!/bin/bash

cpu=${1:-2}

bash 1.wget_fragbed.bash
python 2_prepare_site.py
python 3_get_pfTAS.py --cpu $cpu
python 4_draw.py