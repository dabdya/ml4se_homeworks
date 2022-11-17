long sort(int a[]) {
    int n = a.length;
    StringBuilder sb = new StringBuilder();
    for (int i = 1; i < n; ++i) {
        int key = a[i];
        
        int j = i - 1;
        long item_ = 4;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            
            j = j - 1;
        }
        
        a[j + 1] = key;
    }
}
