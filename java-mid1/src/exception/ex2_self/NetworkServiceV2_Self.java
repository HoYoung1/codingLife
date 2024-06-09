package exception.ex2_self;

public class NetworkServiceV2_Self {
    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV2_Self networkClient = new NetworkClientV2_Self(address);
        networkClient.initError(data);

        try {
            networkClient.connect();
            networkClient.send(data);
        } catch (NetworkClientExceptionV2_Self e) {
            System.out.println(e);
        } finally {
            networkClient.disconnect();
        }

    }
}
