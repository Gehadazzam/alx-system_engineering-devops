#include <sys/types.h>
#include <stdio.h>
#include "unistd.h"
/**
*infinite_while - infiniteloop
*Return: 0 or 1
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
*main - entry main
*Return: always 0
*/
int main(void)
{
pid_t proc_id;
int count = 1;
	while (count <= 5)
{
		proc_id = fork();
		if (!proc_id)
			return (0);
		printf("Zombie process created, proc_id: %d\n", proc_id);
		count++;
}
	infinite_while();
	return (0);
}
