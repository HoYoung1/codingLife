package array;

public class ArrayDi3 {
    public static void main(String[] args) {
//        int[][] arr = new int[][]{
//                {1,2,3},
//                {4,5,6},
//        };

        int[][] arr = {
                {1,2,3},
                {4,5,6},
        };
//        arr[0][0] = 1;
//        arr[0][1] = 2;
//        arr[0][2] = 3;
//        arr[1][0] = 4;
//        arr[1][1] = 5;
//        arr[1][2] = 6;

//        System.out.print(arr[0][0] + " ");
//        System.out.print(arr[0][1] + " ");
//        System.out.print(arr[0][2] + " ");
//        System.out.println();
//        System.out.print(arr[1][0] + " ");
//        System.out.print(arr[1][1] + " ");
//        System.out.print(arr[1][2] + " ");

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }


    }
}
