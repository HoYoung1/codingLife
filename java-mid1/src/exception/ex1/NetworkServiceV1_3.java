package exception.ex1;

public class NetworkServiceV1_3 {
    public void sendMessage(String data) {
        String address = "http://example.com";
        NetworkClientV1 networkClient1 = new NetworkClientV1(address);
        networkClient1.initError(data);

        String connectResult = networkClient1.connect();
        if (isError(connectResult)) {
            System.out.println("[네트워크 오류 발생] 오류 코드 : " + connectResult);
        } else {
            String sendResult = networkClient1.send(data);
            if (isError(sendResult)) {
                System.out.println("[네트워크 오류 발생] 오류 코드 : " + sendResult);
            }
        }
        networkClient1.disconnect();
    }

    private static boolean isError(String connectResult) {
        return !connectResult.equals("success");
    }


}
