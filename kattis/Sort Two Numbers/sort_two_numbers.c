#include <stdio.h>

int main(void) {
        long long a, b;
        scanf("%lld%lld", &a, &b);
        if (a < b)
                printf("%lld %lld\n", a, b);
        else
                printf("%lld %lld\n", b, a);
}
