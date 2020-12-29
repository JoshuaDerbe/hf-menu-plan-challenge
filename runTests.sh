#!/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color
echo -e "${RED}Please make sure you have pytest and newman installed first!${NC}"
echo "Running tests..."
echo "----------------"

echo "Running Pytest unit tests..."
cd backend
python3 -m pytest

echo "Running Newman E2E tests..."
newman run tests/postman/hf_menu_plan.postman_collection.json

echo "Testing done!"