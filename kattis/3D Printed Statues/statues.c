#include <stdio.h>

int main(void) {
        long double n;
        scanf("%Lf", &n);
        long long d;
        d = 0;
        while (n > 0) {
                if (n > 1)
                        n /= 2;
                else
                        n -= 1;
                d += 1;
        }
        printf("%lld\n", d);
}
