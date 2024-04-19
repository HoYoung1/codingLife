package enumeration.test.http;

public enum HttpStatus {
    OK(200,"OK"),
    BAD_REQUEST(400, "BAD REQUEST"),
    NOT_FOUND(404, "NOT FOUND"),
    INTERNAL_SERVER_ERROR(500, "Internal Server Error");

    HttpStatus(int statusCode, String message) {
        this.code = statusCode;
        this.message = message;
    }

    private final int code;
    private final String message;

    public static HttpStatus findByCode(int statusCode) {
        HttpStatus[] values = HttpStatus.values();
        for (HttpStatus value : values) {
            if (value.code == statusCode) {
                return value;
            }
        }
        return null;
    }

    public int getCode() {
        return code;
    }

    public String getMessage() {
        return message;
    }

    public boolean isSuccess() {
        return this.code >= 200 && this.code < 300;
    }

}
