package exception.ex2;

import exception.ex2_self.NetworkClientExceptionV2_Self;

public class NetworkServiceV2_1 {
    public void sendMessage(String data) throws NetworkClientExceptionV2 {
        String address = "http://example.com";
        NetworkClientV2 networkClient1 = new NetworkClientV2(address);
        networkClient1.initError(data);

        networkClient1.connect();
        networkClient1.send(data);
        networkClient1.disconnect();

    }


}
