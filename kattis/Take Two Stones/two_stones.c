/* Jacobus Burger (2022)
 * Take two stones
 * Choose winner based on evenness of stones
 */
#include <stdio.h>

int
main(void)
{
        long long i;
        
        // if the start is even, the end is even, otherwise odd
        while(scanf("%lld", &i) == 1)
        {
                if (i % 2 == 0)
                        printf("Bob");
                else
                        printf("Alice");
        }
}
