/* Jacobus Burger (2022)
 * Problem:
 *   Determine how many ramp numbers there are from a given ramp number
 *   down to and including the number 1.
 *   A ramp number is a number whose digits are strictly increasing
 *   in value from most to least significant digit. For example:
 *      123
 *      11223
 *      11
 * Solution:
 *   The neiive solution shown here involves looking at every single
 *   number from n down to 0 and checking if they meet the conditions
 *   of a ramp number (and counting them if they do). It's very
 *   inefficient and fails time requirements on 80 digits.
 */
#include <stdio.h>
#include <stdlib.h>

int
num_digits(long long n)
{
        if (n / 10 == 0)
                return 1;
        return 1 + num_digits(n / 10);
}

int
is_ramp(long long n)
{
        int digits = num_digits(n);
        char str[digits];
        sprintf(str, "%lld", n);

        if (digits <= 1)
                return 1;

        char ramping = 0;
        for (int i = 0; i < digits - 1; i++)
        {
               // ramp condition failed
               if ( (((int)str[i]) - '0') > (((int)str[i + 1]) - '0') )
                       return 0;
               else
                       ramping = 1;
        }

        return ramping;
}


int
ramp_number(long long n)
{
        if (!is_ramp(n))
                return -1;

        int count = 0;
        while (n > 0)
        {
                if (is_ramp(n))
                        count++;
                n--;
        }

        return count;
}


int
main(void)
{
        long long T, n;
        scanf("%lld", &T);

        for (int i = 0; i < T; i++)
        {
                scanf("%lld", &n);
                printf("%i\n", ramp_number(n));
        }
}

