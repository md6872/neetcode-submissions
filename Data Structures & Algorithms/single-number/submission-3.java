class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> map = new HashSet<>();

        for (int n: nums) {
            if (map.contains(n)) {
                map.remove(n);
            } else {
                map.add(n);
            }
        }

        return map.iterator().next();
    }
}
