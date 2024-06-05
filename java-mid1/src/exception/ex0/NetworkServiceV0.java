package exception.ex0;

public class NetworkServiceV0 {
    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV0 networkClient0 = new NetworkClientV0(address);

        networkClient0.connect();
        networkClient0.send(data);
        networkClient0.disconnect();

    }


}
