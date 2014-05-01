
SHELL		= /bin/bash
PY2		= python
PYTESTOPTS	= -v --capture=no
PYTEST		= $(PY2) -m pytest $(PYTESTOPTS)

.PHONY:		clean test test-% unit-%

clean:
	find . -name '*.pyc' -exec rm {} \;
	find . -name '*.packc' -exec rm {} \;

test:		clean
	$(PYTEST)

test-%:		clean
	$(PYTEST) *$**.py

unit-%:		clean
	$(PYTEST) -k $*
