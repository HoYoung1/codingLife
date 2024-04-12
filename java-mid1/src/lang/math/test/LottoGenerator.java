package lang.math.test;

import java.util.Random;

public class LottoGenerator {
    private int[] lottoNum;
    private int count;
    private Random random = new Random();

    public void generate() {
        Random random = new Random();
        lottoNum = new int[6];
        count = 0;

        while (count < 6) {
            int randomValue = random.nextInt(0, 45) + 1;
            if (!hasAlready(lottoNum, randomValue)) {
                lottoNum[count] = randomValue;
                count += 1;
            }
        }
    }

    private boolean hasAlready(int[] lottoNum, int target) {
        for (int num : lottoNum) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }

    public int[] getLottoNum() {
        return lottoNum;
    }
}
