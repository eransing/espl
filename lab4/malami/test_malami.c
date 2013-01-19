#include <stdlib.h>
#include <stdio.h>

extern int malami();

int main(int argc, char **argv) {
	int ans = malami(argv[1]);
	printf("the value is: %d\n",ans);
	printf("the value is: %d\n",atoi(argv[1]));
	return 0;
}
