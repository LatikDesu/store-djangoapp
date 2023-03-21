#!/bin/sh
# run a worker :)
celery -A store worker --loglevel=info --concurrency 1 -E
