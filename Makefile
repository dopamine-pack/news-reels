# Makefile

# Variables
PYTHON = python3
SRC_DIR = src
TEST_DIR = tests
VENV_DIR = .venv
VENV_PIP = $(VENV_DIR)/bin/pip
VENV_PYTHON = $(VENV_DIR)/bin/python

# Targets
.PHONY: venv clean test run

run:
	$(VENV_PYTHON) $(SRC_DIR)/main.py

clean:
	# Add commands to clean up generated files or directories
	rm -rf $(VENV_DIR)

test:
	$(VENV_PYTHON) -m unittest discover -s $(TEST_DIR) -p "test_*.py"

venv:
	$(PYTHON) -m venv $(VENV_DIR) && source $(VENV_DIR)/bin/activate
	$(VENV_PIP) install -r requirements.txt
