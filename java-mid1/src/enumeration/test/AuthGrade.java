package enumeration.test;

import java.util.Arrays;
import java.util.stream.Stream;

public enum AuthGrade {
    GUEST(1, "손님", new String[]{"메인 화면"})
    , LOGIN(2, "로그인 회원", new String[]{"이메일 관리 화면"})
    , ADMIN(3, "관리자", new String[]{"관리자 화면"})
    ;

    private final int level;
    private final String description;
    private final String[] accessibleMenu;

    AuthGrade(int level, String description, String[] accessibleMenu) {
        this.level = level;
        this.description = description;
        this.accessibleMenu = accessibleMenu;
    }


    public int getLevel() {
        return level;
    }

    public String getDescription() {
        return description;
    }



    public String[] getAccessibleMenu() {
        if (this == LOGIN) {
//            return new String[]{GUEST.accessibleMenu, LOGIN.getDescription()};
            return Stream.concat(Arrays.stream(GUEST.accessibleMenu), Arrays.stream(LOGIN.accessibleMenu)).toArray(String[]::new);
        } else if (this == ADMIN) {
            return Stream.concat(Arrays.stream(LOGIN.getAccessibleMenu()), Arrays.stream(ADMIN.accessibleMenu)).toArray(String[]::new);
        }
        return new String[]{this.getDescription()};
    }
}
