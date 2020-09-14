
public class Main {
    public static void main(String[] args) {
        int[] arr = new int[]{45,7,99,2,54,85,3,1,6,84};
        quickSort(arr,0,9);
        printArray(arr);

    }

    public static void quickSort(int[] arr, int low, int high){
        if(low < high) {
            int partIndex = partion(arr, low, high);
            quickSort(arr, low, partIndex - 1);
            quickSort(arr, partIndex + 1, high);
        }
    }

    public static int partion(int[] arr, int low, int high){
        int temp;
        int pivot = arr[high];
        int i = low;
        for(int j=low; j<high; j++){
            //if(arr[j] < pivot) for inc order
            // this is for dec ordder
            if(arr[j] > pivot){
                    temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;
                    i++;

            }
        }
        temp = arr[high];
        arr[high] = arr[i];
        arr[i] = temp;
        return i;
    }

    public static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
