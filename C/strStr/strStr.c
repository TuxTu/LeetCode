#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//4ms,7.3MB
int strStr(char * haystack, char * needle){
    int nLen = strlen(needle), maxIndex = strlen(haystack) - strlen(needle);
    if (nLen == 0) {
        return 0;
    }
    int i = 0;
    char* temp;
    temp = (char*)malloc(sizeof(char) * (nLen + 1));
    while (i <= maxIndex) {
        strncpy(temp, haystack + i, nLen);
        temp[nLen] = '\0';
        if (strcmp(temp, needle) == 0) {
            return i;
        }
        i++;
    }
    return -1;
}
int main(){
	printf("The answer is: %d\n", strStr("a", "a"));
	return 0;
}
