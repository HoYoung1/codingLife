package chapter6;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class SplitPhase6_11_3_v2 {
    public static void main(String[] args) {
        try {
            System.out.println(run(args));
        } catch (Exception e) {
            System.err.println(e);
            System.exit(1);
        }
    }

    private static long run(String[] args) throws IOException {
        CommandLine_v2 commandLine = new CommandLine_v2(args);
        return countOrders(commandLine);
    }

    private static long countOrders(CommandLine_v2 commandLine) throws IOException {
        File input = Paths.get(commandLine.filename()).toFile();
        ObjectMapper mapper = new ObjectMapper();
        Order[] orders = mapper.readValue(input, Order[].class);
        if (commandLine.onlyCountReady()) {
            return Stream
                    .of(orders)
                    .filter(o -> "ready".equals(o.status))
                    .count();
        } else {
            return orders.length;
        }
    }
}
