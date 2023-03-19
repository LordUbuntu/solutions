#include <stdio.h>
#include <string.h>

int main(void) {
        char *s;
        scanf("%ms", &s);
        for (int i = 1; i < strlen(s); i++) {
                // find first occurence of "ss" and print "hiss"
                if (s[i - 1] == 's' && s[i] == 's') {
                        printf("hiss");
                        return 0;
                }
        }
        // otherwise print "no hiss"
        printf("no hiss");
}
