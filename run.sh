#!/bin/bash

gunicorn --workers=2 --threads=10 --timeout=120 --bind 0.0.0.0:9999 wsgi:app