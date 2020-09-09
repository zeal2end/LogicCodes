#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct node
{
    int data;
    struct node* next;
}digit;

digit* insert_at_end(int value,digit* head)
{
    digit* temp = (digit*)malloc(sizeof(digit));
    temp->data = value;
    if(head == NULL)
    {
        head = temp;
        temp->next = NULL;
    }
    else
    {
        digit* ptr = head;
        while(ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        ptr->next = temp;
        temp->next = NULL;
    }
    return head;

}
digit* reverse_linked_list(digit* head)
{
    digit* current = head;
    digit* prev = NULL;
    digit* next = NULL;
    while(current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
	return prev;
}
void display(digit* p)
{

    digit *ptr = p;
    while(ptr != NULL)
    {
        printf("%d",ptr->data);
        ptr = ptr->next;
    }
}
digit* n_hash(int num)
{  	digit* head = NULL;
	head = (digit*)malloc(sizeof(digit));
    head->next = NULL;
    head->data = 1;
    digit* ptr = NULL;;
    int temp,carry = 0;
    for(int i = 1;i < num || i == num;i++)
    {
        for(int j = i;j< num || j == num;j++)
        {  
            ptr = head;
            carry = 0;
            while(ptr != NULL)
            {
                temp = j * (ptr->data) + carry;
                if(temp > -1 && temp < 10)
                {
                    ptr->data = temp;
                    carry = 0;
                    ptr = ptr->next;
                }
                else
                {
                    if(ptr == head)
                    {
                        ptr->data = temp%10;
                        if(ptr->next == NULL)
                        {   temp = temp/10;
                             while(temp != 0)
                                {
                                    carry = temp % 10;
                                    head = insert_at_end(carry,head);
                                    temp = temp/10;
                                }
                            ptr = NULL;
                        }
                        else
                        {   
                            carry = temp/10;
                            ptr = ptr->next;
                        }
                    }
                    else
                    {
                        if(ptr->next == NULL)
                        {
                            if(temp > 10 || temp == 10)
                            {
                                ptr->data = temp%10;
                                temp = temp/10;
                                while(temp != 0)
                                {
                                    carry = temp % 10;
                                    head = insert_at_end(carry,head);
                                    temp = temp/10;
                                }
                                ptr = NULL;
                            }
                            else
                            {
                                ptr->data = temp;
                                ptr = ptr->next;
                            }
                        }
                        else
                        {
                            ptr->data = temp% 10;
                            carry = temp/10;
                            ptr = ptr->next;
                        }
                    }
                }
               

            }
           
        }


    }

	return head;
}
int Zero_s(digit* root){
	int a = 0;
	while(root->next!=NULL){
		if(root->data == 0)a++;
		else break;
		root = root->next;
	}
	return a;
}

int len = 0;
int matching(digit* root,digit* match){
	int cnt = 0;
	while(root!=NULL && match!=NULL){
		if(root->data == match->data)cnt++;
		else break;

		root = root->next;
		match = match->next;
	}
	if(cnt == len)return 1;
	else return 0;
}

int Pattern(digit* root, digit* match){
	int cnt = 0;
	while(root!=NULL){
		cnt += matching(root,match);
		root = root->next;
	}

	return cnt;

}


int main(){
	int test_cases = 1;
	scanf("%d",&test_cases);
	for(int tt = 0;tt<test_cases;tt++){

		int num;
		scanf("%d",&num);
		digit* root = n_hash(num);

		int Count_zero = Zero_s(root);
		printf("%d ",Count_zero);
		
		char val[5];
		scanf(" %s",val);
		
		digit* pat = NULL;
		int i = 0;
		while(val[i]!= '\0'){
			len++;
			int r = val[i] - '0';
			pat = insert_at_end(r,pat);
			i++;
		}


		root = reverse_linked_list(root);
		int pattern_count = Pattern(root,pat);
		printf("%d ",pattern_count);
		display(root);
		printf("\n");
		len = 0;

	}

	return 0;

}
