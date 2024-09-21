/*
https://github.com/eugenechevski
https://leetcode.com/problems/baseball-game
*/

import java.util.Stack;

class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> st = new Stack<>();

        // Read the input
        String token = "";
        for (int i = 0; i < operations.length; i++) {
            token = operations[i];
            if (Character.isDigit(token.charAt(0)) || token.startsWith("-")) // push the record
            {
                st.push(Integer.valueOf(token));
            } else if (token.equals("+")) // add the last two records
            {
                Integer a = st.pop();
                Integer b = st.pop();
                st.push(b);
                st.push(a);
                st.push(a + b);
            } else if (token.equals("D")) // record the double of the previous score
            {
                st.push(2 * st.peek());
            } else if (token.equals("C")) // invalidate the previous score
            {
                st.pop();
            }
        }

        // Sum up all the records and return the result
        return st.stream().mapToInt(Integer::intValue).sum();
    }
}