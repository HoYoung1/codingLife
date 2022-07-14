package chapter7tocaller.chapter7;

import java.time.LocalDateTime;

public class Photo {
    public String title;
    public String location;
    public LocalDateTime date;

    public Photo() {
        title = "photo title";
        location = "photo location";
        date = LocalDateTime.now();
    }
}
