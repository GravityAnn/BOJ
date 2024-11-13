#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

//'달디달고'가 n번 반복된 후 '달디단'으로 끝나도록
//매초에 두개의 작업중 하나를 택

//a~z중 원하는 알파벳 하나를 골라 맨뒤에 입력

//지금까지 입력한 문자열의 연속된 부분 문자열을 복사.
//맨뒤에 붙. 연속된 문자열만 복사 사능. 
void func1(int n)
{
	int i = 0;
	int ans = 0;
	while (1)
	{
		//printf("지나갑니다 : %d", i);
		if ((pow(2, i) <= n) && (n < pow(2, i + 1)))
		{
			printf("%d", 10 + i);
			break;
		}
		else
			i++;
	}
}

int main(void)
{
	int n;
	//printf("뭐지??");
	scanf("%d", &n);//'달디달고'의 횟수
	func1(n);
	return 0;
}

//d
//a
//l
//d
//i
//dal
//g
//o : 8
//daldidalgo : 9
//daldida : 10
//n : 11초(2)

//d
//a
//l
//d
//i
//dal
//g
//o : 8
//daldidalgo : 9
//daldidalgodaldida : 10
//n : 11초(3)

//d
//a
//l
//d
//i
//dal
//g
//o : 8
//daldidalgo : 9
//daldidalgodaldidalgo : 10
//daldida : 11
//n : 12초(4)

//d
//a
//l
//d
//i
//dal
//g
//o : 8
//daldidalgo : 9
//daldidalgodaldidalgo : 10
//daldidalgodaldidalgodaldida : 11
//n : 12초

//d
//a
//l
//d
//i
//dal
//g
//o : 8
//daldidalgo : 9
//daldidalgodaldidalgo : 10
//daldidalgodaldidalgodaldidalgodaldida : 11
//n : 12초

//d
//a
//l
//d
//i
//dal
//g
//o : 8
//daldidalgo : 9
//daldidalgodaldidalgo : 10
//daldidalgodaldidalgodaldidalgodaldidalgodaldida : 11
//n : 12초

//n = 2 : 8 + 1 + (1 + 1)초 -> 11초
//n = 3 : 8 + 1 + (1 + 1)초 -> 11초
//n = 4 : 8 + 1 + 1 + (1 + 1)초 -> 12초
//n = 5 : 8 + 1 + 1 + 1 + (1 + 1)초 -> 12초
//n = 6 : 8 + 1 + 1 + 1 + (1 + 1)초 -> 12초
//n = 7 : 8 + 1 + 1 + 1 + (1 + 1)초 -> 12초
//n = 8 : 8 + 1 + 1 + 1 + (1 + 1)초 -> 13초
