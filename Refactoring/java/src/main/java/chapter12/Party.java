package chapter12;

public class Party {
    public Party(int monthlyCost) {
        this.monthlyCost = monthlyCost;
    }

    private int monthlyCost;

    public int annualCost() {
        return this.monthlyCost * 12;
    }
}
