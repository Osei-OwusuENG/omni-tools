#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Johnlibrary.h"

int Record(char *book);
int main(int argc, char *argv[])
{
        char *names[10];
        names[0] = "kofi is going to school";
        names[1] = "john is going to school";
        names[2] = "jane is going to school";
        names[3] = "james is going to school";
        names[4] = "jennifer is going to school";
        names[5] = "joseph is going to school";
        names[6] = "julie is going to school";
        names[7] = "jason is going to school";
        names[8] = "jessica is going to school";
        names[9] = "jacob is going to school";

        printf("%p\n", &names[0][0]); // Print the first character of the first name
        printf("%p\n", &names[0][1]); // Print the second character of the first name
        printf("%p\n", &names[1][0]); // Print the first character of the second name
        printf("%p\n", &names[1][1]); // Print the second character of the second name
        printf("%p\n", &names[2][0]); // Print the first character of the third name
        printf("%p\n", &names[3][0]); // Print the first character of the fourth name
        printf("%p\n", &names[4][0]); // Print the first character of the fifth name
        printf("%p\n", &names[5][0]); // Print the first character of the sixth name
        printf("%p\n", &names[6][0]); // Print the first character of the seventh name
        printf("%p\n", &names[7][0]); // Print the first character of the eighth name
        printf("%p\n", &names[8][0]); // Print the first character of the ninth name
        printf("%p\n", &names[9][0]); // Print the first character of the tenth name

        char *Alpha = NULL;
        
        for (int i = 0; i <10; i++)
        {
            char *temp = realloc(Alpha, (i + 2) * sizeof(char));
            if (temp == NULL)
            {
                free(Alpha);
                return 1;
            }

            Alpha = temp;
            Alpha[i] = 'a' + i;
            Alpha[i + 1] = '\0';
            printf("%s, memory size: %d bytes\n", Alpha, i + 1);
        }
        
       
        char *user_input = get_input("Tu ere nino?: ");

        if (user_input != NULL)
        {
            printf("Buanches nada, %s\n", user_input);
            free(user_input);
        }
        free(Alpha);

        if (argc <2)
        {
            printf("Usage: ./program <filename>\n");
            return 1;
        }

        int noted = Record(argv[1]);
        
        if (noted != 0)
        {
            return 1;
        }

        printf(" Note Successfully taken\n");

        return 0;
}

int Record(char *book)
{
    char *title = get_input("Content Title: ");
    char *note = get_input("Note: ");

    if (book == NULL) return 1;

    FILE *file = fopen(book, "a");

    if (file == NULL)
    {
        free(title); free(note);
        return 1;
    }

    fprintf(file, "%s: %s\n", title, note);

    fclose(file);
    free(title);
    free(note);

    return 0;
}

