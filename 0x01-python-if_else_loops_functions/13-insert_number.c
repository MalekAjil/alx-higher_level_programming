#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node
 * @head: the pointer to the list head
 * @number: the number
 * Return: the pointer to inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp = *head;

	node = malloc(sizeof(listint_t));
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
		*head = node;
	else if (number < tmp->n)
	{
		*head = node;
		node->next = tmp;
	}
	else
	{
		while (tmp->next != NULL && tmp->next->n < number)
			tmp = tmp->next;
		if (tmp->next == NULL)
			tmp->next = node;
		else
		{
			node->next = tmp->next;
			tmp->next = node;
		}
	}
	return (node);
}
