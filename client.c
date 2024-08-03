#include <stdio.h> 
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>

void error(const char *msg) {
  perror(msg);
  exit(1);
}

int main(int argc, char* argv[]) {
  if (argc < 3) {
    fprintf(stderr, "Port number or host name not provided\n");
    exit(1);
  }
  // sockfd = file descriptor for the new socket
  int sockfd, portno, n;
  char buffer[255];
  // https://man7.org/linux/man-pages/man3/sockaddr.3type.html
  struct sockaddr_in serv_addr;
  struct hostent* server;
  
  portno = atoi(argv[2]);
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0) 
    error("Error on opening socket");

  server = gethostbyname(argv[1]);
  if (server == NULL) {
    error("No such host");
  }

  
  bzero((char*) &serv_addr, sizeof(serv_addr));
  serv_addr.sin_family = AF_INET;
  bcopy((char*) server->h_addr_list[0], (char*) &serv_addr.sin_addr.s_addr, server->h_length);
  serv_addr.sin_port = htons(portno);
  if (connect(sockfd, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) < 0) {
    error("connection failed");
  }

  while(1) {
    bzero(buffer, 255);
    fgets(buffer, 255, stdin);
    n = write(sockfd, buffer, strlen(buffer));
    if (n < 0) {
      error("error on writing");
    }
    bzero(buffer, 255);
    n = read(sockfd, buffer, 255);
    if (n < 0) {
      error("error on reading");
    }
    printf("Server: %s\n", buffer);
    if (strncmp("Bye", buffer, 3) == 0)
      break;
  }
  close(sockfd);
  return 0;
}