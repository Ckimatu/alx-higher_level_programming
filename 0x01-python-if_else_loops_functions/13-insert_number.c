#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the node
 * @number: content to be entered
 * Return: address of the new node
 * NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *n_pointer = *head;

	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (n_pointer->next)
	{
		if ((n_pointer->next)->n >= number)
		{
			new_node->next = n_pointer->next;
			n_pointer->next = new_node;
			return (new_node);
		}
		n_pointer = n_pointer->next;
	}

	new_node->next = NULL;
	n_pointer->next = new_node;

	return (new_node);
}
