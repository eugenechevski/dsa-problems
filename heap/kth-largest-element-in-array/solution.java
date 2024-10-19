import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(nums.length, (a, b) -> b - a);

        // Add all elements to the heap
        for (int num : nums) {
            maxHeap.add(num);
        }

        // Remove k - 1 elements from the heap
        for (int i = 0; i < k - 1; i++) {
            maxHeap.poll();
        }

        // Return the kth largest element
        return maxHeap.poll();
    }
}