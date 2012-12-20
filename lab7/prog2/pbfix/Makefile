CC=gcc
CFLAGS=-O -g

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

all: bcmp pbfix diff

bcmp: bcmp.o
	$(CC) $(CFLAGS) -o $@ $^

pbfix: pbfix.o diff.o
	$(CC) $(CFLAGS) -o $@ $^

diff: diff.o
	
bcmp.o: bcmp.c
pbfix.o: pbfix.c diff.h
diff.o: diff.c diff.h

clean:
	rm -f *.o bcmp pbfix diff
