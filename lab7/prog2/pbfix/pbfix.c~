#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "diff.h"



void fixChange( char *diffLine, struct diff theDiff, FILE *toPrint, char* flgs){
     // get difference (per line) 

      parsediff(diffLine, &theDiff);
      
      
      // read bytes from file (stream) - 4 bytes per iteration, and XOR it with results (accumelator)
      fseek(toPrint,theDiff.offset, SEEK_SET);
      
      // in case no reverse
      
      if ( (strchr(flgs, 'r')) == 0 ) {
	if ( (char)getc(toPrint) == theDiff.old ) {
	  fseek(toPrint,theDiff.offset,SEEK_SET);
	  fwrite(&theDiff.new,1,1,toPrint);
	  if (strchr(flgs, 'm')) {printf("A change was applied: %s\n",diffLine);}
	}	
      }
      
      // in case reverse was needed
      
      else{
	if ( (char)getc(toPrint) == theDiff.new ) {
	  fseek(toPrint,theDiff.offset,SEEK_SET);
	  fwrite(&theDiff.old,1,1,toPrint);
	  if (strchr(flgs, 'm')) {printf("A change was applied (reverse): %s\n",diffLine);}
	}	
      }
       
      fclose(toPrint);
}



int main(int argc, char *argv[ ]) {
  
   //recieving all arguments (options and/or input files)
   int c;
   int Nproc = 0;
   FILE *toPrint; //input file: original file to fix
   FILE *difference; //input file: differences file, as recieved by bcmp.c
   char *flgs = 'e';
   while ((c = getopt(argc, argv, "hrmp:")) != -1) {  
     switch(c) {
        case 'h':
	  printf("\r\n=====options summery:======\r\n");
	  printf("-h print a summary of options and exit\r\n");
	  printf("-r reverse the differences\r\n");
	  printf("-m print a message each time a change is applied\r\n");
	  printf("-p NPROC maximum number of child processes\r\n");
	  printf("====================\r\n");
	  return 0;
        case 'r':
	  strcat(flgs,'r');
          break;
	case 'm':
	strcat(flgs,'m');
          break;
        case 'p':
	  strcat(flgs,'p');
	  Nproc = optind;
          break;
	}
    }
    
    // parsing input file into tokens (newLine delimeter)
   char diffLine[300];
   
   difference = fopen(argv[optind+1], "r");
   struct diff theDiff;
   
   // open input file again
   toPrint = fopen(argv[optind], "rb+");
	 
   while(fgets(diffLine,sizeof(diffLine),difference) != NULL){      
    fixChange( diffLine,theDiff, toPrint,flgs);

    }
    
    //while the forks are running wait..
  
    
     fclose(difference);
     return 0;
      
   }