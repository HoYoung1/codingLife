package exception.ex2;

public class NetworkServiceV2_2 {
    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV2 networkClient1 = new NetworkClientV2(address);
        networkClient1.initError(data);

        try {
            networkClient1.connect();
        } catch (NetworkClientExceptionV2 e) {
            System.out.println("[오류] 오류코드 : " + e.getErrorCode() + " 메세지 : " + e.getMessage() );
            return;
        }
        try {
            networkClient1.send(data);
        } catch (NetworkClientExceptionV2 e) {
            System.out.println("[오류] 오류코드 : " + e.getErrorCode() + " 메세지 : " + e.getMessage() );
            return;
        }
        networkClient1.disconnect();

    }


}
