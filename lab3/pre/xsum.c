#include <unistd.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char **argv) {
    int c;
    int xhflag =1; //1 - if hex (x), 2 - if dec
    char *file;
    
    extern char *optarg;
    
    while ((c = getopt(argc, argv, "hx:")) != -1) {
        switch(c) {
	  case 'h':
	    printf("OPTIONS:\r\n");
	    printf("[default] print the checksum as a decimal number.\r\n");
	    printf("[-x]  print the checksum as a hexadecimal rather than decimal number.\r\n");
	    return 0;
	  case 'x':
	    xhflag = 2;
	    break;
	  default:
	    break;
	}
    }
    
    
    unsigned int word;
    unsigned int cksum = 0;
    
    FILE *stream =fopen(argv[xhflag], "r");
    
    // read bytes from file (stream) - 4 bytes per iteration, and XOR it with results (accumelator)
    while(fread(&word, sizeof(word), 1, stream)) {
      cksum = cksum ^ word;
    }
   
   if (xhflag == 2) {printf("%x\r\n",cksum);}
   if (xhflag == 1) {printf("%d\r\n",cksum);}
    
   fclose(stream);
   return 0;
   
}
