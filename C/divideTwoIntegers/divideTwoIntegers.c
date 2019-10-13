#include <stdio.h>
#include <stdlib.h>

#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)

#4ms, 6.7MB
int divide(int dividend, int divisor){
    int sign = (dividend > 0) == (divisor > 0);
    int result = 0;
    
    if (dividend == divisor) return 1;
    if (divisor == INT_MIN) return 0;
    
    int flag = dividend == INT_MIN;
    if (flag) dividend += abs(divisor);
    
    dividend = abs(dividend);
    divisor = abs(divisor);
    
    for (int i = 31; i >= 0; i--){
        if ((dividend >> i) >= divisor){
            result += 1 << i;
            dividend -= divisor << i;
        }
    }
    
    if (flag) return sign ? (result == INT_MAX ? result : result + 1) : -result - 1;
    
    return sign ? result : -result;
}

int main(){
	int dividend, divisor;
	printf("Please input dividend and divisor:");
	while(1){
		if (scanf("%d %d", &dividend, &divisor) != 2 || divisor == 0){
			printf("Illegal input!Please input again!\n");
			printf("Please input dividend and divisor:");
			fflush(stdin);
			continue;
		}
		break;
	}

	printf("The answer is:%d.\n", divide(dividend, divisor));

	return 0;
}
