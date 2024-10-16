#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define N 10000

typedef struct Queue
{
	int front, rear;
	int data[N];
}Queue;

void init_queue(Queue* q)
{
	q->front = q->rear = 0;
}

int isEmpty(Queue* q)
{
	return (q->front == q->rear);
}

int isfull(Queue* q)
{
	return (q->front == (q->rear + 1) % N);
}

void push(Queue* q, int e)
{
	q->rear = (q->rear + 1) % N;
	q->data[q->rear] = e;
}

int pop(Queue* q)
{
	if (isEmpty(q) == 1)
		return -1;
	q->front = (q->front +1)%N;
	return (q->data[q->front]);
}

int size(Queue* q)
{
	return (q->rear - q->front + N)%N;
}

int front(Queue* q)
{
	if (isEmpty(q) == 1)
		return -1;
	return (q->data[(q->front+1) % N]);
	return (q->data[(q->front + 1) % N]);
}

int back(Queue* q)
{
	if (isEmpty(q) == 1)
		return -1;
	return (q->data[q->rear]);
}

int main(void)
{
	Queue q;
	
	int n;
	int e;

	init_queue(&q);
	scanf("%d", &n);
	for (int i = 0; i <n; i++)
	{
		char order[10];
		scanf("%s", order);
		
		if (strcmp(order, "push") == 0)
		{
			scanf("%d", &e);
			push(&q, e);
		}
		else if (strcmp(order, "pop") == 0)
		{

			printf("%d\n", pop(&q));
		}
			
		else if (strcmp(order, "front") == 0)
			printf("%d\n", front(&q));
		else if (strcmp(order, "back") == 0)
			printf("%d\n", back(&q));
		else if (strcmp(order, "size")==0)
			printf("%d\n", size(&q));
		else if (strcmp(order, "empty") == 0)
			printf("%d\n", isEmpty(&q));

	}

}