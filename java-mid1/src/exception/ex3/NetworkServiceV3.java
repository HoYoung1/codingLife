package exception.ex3;

import exception.ex3.exception.ConnectExceptionV3;
import exception.ex3.exception.SendExceptionV3;

public class NetworkServiceV3 {
    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV3 networkClient = new NetworkClientV3(address);
        networkClient.initError(data);

        try {
            networkClient.connect();
            networkClient.send(data);
        } catch (ConnectExceptionV3 e) {
            System.out.println("[연결 오류] 주소 : " + e.getAddress() + ", 메세지 : " + e.getMessage());
        } catch (SendExceptionV3 e) {
            System.out.println("[전송 오류] 전송데이터 : " + e.getSendData() + ", 메세지 : " + e.getMessage());
        } finally {
            networkClient.disconnect();
        }

    }


}
