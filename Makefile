init: buildenv startenv

buildenv:
	python3 -m venv venv 

startenv:
	. ./venv/bin/activate; \
	pip3 install -r requirements.txt; \

test:
	pytest

run:
	python3 converter.py

clean:
	rm -rf venv

.PHONY: init test