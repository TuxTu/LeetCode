#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int strStr(char * haystack, char * needle){
	int nLen = strlen(needle), maxIndex = strlen(haystack) - strlen(needle);
	int i = 0;
	char* temp;
	temp = (char*)malloc(sizeof(char) * (nLen + 1));
	while (i <= maxIndex) {
		strncpy(temp, haystack + i, nLen);
		printf("%s\n", temp);
		if (strcmp(temp, needle) == 0) {
			return i;
		} 
		i++;
	}
	return -1;
}

int main(){
	printf("The answer is: %d\n", strStr("hello", "ll"));
	return 0;
}
