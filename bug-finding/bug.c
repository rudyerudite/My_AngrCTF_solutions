#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

/*void print_good()
{
	printf("Great!\n");
}*/

int main(int argc, char const *argv[])
{
	char buf[8];
	printf("Enter password:\n");
	for(int i=0; i<8;i++)
		buf[i] = getchar();
	printf("Try again!\n");
	return 0;
}
