package exception.ex4;

public class NetworkServiceV5 {
    public void sendMessage(String data) {
        String address = "http://example.com";

        try (NetworkClientV5 networkClient = new NetworkClientV5(address)) {
            networkClient.initError(data);
            networkClient.connect();
            networkClient.send(data);
        } catch (Exception e) {
            System.out.println("[예외확인]: " + e.getMessage());
            throw e;
        }
    }
}
