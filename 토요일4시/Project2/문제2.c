#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define LEN_INPUT 1000001

int main() {
	
	//c언어의 배열정보 길이는 변수는 불가
	char a[LEN_INPUT];//지역변수: stack에저장
	
	scanf_s("%s", a, (int)sizeof(a));
	printf("a = %s", a);
	return 0;
}