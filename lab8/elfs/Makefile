CC=gcc
CFLAGS=-O -g -m32

all: encbc decbc

decbc: secret-elf-a secret-elf-c
	$(CC) $(CFLAGS) -o $@ $^

encbc: secret-elf-b secret-elf-c
	$(CC) $(CFLAGS) -o $@ $^
	
clean:
	rm -f encbc decbc

