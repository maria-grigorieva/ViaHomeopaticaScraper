#!/bin/bash
# start Celery workers
nohup /opt/ViaHomeopaticaScraper/venv/vh_py37/bin/celery -A tasks worker -l info -f logs/celery.log > /dev/null 2>&1&
echo "Celery Worker started"

# start Celerybeat
nohup /opt/ViaHomeopaticaScraper/venv/vh_py37/bin/celery -A tasks beat -l info -f logs/celerybeat.log > /dev/null 2>&1&
echo "Celerybeat started"

# start Flower
nohup /opt/ViaHomeopaticaScraper/venv/vh_py37/bin/celery -A tasks flower -l debug -f logs/flower.log > /dev/null 2>&1&
echo "Flower started"