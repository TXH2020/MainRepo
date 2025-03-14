#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
int val;
if (argc != 2)
printf("usage: a.out <descriptor#>");
if ((val = fcntl(atoi(argv[1]), F_GETFL, 0)) < 0)
printf("fcntl error for fd %d", atoi(argv[1]));
switch (val & O_ACCMODE) {
case O_RDONLY:
printf("read only");
break;
case O_WRONLY:
printf("write only");
break;
case O_RDWR:
printf("read write");
break;
default:
printf("unknown access mode");
}
if (val & O_APPEND)
printf(", append");
if (val & O_NONBLOCK)
printf(", nonblocking");
if (val & O_SYNC)
printf(", synchronous writes");
#if !defined(_POSIX_C_SOURCE) && defined(O_FSYNC) && (O_FSYNC != O_SYNC)
if (val & O_FSYNC)
printf(", synchronous writes");
#endif
printf("\n");
exit(0);
}
