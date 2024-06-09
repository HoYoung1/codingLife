package exception.ex2_self;

public class NetworkClientExceptionV2_Self extends Exception {
    private String errorCode;

    public NetworkClientExceptionV2_Self(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
