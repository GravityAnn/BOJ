#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define N 101;

//n개의 레벨이 있고, 클리어할 때마다 점수
//점수들의 합으로 온라인 순위
//레벨을 난이도 순으로 배치
//실수로 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우 발생
//해결책 : 특정 레벨의 점수를 감소시키려
//각 레벨을 클리어할 때 주는 점수를 증가하게 만드려고

//각 레벨을 클리어할 때 얻는 점수가 주어졌을때 몇번 감소하면
//그중에서 최소한으로

void ans(int a[], int n)
{
	int count = 0;
	for (int i = n - 1; i >= 1; i--)
	{
		//printf("[%d] ,[%d]\n", a[i], a[i-1]);
		if (a[i] <= a[i - 1])
		{
			//printf("????");
			count += a[i - 1] - a[i] + 1;
			//printf("( %d, %d) = %d", a[i], a[i - 1], count);
			a[i - 1] = a[i] - 1;
		}
	}
	printf("%d", count);
}

int main(void)
{
	int n, x;
	scanf("%d", &n);
	int a[100] = { 0 };//점수는 항상 양수

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &x);
		a[i] = x;
	}	

	ans(a, n);

	return 0;
}

//5->2(3)
//3
//7->4(3)
//5