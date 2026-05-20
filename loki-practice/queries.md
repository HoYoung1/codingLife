# LogQL 실습 쿼리 모음

Grafana → Explore → Loki 데이터소스 선택 후 아래 쿼리를 입력하세요.

---

## 1단계: 기본 스트림 조회

```logql
{job="myapp"}
```
> myapp 전체 로그 스트림을 시간 역순으로 봅니다.

```logql
{job="myapp", env="local"}
```
> 라벨을 2개 조합해 필터링합니다.

---

## 2단계: 레벨 필터 (라벨 기반)

Alloy의 `stage.regex` + `stage.labels`가 `level` 라벨을 추출했기 때문에 라벨로 필터링 가능합니다.

```logql
{job="myapp", level="ERROR"}
```
```logql
{job="myapp", level="WARN"}
```
```logql
{job="myapp", level="INFO"}
```

---

## 3단계: 키워드 검색 (파이프 필터)

```logql
{job="myapp"} |= "timeout"
```
> 로그 라인에 "timeout" 문자열이 포함된 것만 필터링합니다.

```logql
{job="myapp"} |= "ERROR" != "Auth"
```
> ERROR를 포함하지만 "Auth"는 제외합니다.

```logql
{job="myapp"} |~ "user_id=[1-9][0-9]{2}"
```
> 정규식으로 user_id가 100 이상인 로그만 조회합니다.

---

## 4단계: 메트릭 쿼리 (레이트)

```logql
rate({job="myapp"}[1m])
```
> 전체 로그의 초당 라인 수 (1분 구간).

```logql
rate({job="myapp", level="ERROR"}[1m])
```
> ERROR 로그의 초당 발생 수.

---

## 5단계: 집계

```logql
sum by (level) (rate({job="myapp"}[1m]))
```
> 레벨별 초당 로그 수를 시계열로 비교합니다.

```logql
sum(count_over_time({job="myapp", level="ERROR"}[5m]))
```
> 최근 5분 동안 발생한 ERROR 총 건수.

---

## 6단계: 알림 룰 쿼리

Grafana Alerting → New alert rule 에서 아래 쿼리를 사용하세요.

```logql
sum(rate({job="myapp", level="ERROR"}[5m])) > 0.1
```
- **조건**: 5분 평균 ERROR 발생률이 0.1/s 초과 시 (약 30초에 ERROR 3건)
- **For**: 1m (1분 지속 시 Firing)
- **알림 채널**: Grafana 내장 이메일 or Webhook

```logql
sum(count_over_time({job="myapp", level="ERROR"}[1m])) > 5
```
- 1분 안에 ERROR가 5건을 넘으면 즉시 알림

---

## 참고: Grafana 데이터소스 설정

1. Grafana `http://localhost:3000` 접속 (admin / admin)
2. **Connections** → **Data sources** → **Add new data source** → **Loki**
3. URL: `http://localhost:3100`
4. **Save & test** 클릭 → "Data source successfully connected" 확인
