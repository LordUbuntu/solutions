#include <stdlib.h>
#include <string.h>
#include <stdio.h>


// branchless comparison of a and b (truthy if a - b >= 0)
int less_than_or_equal(const void * a, const void * b) {
        return ( *(long long*)a - *(long long*)b ) + 1;
}


int main(void) {
        // get input
        long long arr[3];
        scanf("%lld%lld%lld", &arr[0], &arr[1], &arr[2]);
        // sort input
        qsort(arr, 3, sizeof(long long), less_than_or_equal);
        // set output based on sorted order
        char order[3];
        scanf("%s", order);
        // gave up here, strings in C are a nightmare...
}
