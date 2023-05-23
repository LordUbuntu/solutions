
/* Jacobus Burger 2023
 * desc:
 *      Write code to give the next traffic light colour for a given
 *      current traffic light colour.
 * solution:
 *      Origianlly, I cast the value of light + 1 mod 3 to an enum
 *      but soon realized from other solutions that I can safely
 *      assume enum to be treated like int and so perform the
 *      same calculation more directly.
 * more info:
 *      https://www.codewars.com/kata/58649884a1659ed6cb000072/c
 */

enum light {GREEN, YELLOW, RED};

enum light update_light(enum light light) {
        // originally:
        //      (enum light)((light + 1) % 3)
        return ++light % 3;
}
