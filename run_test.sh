#!/bin/bash

# Baccarat Simulator - Test runner
# Usage: ./run_test.sh
#
# Purpose: test files stores in Test dir, which the best way is to run the test with bash and in current dir
#

echo "Running Baccarat tests..."
echo "========================="

# Run pytest with verbose output
python3 -m pytest test/test_rules.py -v --tb=short

# Check the exit code
if [ $? -eq 0 ]; then
  echo ""
  echo "All tests passed!"
else
  echo ""
  echo "Some tests failed."
  exit 1
fi
