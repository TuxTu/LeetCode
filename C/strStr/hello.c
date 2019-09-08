#include <stdio.h>
#include <string.h>

int main(){
	char* s;
	char a[4];
	int length;
	s = "abcdefg";
	strncpy(a, s + 1, 3);
	strncpy(a, s + 2, 3);
	if (strcmp(a, "bcd") == 0){
		printf("hello,world!\n");
	}
	length = sizeof(a) / sizeof(a[0]);
	printf("%s, %d\n", a, length);
	return 0;
}
