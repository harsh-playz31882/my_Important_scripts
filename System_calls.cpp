#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/wait.h> 


using namespace std;

int main() {
    /* TASK 2
    int fd = open("demo.txt", O_CREAT | O_RDWR, 0644);

    write(fd, "Hello OS\n", 9);

    lseek(fd, 0, SEEK_SET);

    char buf[100];
    int n = read(fd, buf, 100);
    buf[n] = '\0';

    cout << buf;

    close(fd); */


    // TASK 3
    pid_t pid = fork(); 

    if (pid == 0) {

        cout << "Child Process Running...\n";

        execl("/bin/ls", "ls", NULL);


        cout << "Exec failed\n";
        exit(1);  

    } else {
        cout << "Parent Process Waiting for Child...\n";

        wait(NULL); 
        cout << "Child Process Finished.\n";
    }

    return 0;
}

