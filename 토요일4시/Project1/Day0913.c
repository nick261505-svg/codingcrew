#include "stdio.h"

const double PI=3.141592;

int b;//전역변수는 자동으로 0으로 초기화 된다.

int main() 
{
	//정의(생성) 와 선언(컴파일러에게 알려주는것)
	//int a=200; //선언

	int a = 10; //지역변수는 반드시 초기화 해야한다.
	
	printf("%d\n", a);
	printf("%d\n", b);//쓰레기값
	printf("%f\n", PI);
	for (int i = 0; i < 10; i++) {
		printf("%d\n", a);
	}

	return 0;
}

