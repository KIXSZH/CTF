#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    char filename[] = ".config.txt"; // Name of the file

    // Open the file for reading
    file = fopen(filename, "r");

    // Check if the file exists
    if (file == NULL) {
        printf("File not found or unable to open.\n");
        return 1;
    }

    // Read the contents of the file character by character
    char *fileContents = NULL;
    int capacity = 0;
    int size = 0;
    int ch;

    while ((ch = fgetc(file)) != EOF) {
        if (size >= capacity) {
            // Double the capacity of the buffer
            capacity = (capacity == 0) ? 1 : capacity * 2;
            fileContents = (char *)realloc(fileContents, capacity * sizeof(char));
        }
        fileContents[size++] = ch;
    }

    // Null-terminate the string
    fileContents = (char *)realloc(fileContents, (size + 1) * sizeof(char));
    fileContents[size] = '\0';

    // Close the file
    fclose(file);

    // Print the contents of the variable
    

    // Free the dynamically allocated memory
    int number; 
    char *flag = fileContents;
   

    printf("Enter THE PASSWORD::: ");
    scanf("%d", &number);
   

    // True if the remainder is 0
    if  (number == 1024) {
        printf("THE FLAG ==\n%s\n", fileContents);
    }
    else {
        printf("Password_is_WRONG_DON'T TRY AGAIN YOU NEVER FIND IT");
    }


    free(fileContents);

    return 0;
}
