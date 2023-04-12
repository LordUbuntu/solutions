/* Jacobus Burger (2023)
 * See:
 *  https://open.kattis.com/problems/simonsays
 */
#include <stdio.h>
#include <string.h>


int main(void) {
        long long N;
        scanf("%lld", &N);

        char input[101];
        for (int i = 0; i < N + 1; i++) {
                fgets(input, 101, stdin);
                if (strncmp(input, "Simon says", 10) == 0)
                        printf("%s", (input + 11));
        }
}
