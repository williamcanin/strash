PREFIX = /usr/local
BASEDIR = .

uninstall:
	@rm -f $(PREFIX)/bin/strash
	@rm -rf $(PREFIX)/share/strash

install: uninstall
	@mkdir $(PREFIX)/share/strash
	@cp -p $(BASEDIR)/strash/strash.py $(PREFIX)/share/strash
	@ln -s $(PREFIX)/share/strash/strash.py $(PREFIX)/bin/strash

.PHONY: install uninstall
