#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


int main () { 
	int z = 4;
	while ( z < 10000 ) {
		int d = 2;
		bool isPair = false;
		while ( d < z ) {
			if ( z%d == 0 ) {
				isPair = true;
			}
			d++;
		}	
		if ( isPair != true ) {
			printf(" %d", z);
		}
		z++;
	}
	exit(EXIT_SUCCESS);
}
