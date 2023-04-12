#include <stdio.h>


int main(void) {
        long long a, b, c;
        scanf("%lld%lld%lld", &a, &b, &c);
        if (a + b == c) {
                puts("correct!");
        }
        else {
                puts("wrong!");
        }
}
