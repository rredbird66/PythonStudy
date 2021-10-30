SOURCES = $(shell find . -name "*.py")
P_VER   = python3
all: $(SOURCES)
	$(foreach file, $(SOURCES), $(P_VER) $(file);)
