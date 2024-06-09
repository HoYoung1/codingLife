package exception.ex2_self;

public class NetworkClientV2_Self {
    private final String address;
    public boolean connectError;
    public boolean sendError;

    public NetworkClientV2_Self(String address) {
        this.address = address;
    }

    public String connect() throws NetworkClientExceptionV2_Self {
        if (connectError) {
            throw new NetworkClientExceptionV2_Self("connectError", address+ " 서버 연결 실패");
        }
        // 연결 성공
        System.out.println(address + " 서버 연결 성공");
        return "success";
    }

    public String send(String data) throws NetworkClientExceptionV2_Self {
        if (sendError) {
            throw new NetworkClientExceptionV2_Self("sendError", address + " 서버에 데이터 전송 실패");
        }
        System.out.println(address + "서버에 데이터 전송" + data);
        return "success";
    }

    public String disconnect() {
        System.out.println(address + "서버 연결 해제");
        return "success";
    }

    public void initError(String data) {
        if (data.contains("error1")) {
            connectError = true;
        }
        if (data.contains("error2")) {
            sendError = true;
        }

    }
}
