package algorithms;

public class quicksort {
	
	private int array[];
    private int length;
 
    public void sort(int[] inputArr) {
         
        if (inputArr == null || inputArr.length == 0) {
            return;
        }
        this.array = inputArr;
        length = inputArr.length;
        quickSort(0, length - 1);
    }
 
    private void quickSort(int lowerIndex, int higherIndex) {
         
        int i = lowerIndex;
        int j = higherIndex;
        
        int pivot = array[lowerIndex+(higherIndex-lowerIndex)/2];
        
        while (i <= j) {
            /**
             * In each iteration, we will identify a number from left side which
             * is greater then the pivot value, and also we will identify a number
             * from right side which is less then the pivot value. Once the search
             * is done, then we exchange both numbers.
             */
            while (array[i] < pivot) {
                i++;
            }
            while (array[j] > pivot) {
                j--;
            }
            if (i <= j) {
                exchangeNumbers(i, j);
                
                i++;
                j--;
            }
        }
        
        if (lowerIndex < j)
            quickSort(lowerIndex, j);
        if (i < higherIndex)
            quickSort(i, higherIndex);
    }
 
    private void exchangeNumbers(int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
     
    public static void main(String a[]){
    	
    	long startTime = System.currentTimeMillis(); 
        quicksort sorter = new quicksort();
        int[] input = new int[100000];
        for (int i = 0; i < input.length; i++){
	    	input[i] = (int)(Math.random() * (1000000 - 0.000001) + 0.000001);
	    }
        sorter.sort(input);
        long endTime = System.currentTimeMillis();
        
	    System.out.println("Total execution time: " + (endTime-startTime) + "ms");
	    
	    long startTime2 = System.currentTimeMillis();
	    quicksort sorter2 = new quicksort();
	    sorter2.sort(input);
	    long endTime2 = System.currentTimeMillis();
	    
	    System.out.println("Total execution time: " + (endTime2-startTime2) + "ms");
	    
    }

}
