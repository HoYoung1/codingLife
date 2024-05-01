package time.test;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

public class TestCalendarPrinter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("년도를 입력하세요 : ");
        String year = scanner.nextLine();

        System.out.print("월을 입력하세요 : ");
        String month = scanner.nextLine();

        printCalendar(year, month);

    }

    private static void printCalendar(String year, String month) {
        LocalDate firstDate = LocalDate.of(Integer.parseInt(year), Integer.parseInt(month), 1);
        LocalDate nextMonth = firstDate.plusMonths(1);

        int offsetDay = firstDate.getDayOfWeek().getValue() % 7;
        System.out.println("firstDate.getDayOfWeek() = " + firstDate.getDayOfWeek());
        System.out.println("firstDate.getDayOfWeek() = " + offsetDay);

        System.out.println("Su Mo Tu We Th Fr Sa");
        for (int i = 0; i < offsetDay; i++) {
            System.out.print("   ");
        }

        LocalDate dateIterator = firstDate;
        while (dateIterator.isBefore(nextMonth)) {
            System.out.printf("%2d ", dateIterator.getDayOfMonth());
            if (dateIterator.getDayOfWeek() == DayOfWeek.SATURDAY) {
                System.out.println("");
            }

            dateIterator = dateIterator.plusDays(1);
        }




//        offsetDay


    }
}
