balance = 100000
roi = 12
months = 12
count = 0
for i in range(months):
	final = (roi/100 * balance)/12
	balance = final + balance
	count = count + 1
	if count == 5:
		balance = balance - 25000
	elif count == 9:
		balance = balance + 10000
	else :
		print(balance)

#include <stdio.h>

void towerOfHanoi(int n, char source, char auxiliary, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination);
        return;
    }

    towerOfHanoi(n - 1, source, destination, auxiliary);
    printf("Move disk %d from %c to %c\n", n, source, destination);
    towerOfHanoi(n - 1, auxiliary, source, destination);
}

int main() {
    int num_disks;
    
    printf("Enter the number of disks: ");
    scanf("%d", &num_disks);
    
    towerOfHanoi(num_disks, 'A', 'B', 'C');
    
    return 0;
}