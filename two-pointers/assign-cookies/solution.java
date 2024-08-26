/*
https://github.com/eugenechevski
https://leetcode.com/problems/assign-cookies
*/

import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // Sort both arrays
        Arrays.sort(g);
        Arrays.sort(s);

        int gSize = g.length; // size of the 'g' array
        int sSize = s.length; // size of the 's' array
        int numOfContentChildren = 0; // Resulting variable
        int gPtr = 0; // g pointer
        int sPtr = 0; // s pointer

        // Iterate over the sizes of cookies and advance pointers if the
        // following condition is met: g[gPtr] <= s[sPtr] or we run out of bounds
        while (gPtr < gSize && sPtr < sSize) {
            while (sPtr < sSize && g[gPtr] > s[sPtr]) {
                sPtr++;
            } // advance the s pointer
            if (sPtr < sSize && g[gPtr] <= s[sPtr]) { // check the condition
                numOfContentChildren++;
                gPtr++;
                sPtr++;
            }
        }

        return numOfContentChildren;
    }
}