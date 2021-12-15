./scripts/check_styleguide.sh
styleguide=$?
./scripts/check_tests.sh
tests=$?
./scripts/check_coverage.sh
coverage=$?

[ $styleguide -eq 0 ] && echo "Styleguide PASSED" || echo "Styleguide FAILED"
[ $tests -eq 0 ] && echo "Tests PASSED" || echo "Tests FAILED"
[ $coverage -eq 0 ] && echo "Coverage PASSED" || echo "Coverage FAILED"