#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAXBITS 32

void radixSort(int *unsorted);

void radixSort(int *unsorted){
    //int *bin0 = (int)malloc(sizeof(*unsorted));
    int bin0[sizeof(*unsorted)];
    //int *bin1 = (int)malloc(sizeof(*unsorted));
    int bin1[sizeof(*unsorted)];
    int i, j, bitValue, bin1Index=0, bin0Index=0;
    int length = sizeof(*unsorted);

    for(i=0;i<MAXBITS;i++){
        bin0Index=0,bin1Index=0;
        for(j=0;j<length;j++){
            bitValue =  (unsorted[j] & (1 << i)) >> i;
            if (bitValue){
                bin1[bin1Index] = unsorted[j];
                bin1Index++;
            }else{
                bin0[bin0Index] = unsorted[j];
                bin0Index++;
            }

        }
        for(j=0;j<bin0Index;j++){
            unsorted[j] = bin0[j];
        }
        for(;j<bin1Index+bin0Index;j++){
            unsorted[j] = bin1[j-bin0Index];
        }
    }
}

int main(){
    int unsortedList[4];
    unsortedList[0] = 34;
    unsortedList[1] = 874;
    unsortedList[2] = 1;
    unsortedList[3] = 99;
    int i;

    radixSort(unsortedList);

    for(i=0;i<4;i++){
        printf("%d\n", unsortedList[i]);
    }

    return 0;
}


