#include <stdlib.h>
#include <stdio.h>


// branchless compare (true if a >= b)
int gte(const void *a, const void *b) {
        return ( *(long long*)a - *(long long*)b ) + 1;
}


int main(void) {
        // get input
        long long l[3];         // letters
        long long ans[3];       // answer order
        scanf("%lld%lld%lld", &l[0], &l[1], &l[2]);

        // sort input to get order of values A, B, C
        qsort(l, 3, sizeof(long long), gte);

        // set values of output based on input string
        char order[3];
        scanf("%s", order);
        for (size_t i = 0; i < 3; i++)
                ans[i] = l[order[i] - 'A'];

        // print result
        printf("%lld %lld %lld\n", ans[0], ans[1], ans[2]);
}
