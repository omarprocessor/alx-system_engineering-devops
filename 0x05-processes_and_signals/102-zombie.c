#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid == 0) // Child process
        {
            // Child exits immediately to create a zombie
            exit(0);
        }
        else if (pid > 0) // Parent process
        {
            printf("Zombie process created, PID: %d\n", pid);
        }
        else // Fork failed
        {
            perror("Fork failed");
            return (1);
        }
    }
    infinite_while(); // Keep the parent alive
    return (0);
}
