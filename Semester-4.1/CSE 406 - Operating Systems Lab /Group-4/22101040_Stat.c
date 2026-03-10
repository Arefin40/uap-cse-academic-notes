#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>
#include <errno.h>

void print_file_type(mode_t mode)
{
   if (S_ISREG(mode))
      printf("Regular file\n");
   else if (S_ISDIR(mode))
      printf("Directory\n");
   else if (S_ISLNK(mode))
      printf("Symbolic link\n");
   else if (S_ISCHR(mode))
      printf("Character device\n");
   else if (S_ISBLK(mode))
      printf("Block device\n");
   else if (S_ISFIFO(mode))
      printf("FIFO (named pipe)\n");
   else if (S_ISSOCK(mode))
      printf("Socket\n");
   else
      printf("Unknown\n");
}

int main(void)
{
   const char *filename = "text.txt";
   struct stat file_stat;

   if (stat(filename, &file_stat) == -1)
   {
      perror("stat");
      return 1;
   }

   printf("File: %s\n", filename);
   printf("--------------------------------------\n");

   // File Type
   printf("File Type: ");
   print_file_type(file_stat.st_mode);

   // Permissions
   printf("Permissions (octal): %o\n", file_stat.st_mode & 0777);

   // Ownership
   struct passwd *pw = getpwuid(file_stat.st_uid);
   struct group *gr = getgrgid(file_stat.st_gid);
   if (pw)
      printf("Owner: %s (UID: %u)\n", pw->pw_name, file_stat.st_uid);
   if (gr)
      printf("Group: %s (GID: %u)\n", gr->gr_name, file_stat.st_gid);

   // Hard Links
   printf("Number of links: %lu\n", (unsigned long)file_stat.st_nlink);

   // Device and Inode info
   printf("Device ID: %lu\n", (unsigned long)file_stat.st_dev);
   printf("Inode Number: %lu\n", (unsigned long)file_stat.st_ino);

   // Size Information
   printf("Size: %ld bytes\n", (long)file_stat.st_size);
   printf("Preferred block size for I/O: %ld bytes\n", (long)file_stat.st_blksize);
   printf("Blocks allocated: %ld\n", (long)file_stat.st_blocks);

   // Timestamps
   printf("Last accessed: %s", ctime(&file_stat.st_atime));
   printf("Last modified: %s", ctime(&file_stat.st_mtime));
   printf("Last status change: %s", ctime(&file_stat.st_ctime));

   return 0;
}