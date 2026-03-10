#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>
#include <sys/wait.h>
#include <time.h>

sem_t sem;

void critical_section(const char *name)
{
   for (int i = 0; i < 3; i++)
   {
      sem_wait(&sem);
      printf("[%s] trying to enter critical section (PID=%d)\n", name, getpid());

      printf("[%s] ENTERED critical section (PID=%d)\n", name, getpid());
      sleep(rand() % 3 + 1);
      printf("[%s] EXITING critical section (PID=%d)\n", name, getpid());

      sem_post(&sem);
      sleep(rand() % 3 + 1);
   }
}

int main()
{
   srand(time(NULL));
   sem_init(&sem, 1, 1);

   for (int i = 0; i < 3; i++)
   {
      printf("(pid:%d) \n", (int)getpid());
      pid_t pid = fork();
      if (pid == 0)
      {
         char name[20];
         sprintf(name, "Child-%d", i + 1);
         critical_section(name);
         exit(0);
      }
   }

   for (int i = 0; i < 3; i++)
      wait(NULL);

   sem_destroy(&sem);
   return 0;
}
