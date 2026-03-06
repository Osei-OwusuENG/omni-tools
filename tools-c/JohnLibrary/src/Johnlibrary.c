#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Johnlibrary.h"

// CODE FOR GETTING KEYBOARD INPUT FUNCTION

// read user input
char *get(void)
{
    char *input = NULL; // Initialize input to NULL
    int c;
    int i = 0;
    while ((c= fgetc(stdin)) != '\n' && c != EOF) // Read until newline or EOF
    {
        char *temp= realloc(input, (i + 2) * sizeof(char)); // Resize buffer for each character
        
        if (temp == NULL) // Check for allocation failure
        {
            free(input); // Free previously allocation memory
            return NULL; // Return NULL on allocation failure
        }
        input = temp; // Update input pointer to the newly allocated memory
        input[i++] = c; // Store the character and increment index
    }

    if (input == NULL) // return null if no input was read
    {
        return NULL;
    }
    
    input[i] = '\0'; // Null-terminate the string
    return input; // Return the user input
}


// I have to improve it to handle errors well or certain conditions
char *get_input(const char *user_input)
{
    // display the user input instructions
    printf("%s", user_input);

    // get the user input and return it to the caller
    char *input = get();
    return input;
}

// MATHS FUNCTIONS CODE

// addition function code
int Add(int i, int j)
    {
        return i + j;
    }

// multiplication function code
int Multiply(int x, int y)
    {
        return x * y;
    }