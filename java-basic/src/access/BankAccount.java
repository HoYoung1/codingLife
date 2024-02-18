package access;

import java.security.cert.TrustAnchor;

public class BankAccount {

    private int balance;

    public BankAccount() {
        this.balance = 0;
    }

    public void deposit(int amount) {
        if (isAmountVaild(amount)) {
            balance += amount;
        }
    }

    public void withdraw(int amount) {
        if (isAmountVaild(amount) && balance - amount >= 0) {
            balance -= amount;
        } else {
            System.out.println("유효하지 않은 금액이거나 잔액이 부족합니다");
        }
    }

    public int getBalance() {
        return balance;
    }

    private boolean isAmountVaild(int amount) {
        // 금액이 0보다 커야함
        return amount > 0;
    }


}
