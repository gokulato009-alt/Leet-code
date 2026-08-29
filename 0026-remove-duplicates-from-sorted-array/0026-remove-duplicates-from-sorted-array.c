int removeDuplicates(int* arr, int n) {
    int i=0, j=0;
    while(j<n){
        if(arr[i]!=arr[j]){
            i++;
            int temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
        }
        j++;
    }
    return i+1;
}