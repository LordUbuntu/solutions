/* Jacobus Burger (2023)
 * Solution:
 *      We just calculate difference from input. Must be careful of
 *      integer precision in this case however.
 * See:
 *      https://open.kattis.com/problems/different
 */
#include <stdio.h>

int main(void) {
        unsigned long long a, b;
        while (fscanf(stdin, "%llu %llu", &a, &b) != EOF) {
                printf("%llu\n", (a > b) ? a - b : b - a);
        }
}
