package exception.ex1;

public class NetworkServiceV1_1 {
    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV1 networkClient1 = new NetworkClientV1(address);
        networkClient1.initError(data);

        networkClient1.connect();
        networkClient1.send(data);
        networkClient1.disconnect();

    }


}
