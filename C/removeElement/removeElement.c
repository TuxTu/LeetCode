#include <stdio.h>

//8ms,7.1MB
int removeElement(int* nums, int numsSize, int val){
	int i = 0, j = 0;
	int length = numsSize;
	while (j < numsSize) {
		if (nums[j] == val) {
			j++;
			numsSize--;
		}
		else {
			nums[i] = nums[j];
			i++;
			j++;
		}
	}
	return numsSize;
}

//4ms,7.2MB
int removeElement2(int* nums, int numsSize, int val){
	int i = 0;
	while (i < numsSize){
		if (nums[i] == val){
			nums[i] = nums[numsSize - 1];
			numsSize--;
		}
		else {
			i++;
		}
	}
	return numsSize;
}

int main(){
	int a[10] = {3, 2, 2, 3};
	int i = 0;
	printf("The size of the nums is: %d\n", (int)(sizeof(a) / sizeof(a[0])));
	printf("The answer is: %d\n", removeElement2(a, sizeof(a) / sizeof(a[0]), 3));
	while (a[i] != '\0') {
		printf("%d\n", a[i]);
		i++;
	}
	return 0;
}
