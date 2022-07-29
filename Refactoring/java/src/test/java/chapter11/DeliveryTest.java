package chapter11;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DeliveryTest {

    @Test
    void deliveryDate() {
        Order order = new Order("MA");
        boolean isRush1 = false;
        assertEquals(Delivery4.deliveryDate(order, isRush1), 4);

        boolean isRush2 = true;
        assertEquals(Delivery4.deliveryDate(order, isRush2), 2);
    }
}