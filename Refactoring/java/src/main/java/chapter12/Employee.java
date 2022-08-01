package chapter12;

public class Employee extends Party {
    private final Long _id;
    private final Integer _monthlyCost;

    public Employee(String name, Long id, Integer monthlyCost) {
        super();
        this._name = name;
        this._id = id;
        this._monthlyCost = monthlyCost;
    }
}
