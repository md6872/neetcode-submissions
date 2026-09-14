class Solution {
    public int countSeniors(String[] details) {
        int count = 0;

        for (String p : details) {
            if (Integer.parseInt(p.substring(11,13)) > 60) {
                count ++;
            }
        }

        return count;
    }
}