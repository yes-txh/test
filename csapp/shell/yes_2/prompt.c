#include "prompt.h"

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void print_prompt(){
  char h[HOST_NAME_MAX];
  host(h);

  char *path = cwd();

  printf("Yes:%s@%s:%s$ ", user(), h, path);

  free(path);
}

char *user(){
  return getenv("USER");
}

void host(char *name){
  gethostname(name, HOST_NAME_MAX);
}

char *cwd(){
  char *path = getcwd(NULL, 0);
  char *home_path = home();
  size_t home_len = strlen(home_path);

  if (!strncmp(path, home_path, home_len) ){
    path[0] = '~';

    char *p = path;
    do *(p+1) = *(p+home_len);
    while (*(p++ + home_len) );

    return realloc(path, strlen(path) + 1);
  }
  else
    return path;
}

char *home(){
  return getenv("HOME");
}

