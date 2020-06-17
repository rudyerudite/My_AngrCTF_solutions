#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>


char buf[] = "password";
char passwd[8];

int main(int argc, char const *argv[])
{
	//overflow passwd to overwrite array buf with "commands" so as to get it verified
	printf("Enter password:\n");
	gets(passwd);

	if(buf == "commands")
		printf("Well done!\n");
	else
		printf("Try again!\n");
	return 0;
}
