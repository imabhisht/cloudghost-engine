#!/bin/bash
export STEAMPIPE_DATABASE_PASSWORD=admin
steampipe service start --show-password
# python3 app.py
python3 /app/app.py
