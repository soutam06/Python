#include<stdio.h>
int i=0;
int power(int a,int b){
    if (!b) return 1;
    int temp= power(a,b/2) * power(a,b/2);
    if (b%2==1) temp*=a;
    i+=1;
    printf("%d\t",temp);
    printf("%d\t",i);
    printf("%d\n",b);

    return temp;
}
int main(){
    printf("temp\ti\tb");
    printf("\n");
    printf("%d",power(2,7));
    return 0;
}