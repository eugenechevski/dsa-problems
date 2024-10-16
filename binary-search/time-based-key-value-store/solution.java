import java.util.HashMap;
import java.util.ArrayList;
import java.util.Map;

class TimeMap {
    private Map<String, Integer> keyToTime; // key -> timestamps_index
    private Map<String, Map<Integer, String>> keyToTimeToVal; // key -> timestamp -> val
    private ArrayList<ArrayList<Integer>> timestamps;

    public TimeMap() {
        keyToTime = new HashMap<>();
        keyToTimeToVal = new HashMap<>();
        timestamps = new ArrayList<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!keyToTime.containsKey(key)) // the key is not present
        {
            // initialize the maps and the list
            keyToTime.put(key, timestamps.size());
            keyToTimeToVal.put(key, new HashMap<>());
            timestamps.add(new ArrayList<>());
        }

        // update the timestamps
            
        // get the timestamps index
        int index = keyToTime.get(key);

        // add the timestamp
        timestamps.get(index).add(timestamp);

        // add the value at the timestamp
        keyToTimeToVal.get(key).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        if (!keyToTime.containsKey(key)) { return ""; } // no key found

        // found the timestamp
        if (keyToTimeToVal.get(key).containsKey(timestamp)){ return keyToTimeToVal.get(key).get(timestamp); }

        // not timestamp found, perform BST to get the closest predecessor

        // get the array
        int index = keyToTime.get(key);
        ArrayList<Integer> arr = timestamps.get(index);
        
        // The requested timestamp is outside of the range of values
        if (timestamp < arr.get(0))
        {
            return "";
        }

        // start the BST
        int l = 0, r = arr.size() - 1;
        int m = 0;
        while (l <= r)
        {
            m = (l + r) / 2;
            
            if (timestamp < arr.get(m))
            {
                r = m - 1;
            }
            else
            {
                l = m + 1;
            }
        }

        // Determine the correct preceding timestamp index
        String result = "";
        int prevTimestamp = 0;
        if (timestamp < arr.get(m))
        {
            prevTimestamp = arr.get(m - 1);
        }
        else
        {
            prevTimestamp = arr.get(m);
        }

        result = keyToTimeToVal.get(key).get(prevTimestamp);
        
        return result; // no val
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */