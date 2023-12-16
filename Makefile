COMPILER = gcc
CFLAGS = -O3 --shared
LFLAGS = -fPIC

TARGET = core.so

all: $(TARGET)

core.so: core.c
	$(COMPILER) $(CFLAGS) -o $@ $^ $(LFLAGS)

clean:
	rm $(TARGET)

.PHONY: clean all
