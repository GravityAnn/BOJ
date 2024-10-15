#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define N  1000001

typedef struct Stack
{
	int top;
	int data[N];
}Stack;

void init_stack(Stack* stack)
{
	stack->top = -1;
}

int isEmpty(Stack* stack)
{
	return (stack->top == -1);
}

void push(Stack* stack, int n)
{
	stack->top += 1;
	stack->data[stack->top] = n;
}

int pop(Stack* stack)
{
	if (isEmpty(stack) == 1)
		return -1;
	else
	{
		int pos = stack->data[stack->top];
		stack->top -= 1;
		return pos;
	}
}

int cnt(Stack* stack)
{
	return (stack->top) + 1;
}

int peek(Stack* stack)
{
	if (isEmpty(stack) == 1)
		return -1;
	else
	{
		int pos = stack->data[stack->top];
		return pos;
	}
}

int main()
{
	int n;
	scanf("%d", &n);//명령의 수 입력

	int* a = (int*)malloc(sizeof(int) * n);
	Stack s;
	init_stack(&s);

	for (int i = 0; i < n; i++)
	{
		int func, value;

		scanf("%d", &func);
		if (func == 1)
		{
			scanf("%d", &value);
			push(&s, value);
		}
		else if (func == 2)
			printf("%d\n", pop(&s));
		else if(func == 3)
			printf("%d\n", cnt(&s));
		else if (func == 4)
			printf("%d\n", isEmpty(&s));
		else if (func == 5)
			printf("%d\n", peek(&s));
	}
	return 0;
}