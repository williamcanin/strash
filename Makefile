PREFIX = /usr/local
BASEDIR = .

uninstall:
	@rm -f $(PREFIX)/bin/strash
	@rm -rf $(PREFIX)/share/strash

install: uninstall
	@cp -rp $(BASEDIR)/strash $(PREFIX)/share
	@ln -s $(PREFIX)/share/strash/strash.py $(PREFIX)/bin/strash

.PHONY: install uninstall
