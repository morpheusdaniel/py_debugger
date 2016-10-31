#include <stdio.h>

int main(int argc, char **argv)
{
	FILE *fin = fopen(argv[1], "r");
	char buf[256];
	char buf2[1024];
	
	fgets(buf2, 1024, fin);
	strcpy(buf, buf2);
	
	return 0;
}