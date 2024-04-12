package lang.math.test;

import java.util.Arrays;

public class LottoGeneratorMain {
    public static void main(String[] args) {
        LottoGenerator lottoGenerator = new LottoGenerator();
        lottoGenerator.generate();
        String string = Arrays.toString(lottoGenerator.getLottoNum());
        System.out.println(string);
    }
}
