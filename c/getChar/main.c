#include <stdio.h>
#include <stdlib.h>
#define TAMANHO 10

int palavra[TAMANHO];
int count = 0;

int main () {
	while ( count < TAMANHO ) {
		char name;
		name = getchar();
		if ( name == '\n' ) {
			break;
		}
		else {
			palavra[count] = name;
		}
		count++;
	}
	count = 0;
	puts ("\nYour name is ");
	while ( count < TAMANHO ) {
		char name = palavra[count];
		printf("%c", name);
		count++;
	}
	puts ("\n");
	exit(EXIT_SUCCESS);
}
