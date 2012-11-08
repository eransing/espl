CC=gcc
CFLAGS=-O -g

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

all: bcmp

bcmp: bcmp.o
	$(CC) $(CFLAGS) -o $@ $^

bcmp.o: bcmp.c

clean:
	rm -f *.o bcmp
