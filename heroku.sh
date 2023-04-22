#!/bin/bash
gunicorn app:app --daemon
python run.py
