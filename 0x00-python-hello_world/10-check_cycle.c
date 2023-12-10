#include "lists.h"

/**
 * check_cycle - check the list if it is cyclic or not
 * @list: the header of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp != NULL)
	{
		tmp = tmp->next;
		if (tmp == list)
			return (1);
	}
	return (0);
}
