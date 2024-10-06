/*
https://github.com/eugenechevski
https://leetcode.com/problems/lfu-cache
*/

import java.util.HashMap;

class Node {
    int key;
    int val;
    int freq;
    Node next;
    Node prev;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.freq = 1;
    }

    public Node() {
        this.key = -1;
        this.freq = 1;
    }
}

class LL {
    Node head;
    Node tail;

    public LL()
    {
        head = null;
        tail = null;
    }

    // Swaps the given node with the one to the left
    // if the frequency of the given node is greater than the frequency of the node to the left
    public void swapLeft(Node target)
    {
        // Check if there's a node to the left and the frequency of the target node is greater
        if (target.prev != null && target.prev.freq < target.freq) {
            // swap the current with the previous
            // A <-> B <-> T <-> C

            // B <- C 
            // update the target.next
            if (target.next != null) {
                target.next.prev = target.prev;
            }

            // A -> T
            // update target.prev.prev
            if (target.prev.prev != null) {
                target.prev.prev.next = target;
            }

            // Save A
            Node prevPrev = target.prev.prev;

            target.prev.prev = target; // T <- B 
            target.prev.next = target.next; // B -> C

            target.next = target.prev; // T -> B
            target.prev = prevPrev; // A <- T

            // Final structure: A <-> T <-> B <-> C

            // update the head if target moves to the front of the list
            if (target.prev == null) 
            {
                head = target;
            }

            // update the tail if B moves to the end of the list
            if (target.next.next == null)
            {
                tail = target.next;
            }
        }
    }

    // inserts a node to the front of the list
    public void insertFront(Node target)
    {
        if (head != null)
        {
            target.next = head;
            head.prev = target;
        }
        head = target;

        if (tail == null)
            tail = target;
    }

    public void appendNode(Node target)
    {
        if (head == null)
        {
            insertFront(target);
        }
        else
        {
            tail.next = target;
            tail = target;
        }
    }

    // removes the given node from the list
    // by removing the links and update head and tail
    public void removeNode(Node target)
    {   
        if (target.prev != null)
            target.prev.next = target.next;

        if (target.next != null)
            target.next.prev = target.prev;

        if (head == target)
            head = target.next;
        
        if (tail == target)
            tail = target.prev;

        target.prev = null;
        target.next = null;
    }

    // removes the tail from the list
    public Node pop()
    {
        // the list is empty
        if (head == null || tail == null)
            return null;

        // there's one node in the list
        Node popped = tail;
        if (head == tail)
        {
            head = null;
            tail = null;
        }
        else
        {
            tail.prev.next = null; // remove the link from the previous node
            tail = tail.prev; // update the tail
        }

        // return the popped node
        return popped;
    }
}

class LFUCache {
    private HashMap<Integer, Node> data; // maps: key -> Node
    private LL lfu; // stores based on frequency order: node_i -> node_i+1
    private LL lru; // stores based on usage where head is the recently used item
    private int size;
    private int cap;

    public LFUCache(int capacity) {
        data = new HashMap<>(capacity);
        lfu = new LL();
        lru = new LL();
        cap = capacity;
        size = 0;
    }

    // a utility for evicting lfu or if tie lru
    private Node evict()
    {   
        // Check if there's the tie in lfu
        Node evicted = null;
        if (lfu.tail.prev != null && lfu.tail.prev.freq == lfu.tail.freq) // there's a tie
        {
            // use lru for eviction decision
            evicted = lru.pop();
        }
        else
        {
            // use lfu for eviction decision
            evicted = lfu.pop();
        }

        // update the capacity
        size--;

        // return the evicted node
        return evicted;
    }

    public int get(int key) {
        // check if the key is present
        if (data.containsKey(key)) {
            // update the frequency
            Node target = data.get(key);
            target.freq++;

            // update lfu list
            lfu.swapLeft(target);

            // update lru list
            lru.removeNode(target);
            lru.insertFront(target);

            // return the value of the key
            return target.val;
        }

        return -1;
    }

    public void put(int key, int value) {
        if (data.containsKey(key))
        {
            // Obtain the existing node
            Node target = data.get(key);

            // Update the value
            target.val = value;

            // Update the frequency
            target.freq++;

            // Update lfu
            lfu.swapLeft(target);

            // Update lru
            lru.removeNode(target);
            lru.insertFront(target);
        }
        else
        {
            // Create the new node
            Node newData = new Node(key, value);

            // Update the map
            data.put(key, newData);

            // Update the capacity
            size++;

            // Check if eviction is required
            if (size > cap)
            {
                Node evicted = evict();
                data.remove(evicted.key);
                lfu.removeNode(evicted);
                lru.removeNode(evicted);
            }

            // Add the new node to lfu
            lfu.appendNode(newData);

            // Add the new to lru
            lru.insertFront(newData);
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */