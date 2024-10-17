#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define N 50

typedef char Element;

typedef struct Queue {
  int front, rear;
  char data[N];
} Queue;

void init(Queue *q) {
  q->front = q->rear = 0;
}

int isEmpty(Queue *q) {
  return (q->front == q->rear);
}

int isFull(Queue *q) { return (q->front == (q->rear + 1) % N); }

void push(Queue *q, Element e) {
  if (isFull(q))
    return;
  else {
    q->rear = (q->rear + 1) % N;
    q->data[q->rear] = e;
  }
}

Element pop(Queue *q) {
  if (isEmpty(q)) {
    return -1;
  } else {
    q->front = (q->front + 1) % N;
    return q->data[q->front];
  }
}

Element peek(Queue *q) {
  if (isEmpty(q)) {
    return -1;
  } else {
    return q->data[(q->front + 1) % N];
  }
}

int main(void) {
  Queue q;
  int cnt;
  int n;
  char str[N];
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    init(&q);  // 각 테스트마다 큐 초기화
    cnt = 0;
    scanf("%s", str);
    for (int j = 0; str[j] != '\0'; j++) {
      if (str[j] == '(' || str[j] == '[' || str[j] == '{')
        push(&q, str[j]);
      else {
        if (str[j] == ')' && peek(&q) == '(')
          pop(&q);
        else if (str[j] == '}' && peek(&q) == '{')
          pop(&q);
        else if (str[j] == ']' && peek(&q) == '[')
          pop(&q);
        else {
          printf("NO\n");
          cnt++;
          break;
        }
      }
    }

    // 큐에 남은 괄호가 있으면 NO 출력
    if (!isEmpty(&q)) {
      cnt++;
      printf("NO\n");
    }

    if (cnt == 0) {
      printf("YES\n");
    }
  }

  return 0;
}
