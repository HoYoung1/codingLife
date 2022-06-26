import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class SplitPhase6_11_6 {
    public static void main(String[] args) {
        try {
            System.out.println(run(args));
        } catch (Exception e) {
            System.err.println(e);
            System.exit(1);
        }
    }

    private static long run(String[] args) throws IOException {
        CommandLine commandLine = parseCommandLine(args);
        return countOrders(commandLine);
    }

    private static CommandLine parseCommandLine(String[] args) {
        if (args.length == 0) throw new RuntimeException("파일 명을 입력하세요");
        CommandLine commandLine = new CommandLine();
        commandLine.onlyCountReady = Stream.of(args).anyMatch(arg -> "-r".equals(arg));
        commandLine.fileName = args[args.length - 1];
        return commandLine;
    }

    private static long countOrders(CommandLine commandLine) throws IOException {
        File input = Paths.get(commandLine.fileName).toFile();
        ObjectMapper mapper = new ObjectMapper();
        Order[] orders = mapper.readValue(input, Order[].class);
        if (commandLine.onlyCountReady) {
            return Stream
                    .of(orders)
                    .filter(o -> "ready".equals(o.status))
                    .count();
        } else {
            return orders.length;
        }
    }
}
