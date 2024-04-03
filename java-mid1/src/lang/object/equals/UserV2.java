package lang.object.equals;

import java.util.Objects;

public class UserV2 {
    private String id;

    public UserV2(String id) {
        this.id = id;
    }

    public String getId() {
        return id;
    }

//    @Override
//    public boolean equals(Object obj) {
//        if (obj instanceof UserV2 userV2)
//            return this.id.equals(userV2.getId());
//        return false;
//    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        UserV2 userV2 = (UserV2) o;
        return Objects.equals(id, userV2.id);
    }

}
