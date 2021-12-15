pytest --cov=./sil_framework/ --cov-fail-under=100 ./
coverage=$?

[ $coverage -eq 0 ] && exit 0 || exit 1