package access;

import class1.Student;

public class Speaker {
    private int volume;

    Speaker(int volume) {
        this.volume = volume;
    }

    void volumeUp() {
        if (volume >= 100) {
            System.out.println("음량 증가는 안됩니다. 최대 음량입니다");
        } else {
            volume += 10;
            System.out.println("음량을 10 증가시킵니다");
        }

    }

    void volumeDown() {
        volume -= 10;
        System.out.println("볼륨 다운 호출");
    }

    void showVolume() {
        System.out.println("현재 볼륨 : " + volume);
    }




}
