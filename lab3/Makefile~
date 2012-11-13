CC=gcc
CFLAGS=-O -g

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

<<<<<<< HEAD
all: xsum

xsum: xsum.o
	$(CC) $(CFLAGS) -o $@ $^

xsum.o: xsum.c

clean:
	rm -f *.o xsum
=======
all: bcmp bfix diff

bcmp: bcmp.o
	$(CC) $(CFLAGS) -o $@ $^

bfix: bfix.o diff.o
	$(CC) $(CFLAGS) -o $@ $^

diff: diff.o
	
bcmp.o: bcmp.c
bfix.o: bfix.c diff.h
diff.o: diff.c diff.h

clean:
	rm -f *.o bcmp bfix diff
>>>>>>> 42bb9cecaa42862eeca97dbd6166f84188441444
