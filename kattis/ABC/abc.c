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

        // substitute letters in string with numbers
        //      calculate total anticipated length of answer strng
        size_t len = snprintf(NULL, 0, "%lld %lld %lld\n", arr[0], arr[1], arr[2]);
        //      get letter ordering
        char ans[len], ord[len];
        scanf("%s", ord);
        //      substitute letters in string
        size_t num_len;
        size_t offset = 0;
        int index = 0;
        for (size_t i = 0; i < 3; i++) {
                // get the current char* representation of the number value
                switch (ord[i]) {
                        case 'A': 
                                index = 0;
                                break;
                        case 'B':
                                index = 1;
                                break;
                        case 'C':
                                index = 2;
                                break;
                }
                num_len = snprintf(NULL, 0, "%lld", arr[index]);
                char num_str[num_len];
                snprintf(num_str, num_len, "%lld", arr[index]);
                // copy characters over to answer
                memcpy(&ans[offset], num_str, num_len + 1);
                offset += num_len;
        }
        // end string with newline and print it
        ans[len - 1] = '\n';
        printf("%s", ans);
}
