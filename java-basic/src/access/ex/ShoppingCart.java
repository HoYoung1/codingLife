package access.ex;

public class ShoppingCart {

    private Item[] items = new Item[10];
    private int itemCount;

    public void addItem(Item item) {
        if (itemCount >= items.length) {
            System.out.println("꽉차서 담을수 없습니다");
            return;
        }
        items[itemCount] = item;
        ++itemCount;
    }

    public void displayItems() {
        for (int i = 0; i < itemCount; i++) {
            System.out.println(items[i]);
        }
    }
}
