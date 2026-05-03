CC = gcc
CFLAGS = -lm
TARGET = signal
PYTHON = python3

all: run

$(TARGET): signal.c
	$(CC) signal.c -o $(TARGET) $(CFLAGS)

run: $(TARGET)
	$(PYTHON) plot.py

clean:
	rm -f $(TARGET)