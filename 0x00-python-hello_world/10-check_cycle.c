#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list input
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *second;
	listint_t *previous_node;

	second = list;
	previous_node = list;
	while (list && second && second->next)
	{
		list = list->next;
		second = second->next->next;

		if (list == second)
		{
			list = previous_node;
			previous_node =  second;
			while (1)
			{
				second = previous_node;
				while (second->next != list && second->next != previous_node)
				{
					second = second->next;
				}
				if (second->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
