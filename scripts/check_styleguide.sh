flake8 ./sil_framework --config=.flake8
flake=$?
pylint ./sil_framework --rcfile=.pylintrc
pylint=$?

[[ $flake -eq 0 && $pylint -eq 0 ]] && exit 0 || exit 1