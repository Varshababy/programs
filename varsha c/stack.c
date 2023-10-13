#include<stdio.h>
#include<stdlib.h>
void push();
void pop();
void peek();
void display();
int top=-1,arr[5];
void main()
{
while(1)
{
int op;
printf("\nStack operation");
printf("\n 1.push");
printf("\n 2.pop");
printf("\n 3.peek");
printf("\n 4.display");
printf("\n 5.exit");
printf("\nSelect your option:  ");
scanf("%d",&op);
switch(op)
{
case 1:push();
break;
case 2:pop();
break;
case 3:peek();
break;
case 4:display();
break;
case 5:exit(0);
break;
default:printf("\n select from 1,2,3,4,5: \n\n");
}
}
}
void push()
{
int n;
if(top>=4)
{
printf(" stack overflow");
}
else
{
printf("\n enter element to be pushed :");
scanf("%d",&n);
top=top+1;
arr[top]=n;
printf("%d added to stack. \n\n",n);
}
}
void pop()
{
if(top==-1)
{
printf("\n stack underflow.\n");
}
else
{
printf("\n%d popped.\n",arr[top]);
top=top-1;
}
}
void peek()
{
if(top==-1)
{
printf("\n no element in stack\n");
}
else
{
printf("\n top element is %d.\n",arr[top]);
}
}
void display()
{
if(top==-1)
{
printf("\n no of elements in stack \n");
}
else
{
printf("\n elements in stack:\n");
for(int i=top;i>=0;--i)
printf("%d\n",arr[i]);
}
}


