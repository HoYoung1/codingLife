package chapter6;

import java.util.stream.Stream;

public class CommandLine_v2 {
    String[] args;
    public CommandLine_v2(String[] args) {
        this.args = args;
        if (args.length == 0) throw new RuntimeException("파일 명을 입력하세요");
    }

    public String filename() {
        return args[args.length - 1];
    }

    public boolean onlyCountReady() {
        return Stream.of(args).anyMatch(arg -> "-r".equals(arg));
    }

}
