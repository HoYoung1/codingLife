package oop1;

public class MusicPlayerMain2 {
    public static void main(String[] args) {

        MusicPlayerData musicPlayerData = new MusicPlayerData();

//        int volume = 0;
//        musicPlayerData.isOn = false;

//        // 음악 플레이어 켜기
//        musicPlayerData.isOn = true;
//        System.out.println("음악 플레이어를 시작합니다");
        on(musicPlayerData);


        // 볼륨 증가
//        volume++;
//        System.out.println("음악 플레이어 볼륨 : " + volume);
        volumeUp(musicPlayerData);

//        volume++;
//        System.out.println("음악 플레이어 볼륨 : " + volume);
        volumeUp(musicPlayerData);

//        volume--;
//        System.out.println("음악 플레이어 볼륨 : " + volume);
        volumeDown(musicPlayerData);


        // 음악 플레이어 상태
        showStatus(musicPlayerData);

        // 음악 플레이어 끄기
//        musicPlayerData.isOn = false;
//        System.out.println("음악 플레이어를 종료합니다");
        off(musicPlayerData);



    }

    private static void showStatus(MusicPlayerData musicPlayerData) {
        System.out.println("음악 플레이어 상태 확인");
        if (musicPlayerData.isOn) {
            System.out.println("음악 플레이어 On, 볼륨 : " + musicPlayerData.volume);
        } else {
            System.out.println("음악 플레이어 Off, 볼륨 : " + musicPlayerData.volume);
        }
    }

    static void on(MusicPlayerData musicPlayerData) {
        musicPlayerData.isOn = true;
        System.out.println("음악 플레이어를 시작합니다");
    }

    static void off(MusicPlayerData musicPlayerData) {
        musicPlayerData.isOn = false;
        System.out.println("음악 플레이어를 종료합니다");
    }

    static void volumeUp(MusicPlayerData musicPlayerData) {
        musicPlayerData.volume++;
        System.out.println("음악 플레이어 볼륨 : " + musicPlayerData.volume);
    }

    static void volumeDown(MusicPlayerData musicPlayerData) {
        musicPlayerData.volume--;
        System.out.println("음악 플레이어 볼륨 : " + musicPlayerData.volume);
    }
}
