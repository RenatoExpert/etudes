#include <stdio.h>

void teste () {
	long int tool = 1;
	int much = 0;
	while (tool <= 999999999) {
		much++;
		tool *= 10;
		printf("Count %d, tool= %ld \n", much, tool);
	}
	printf("Result:%d \n",much);
}	

void main () {
	teste();
}
