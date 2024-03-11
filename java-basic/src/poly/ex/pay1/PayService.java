package poly.ex.pay1;

public class PayService {
    public void processPay(String option, int amount) {

        System.out.println("결제를 시작합니다. option = " + option + "amount = " + amount);

        if (PayStore.findPay(option).pay(amount)) {
            System.out.println("결제가 성공했습니다.");
        } else {
            System.out.println("결제중 실패했습니다.");
        }
    }
}
