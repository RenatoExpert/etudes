//	Simple output of alphabet
#include <stdio.h>
#include <stdlib.h>

char letter = 'A';

void main () {
	puts("C N");
	while ( letter <= 'z' ) {
		printf ("%c %d\n", letter, letter);
 		letter++;
	}
	puts("");
	exit(EXIT_SUCCESS);
}	
