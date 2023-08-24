#!/bin/bash
# export STEAMPIPE_DATABASE_PASSWORD=admin
# export STEAMPIPE_INTROSPECTION=info
# steampipe service start --show-password
# steampipe service stop
steampipe service start --show-password
python3 /app/app.py
# steampipe service start --foreground --show-password

# while true; do
#     sleep 10
# done