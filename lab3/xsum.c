#include <unistd.h>
#include <string.h>
#include <stdio.h>

int
main(int argc, char *argv[ ]) {
    int c;
    int xflg=0;
    int hflg;
    char *xfile;
    extern char *optarg;
    //extern int optind, optopt;
    
    while ((c = getopt(argc, argv, ":hx:")) != -1) {
        switch(c) {
        case 'h':
	printf("\r\noptions summery:\r\n");
	printf("\r\n-h  print a summary of options and exit\r\n");
	printf("\r\n-x  print the checksum as a hexadecimal rather than decimal number.\r\n");
            break;
        case 'x':
	  xflg++;
	  printf("\r\nx option\r\n");
           xfile = optarg;
	   printf("\r\n%s\r\n", xfile);
            break;
        }
    }
    if(xflg !=1){
    xfile = argv[1];
    }
    unsigned int f_word =0000;
    unsigned int word;
    unsigned int result =0000;
    FILE *fp;
    fp=fopen(xfile, "r");
    
    while(fread(&word, sizeof(word), 1, fp)) {
	result = f_word ^ word;
	f_word = word;
	printf("%d\r\n", word); 
	}
	
	if(xflg ==1){
    printf("*************\r\n");
    printf("the hexa result is: %x \r\n", result);
    
    }else{
         printf("*************\r\n");
    printf("the  deca result is: %d \r\n", result); 
    }
    
    fclose(fp);
	
	
	
	
    
}





