#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//카드게임중 코딩을 하는 사이에 게임실력이 증가
// 게임 기록을 삭제할 수 없어서 증명 불가
//횟수와 이긴 게임, 승률이 정해졌을대 몇번 더 해야 
//확률이 변하는지 출력

unsigned long long win(unsigned long long x, unsigned long long y)
{
	return ((unsigned long long)y * 100) / x;
}

void func(unsigned long long x, unsigned long long y)
{
	unsigned long long c = win(x, y);
	unsigned long long start = 0;
	unsigned long long end = 1000000000-1;
	//printf("입장\n");
	if (c >= 99 || c == 100 || c == 101) {
		//printf("등장\n");
		end = start-1;
		printf("%d", -1);
		return;
	}
	//printf("???");

	while (start <= end)
	{
		//printf("?????");

		unsigned long long mid = (start + end) / 2;
		unsigned long long nx = x + mid;
		unsigned long long ny = y + mid;
		if ((c == win(nx, ny)) && (c < win(nx+1, ny+1)))
		{
			//printf("%d %d는 서로 같다 그때 mid : %d\n", c, win(nx, ny), mid);
			//이제 찾아보자. 
			printf("%llu", mid + 1);
			return;
		}
		else//서로 달라 진다면 당연한 것
		{
			if (c < win(nx, ny))//확률이 너무 올라갔다면
				end = mid - 1;
			else
				start = mid + 1;
		}

		//if (c + 1 == win(nx, ny))
		//	var1 = mid;
		//printf("start : %d, mid : %d, end : %d, win : %d\n", start, mid, end, win(nx, ny));
	}
	return;
}

long long func2(long x, long y)
{
	long long ans = -1;
	long long z = y * 100 / x + 1;
	if (z == 100 || z == 101) {
		printf("-1");
		return 0;
	}
	long long l = 1, r = 1000000000;
	while (l <= r) {
		long long mid = (l + r) / 2;
		long long val = (y + mid) * 100 / (x + mid);
		if (z <= val) r = mid - 1, ans = mid;
		else l = mid + 1;
	}
	return ans;
}


unsigned long long main(void)
{
	unsigned long long x, y, ans;
	unsigned long long i, j;
	scanf("%llu %llu", &x, &y);
	//x의 범위 1 ~ 1,000,000,000
	//x = 99000000;
	//y = 0;
	func(x, y);
	//for (i = 1; i <= 1000; i++) {
	//	for (j = 0; j <= i; j++) {
	//		printf("Testing i=%llu, j=%llu\n", i, j);  // 함수 호출 전 출력
	//		printf("%llu %llu\n", func(i, j), func2(i, j));
	//		if (func(i, j) != func2(i, j)) {
	//			return -1;
	//		}
	//	}
	//}

	//ans = func(x, y);
	//if (ans != 0)
	//	printf("%llu\n", func(x, y));
	//else
	//	printf("%d", type(ans));
	//printf("%llu\n",win(x, y));
	


	


	return 0;
}
