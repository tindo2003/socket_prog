#include <stdio.h> 
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void error(const char *msg) {
  perror(msg);
  exit(1);
}

int main(int argc, char* argv[]) {
  if (argc < 2) {
    fprintf(stderr, "Port number not provided\n");
    exit(1);
  }
  // sockfd = file descriptor for the new socket
  int sockfd, newsockfd, portno, n;
  char buffer[255];
  // https://man7.org/linux/man-pages/man3/sockaddr.3type.html
  struct sockaddr_in serv_addr, cli_addr;
  socklen_t clilen; 

  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0) 
    error("Error on opening socket");
  
  bzero((char* ) &serv_addr, sizeof(serv_addr));
  portno = atoi(argv[1]);

  serv_addr.sin_family = AF_INET;
  serv_addr.sin_port = INADDR_ANY;
  serv_addr.sin_port = htons(portno);

  if (bind(sockfd, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) < 0) 
    error("binding failed");
  

  listen(sockfd, 5);
  clilen = sizeof(cli_addr);

  newsockfd = accept(sockfd, (struct sockaddr*) &cli_addr, &clilen);

  if (newsockfd < 0) 
    error("Error on accept");
  

  while (1) {
    // clear the buffer
    bzero(buffer, 255);
    n = read(newsockfd, buffer, 255);
    if (n < 0) 
      error("Error on read");
    printf("Client: %s\n", buffer);
    bzero(buffer, 255);
    // read from the terminal
    fgets(buffer, 255, stdin);
    n = write(newsockfd, buffer, strlen(buffer));
    if (n < 0)
      error("Error on write");
    int i = strcmp("Bye", buffer);
    if (i == 0) 
      break;
  }
  close(newsockfd);
  close(sockfd);
  return 0;
}
