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
 *   inefficient.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

long long ramp(long long n);
int num_digits(long long n);
int char_to_int(char c);

int
main(void)
{
        long long T, n;
        scanf("%lld", &T);

        for (int i = 0; i < T; i++) {
                scanf("%lld", &n);
                printf("%lld\n", ramp(n));
        }
}


long long
ramp(long long n)
{
        // check the input is legit
        if (num_digits(n) > 1)
        {
                // represent n as a string
                int digits = num_digits(n);
                char str[digits];
                sprintf(str, "%lld", n);
                
                for (int i = 0; i < digits - 1; i++)
                {
                        // get digits
                        char current_digit = str[i];
                        char next_digit = str[i + 1];

                        // stop if input is illegitimate
                        if (char_to_int(current_digit) > char_to_int(next_digit))
                                return -1;
                }
        }

        int total = 0;

        while (n > 0)
        {
                // represent n as a string
                int digits = num_digits(n);
                char str[digits];
                sprintf(str, "%lld", n);
                
                // check if it ramps (naiive solution)
                if (digits > 1)
                {
                        bool ramping = false;
                        for (int i = 0; i < digits - 1; i++)
                        {
                                // get digits
                                char current_digit = str[i];
                                char next_digit = str[i + 1];

                                // check pair of digits
                                if (char_to_int(current_digit) <= char_to_int(next_digit))
                                {
                                        ramping = true;
                                }
                                else
                                {
                                        ramping = false;
                                        break;
                                }
                        }

                        // count ramp
                        if (ramping)
                        {
                                total++;
                                ramping = false;
                        }
                }
                else
                {
                        total++;
                }


                // decrement integer
                n--;
        }

        return total;  // +1 is including 0 as a ramp number
}


int
num_digits(long long n)
{
        if (n / 10 == 0)
                return 1;
        return 1 + num_digits(n / 10);
}


// convert char digit to int value of char
int
char_to_int(char c)
{
        return ((int)c) - 48;
}
