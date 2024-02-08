package oop1.ex;

public class RectangleOopMain {
    public static void main(String[] args) {

        Rectangle rectangle = new Rectangle();
        rectangle.width = 5;
        rectangle.height = 8;

        int area = rectangle.calculateArea();
        System.out.println("area = " + area);

        int perimeter = rectangle.calculatePerimeter();
        System.out.println("perimeter = " + perimeter);

        boolean square = rectangle.isSquare();
        System.out.println("square = " + square);

    }

}
