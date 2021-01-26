initLin:
	python -m venv venv; \
	. ./venv/bin/activate; \
	pip install -r requirements.txt; \

initWin:
	python -m venv venv &
	# These  v  will have to be run manually on windows
	# .\venv\Scripts\activate
	# pip install -r ./requirements.txt

test:
	pytest

run:
	python converter.py

clean:
	rm -rf venv

.PHONY: init test