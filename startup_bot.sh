#!/bin/bash


cd "$(dirname "$0")"
screen -S chatgpt_vkbot -dm /home/$USER/.local/bin/poetry run python3 main.py