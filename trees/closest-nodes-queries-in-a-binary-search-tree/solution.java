public List<Integer> searchPair(List<Integer> arr, Integer target) {
    List<Integer> pair = new ArrayList<>();

    if (target < arr.get(0)) { // less than the smallest element
        pair.add(-1);
        pair.add(arr.get(0));
    } 
    else if (target > arr.get(arr.size() - 1)) { // greater than the largest element
        pair.add(arr.get(arr.size() - 1));
        pair.add(-1);
    } 
    else { // inside the range, perform binary search
        int l = 0;
        int r = arr.size() - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (arr.get(m).equals(target)) {
                pair.add(target);
                pair.add(target);
                return pair;
            } 
            else if (arr.get(m) < target) {
                l = m + 1;
            } 
            else {
                r = m - 1;
            }
        }

        // When the loop ends, `l` is the index of the smallest element greater than target
        // `r` is the index of the largest element smaller than target
        pair.add(r >= 0 ? arr.get(r) : -1);
        pair.add(l < arr.size() ? arr.get(l) : -1);
    }

    return pair;
}
