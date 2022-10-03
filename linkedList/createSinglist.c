#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};
typedef struct Node node;

void insert(node **head, int value);
void display(node **head);
int delf(node **head);
int dell(node **start);

int main()
{
    node *head;
    head = NULL;
    int last;

    putchar(10);
    insert(&head, 2003);
    insert(&head, 74);
    insert(&head, 3);
    printf("%d\n\n", delf(&head));
    insert(&head, 2);
    display(&head);
    last = dell(&head);
    printf("\n\n%d\n\n", last);
    display(&head);


    return (0);
}
int dell(node **start)
{
    node *temp, *prev;
    temp = *start;
    while(temp->next)
    {
        prev = temp;
        temp = temp->next;
    }
    prev->next = NULL;
    return (temp->data);
    free(temp);

}
int delf(node **head)
{
    node *temp;
    temp = *head;
    if (temp)
    {
        *head = temp->next;
        return (temp->data);
    }
    else
        printf("list is empyt");
}

void insert(node **head, int value)
{
    node *new, *temp;
    temp = *head;
    new = malloc(sizeof(node));
    new->data = value;
    new->next = NULL;

    if (new)
    {
        if (temp == NULL)
        {
            *head = new;
        }
        else
        {
            while (temp->next)
            {
                temp = temp->next;
            }
            temp->next = new;
        }
    }
    else
        printf("failed to allocate memory");
}

void display(node **head)
{
    node *temp;
    temp = *head;
    if (*head == NULL)
    {
        printf("list is empty");
    }
    else
    {
        while (temp)
        {
            printf("%d\n", temp->data);
            temp = temp->next;
        }
    }
}