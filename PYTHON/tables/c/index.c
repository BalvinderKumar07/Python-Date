// #include<stdio.h>

// int main()
// {
//     int a  = 8;
//     float b = 7.9;
//     // char c[10]="balvinder";

//     printf("the sum fo a and b is ",a+b);
// }

#include <stdio.h>
int main() {    

    int number1, number2, sum;
    
    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    // calculating sum
    sum = number1 + number2;      
    
    printf("%d + %d = %d", number1, number2, sum);
    return 0;
}