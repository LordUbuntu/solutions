/* Jacobus Burger (2022)
 * Two sum
 * Add two numbers together
 */
#include <stdio.h>

int
main(void)
{
        long long a, b;
        while(scanf("%lld%lld", &a, &b) == 2)
        {
                printf("%lld\n", (a + b));
        }
}
