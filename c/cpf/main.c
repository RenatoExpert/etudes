#include <stdio.h>

char stylize (int hey) {
	//char prod[9];
	//sprintf(prod, "%d", hey);
	//char hou = atoi(prod);
	return hey;
}
	
int digitos () {
	return 0;
}

void gerador () {
	printf("Gerador de CPFs \n");
	int cpf[9];
	int count = 0;
	int virgo = 0;
	if (virgo == 0) {
		for (int e = 0; e < 9; e++) {
			cpf[e] = 0;
		}
		virgo = 1;
	}
	for (int o = 0; o <= 1; o++) {
	for (int p = 0; p <= 9; p++) {
			for (int q = 0; q <= 9; q++) {
				for (int r = 0; r <= 9; r++) {
	for (int s = 0; s <= 1; s++) {
			for (int t = 0; t <= 9; t++) {
				for (int u = 0; u <= 9; u++) {
	for (int v = 0; v <= 1; v++) {
			for (int w = 0; w <= 9; w++) {
				for (int x = 0; x <= 9; x++) {
					printf("CPF:");
					for (int y = 0; y < 9; y++) {
						int * ponto = &cpf[y];
						if (*ponto > 9) {
							*ponto = 0;
						}
						printf("%d",*ponto);
						count++;
						(*ponto)++;
					}
					printf(" Count: %d\n",count);
				}
				cpf[w]++;
				printf("\n");
			}
		cpf[v]++;
	}

			cpf[u]++;
			}
		cpf[t]++;
		}
	cpf[s]++;
	}
			cpf[r]++;
			}
		cpf[q]++;
		}
	cpf[p]++;
	}
	cpf[o]++;
	}
	printf("Count: %d\n",count);
}
int main () {
	gerador();
	return 1;
}
