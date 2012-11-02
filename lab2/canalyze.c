#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "fgetname.h"
#include "namelist.h"
#include <string.h>

// the function return 1 if the given word is a key word and 0 if not.
int is_key_word(char *name){
  
  char *keywords[33] ={
			"auto", "break", "case", "char", "const", "continue", "default", "do",
			"double","else","enum","extern","float","for","goto","if","int","long",
			"register","return","short","signed","sizeof","static","struct","switch",
			"typedef","union","unsigned","void","volatile","while",NULL
  };
  
  
    int i;
    for(i=0; keywords[i] ; i++){
      if ( strcmp(keywords[i],name) ==0 )
	return 1;
    }
    return 0;
}



int struct_cmp_by_name(const void *a, const void *b) 
{ 
    struct names *ia = (struct names *)a;
    struct names *ib = (struct names *)b;
    return strcmp(ia.name, ib.name);
	/* strcmp functions works exactly as expected from
	comparison function */ 
} 





int main(int argc, char **argv) {
	//make a new name list
	namelist nl = make_namelist();
	
	// for each file print all the words
	int i;
	for (i =1; i< argc; i++){
	  FILE *stream = fopen(argv[i], "r");
	
	  char name[64];
	  if(!stream) {
		  fprintf(stderr, "run the test in the source directory\n");
		  return 1;
	  }


	  //for each name in the file, add the name to the namelist
	  while(fgetname(name, sizeof(name), stream)){
		  printf("%s ", name);
		  if(is_key_word(name)==1)
		    add_name(nl, name);
	  }

	  printf("\n");
	  fclose(stream);
	 }
	 
	 int nl_names_size= (sizeof(nl->names)) / sizeof (char*);
	//TODO to complete
	qsort(nl->names, nl_names_size ,sizeof(char *), struct_cmp_by_name);
	
	 for(i = 0; i!=nl->size; i++) {
		if ((nl->names[i].count) ==1) { 
		printf("%s ", nl->names[i].name);
		printf("%d \r\n", nl->names[i].count);
		}
	 }
	
	 
	return 0;
}

	
