package nested.nested.test.ex1;

public class Library {

    Book[] books;
    int bookIndex;

    public Library(int bookNum) {
        books = new Book[bookNum];
        bookIndex = 0;
    }

    public void addBook(String bookName, String author) {
        if (bookIndex >= books.length) {
            System.out.println("도서관 저장 공간이 부족합니다.");
            return;
        }
        books[bookIndex++] = new Book(bookName, author);
    }

    public void showBooks() {
        for (Book book : books) {
            System.out.println("도서 제목:" + book.title + ", 저자 : " + book.author);
        }
    }

    private static class Book {
        private String title;
        private String author;

        public Book(String title, String author) {
            this.title = title;
            this.author = author;
        }
    }
    // 코드 작성
}
