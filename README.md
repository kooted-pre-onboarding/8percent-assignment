![header](https://capsule-render.vercel.app/api?type=Slice&color=auto&height=350&section=header&text=%20%208PERCENT&fontSize=90&textBg=true)

<br/>
<br>


# 원티드x위코드 백엔드 프리온보딩 과제 4.

<br>

> ## [Assignment] 과제 제출 기업정보

 <br>

  - 기업명 : 8PERCENT

  - [8percent 웹사이트 링크](https://8percent.kr/)

  - [원티드 채용공고 링크](https://www.wanted.co.kr/wd/64695)

<br>
<br>
<br>

> ## Members

<br>

|이름   |Github                   |담당 기능|
|-------|-------------------------|--------------------|
|👨🏻‍🎤 김주현 |[kjhabc2002](https://github.com/kjhabc2002) | DB data control, DB load test, AWS / Docker 배포 |
|👰🏻‍♂️ 이다빈 |[thisisempty](https://github.com/thisisempty)     | DB data control, DB load test, AWS / Docker 배포 |
|👶🏻 구본욱 |[qhsdnr0](https://github.com/qhsdnr0)   | DB data control, DB load test, AWS / Docker 배포 |
|🥷 김지훈  |[kimfa123](https://github.com/kimfa123) | 입금/출금 view, unit test, README 작성|
|🦹🏻‍♂️ 문승준 |[palza4dev](https://github.com/palza4dev)     | 거래내역 view, unit test, postman api, README 작성 |
|👨🏻‍🦳 양가현 |[chrisyang256](https://github.com/chrisyang256)   | 회원가입/로그인 view, unit test, README 작성 |

ㅤ👪 공동작업: DB Modeling

<br>
<br>
<br>


> ## 사용 기술
<br>

<div align="center">

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)ㅤ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)ㅤ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)ㅤ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)ㅤ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)ㅤ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)ㅤ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

</div>

<br>
<br>
<br>

> ## 과제 내용

<br>

ㅤ아래 요구사항에 맞춰 상품관리 Restfull API를 개발합니다.

<br>

### ▶︎ 필수 포함사항
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

<br>

### ▶︎ 개발 요구사항

✔️ API 목록
- 거래내역 조회 API
- 입금 API
- 출금 API

<br>

**✔️ 주요 고려 사항은 다음과 같습니다.**
- 계좌의 잔액을 별도로 관리해야 하며, 계좌의 잔액과 거래내역의 잔액의 무결성의 보장
- DB를 설계 할때 각 칼럼의 타입과 제약

<br>

**✔️ 구현하지 않아도 되는 부분은 다음과 같습니다.**
- 문제와 관련되지 않은 부가적인 정보. 예를 들어 사용자 테이블의 이메일, 주소, 성별 등
- 프론트앤드 관련 부분

<br>

**✔️  제약사항은 다음과 같습니다.**
- (**8퍼센트가 직접 로컬에서 실행하여 테스트를 원하는 경우를 위해**) 테스트의 편의성을 위해 mysql, postgresql 대신 sqllite를 사용해 주세요.

<br>

**✔️  거래내역 조회 API**

- 아래와 같은 조회 화면에서 사용되는 API를 고려하시면 됩니다.
  
    ![image 0](https://user-images.githubusercontent.com/89192083/141446102-f1b6d870-a4c4-4b57-9052-e4f17d470f9c.png)
    

<br>

**✔️  거래내역 API는 다음을 만족해야 합니다.**

- 계좌의 소유주만 요청 할 수 있어야 합니다.
- 거래일시에 대한 필터링이 가능해야 합니다.
- 출금, 입금만 선택해서 필터링을 할 수 있어야 합니다.
- Pagination이 필요 합니다.
- 다음 사항이 응답에 포함되어야 합니다.
    - 거래일시
    - 거래금액
    - 잔액
    - 거래종류 (출금/입금)
    - 적요

<br>

**✔️  입금 API**
- 계좌의 소유주만 요청 할 수 있어야 합니다.

<br>

**✔️  출금 API**
- 계좌의 소유주만 요청 할 수 있어야 합니다.
- 계좌의 잔액내에서만 출금 할 수 있어야 합니다. 잔액을 넘어선 출금 요청에 대해서는 적절한 에러처리가 되어야 합니다.

<br>

**✔️  구현 시 가산점 부여 사항**
- Unit test의 구현
- Functional Test 의 구현 (입금, 조회, 출금에 대한 시나리오 테스트)
- 거래내역이 1억건을 넘어갈 때에 대한 고려
    - 이를 고려하여 어떤 설계를 추가하셨는지를 README에 남겨 주세요.

<br/>
<br/>
<br/>

> ## 모델링

<br/>

<div align="center">

![스크린샷 2021-11-12 오후 6 41 39](https://user-images.githubusercontent.com/89192083/141445866-5177cdd3-0f92-46bc-83b7-99e17548aaf3.png)

</div>

<br/>
<br/>
<br>


> ## 구현 기능

<br>

### ▶︎ 회원가입/로그인
- 신규 회원가입과 동시에 계좌가 개설되도록 설계하였습니다.
- 이에 따라 회원가입 시 users, account table에 각각 동시에 row가 입력되며 account table이 생성되지 않을 경우를 고려하여 transaction 처리를 하였습니다.
- 회원가입 시 유일한 수로 이루어진 고유 계좌번호 부여
  - account_number 함수에서 생성된 계좌번호는 생성 후 즉시 리턴되지 않습니다.
  - Account table을 조회하여 동일한 값의 계좌번호가 존재하지 않을 때 까지 재귀함수를 통해 생성/조회를 반복한 후 값을 최종 리턴하므로 계좌번호의 중복을 차단하도록 구현하였습니다.

```python
def account_number():
    def numbers():
        number = random.randint(1000, 9999)
        return number

    account_number = f'{numbers()}-{numbers()}-{numbers()}-{numbers()}'
    
    if not Account.objects.filter(number=account_number).exists():
        return account_number

    return account_number()

# 리턴값 예시: '9197-6853-7204-1115'
```

<br>

### ▶︎ 입금/출금

- 입금 API는 decorator를 이용하여 계좌를 개설한 로그인 유저만 요청 할수 있게 구현 하였습니다. 
- 0원 이상만 이상으로만 입금 하게 구현 하였습니다.

```python
if data["amount"] <= 0:
 return JsonResponse({"message" : "INVALID_INPUT"}, status=400)
```

- 출금 API 역시 decorator를 이용한 계좌를 가진 로그인 유저만 요청 할수 있게 구현 하였습니다.

- 0원 이상 출금 할수 있으며 잔액 보다 많은 금액을 출금 할 수 없게 구현하였습니다.

```python
if data[“amount”] <= 0:

	return JsonResponse({“message”: “INVALID_INPUT”}, status=400)

if data”["amount"] > account.balance:
s
	return JsonR“sponse(”"m“ssage": "WRON”_REQUEST"}, status=400)

```
- 메소드 전체가 아닌 메소드의 일부분만 처리할수 있게 입금 출금 기능을 트랜잭션으로 묶어 주었습니다.

```python
with transaction.atomic():
  account.balance += data["amount"]
  account.save()
  
with transaction.atomic():
  account.balance -= data["amount"]
  account.save()
```

<br>

### ▶︎ 거래내역
- 모든 필터링 파라미터는 GET 요청의 쿼리 스트링을 사용합니다.
- 거래일시에 대한 필터링을 위해 start-date와 end-date 값이 필요합니다.
- 최신순, 과거순 정렬을 위해 order 값이 필요합니다. 
- 거래종류는 type 값으로 지정할 수 있으며 기본값은 전체입니다.
- 페이지네이션을 적용하였으며 100 이상의 limit을 요청하면 에러를 반환합니다.
- 검색 시작일과 종료일이 동일하면 해당일 하루 동안의 거래내역을 필터링하기 위해 아래와 같이 `timedelta(days=1)` 을 더해주었습니다.

```python
...
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date   = datetime.strptime(end_date, '%Y-%m-%d')
            
if end_date < start_date:
    return JsonResponse({"message":"INVALID_DATE_RANGE"}, status=400)
            
if (start_date == end_date):
    end_date += timedelta(days=1)

q &= Q(created_at__range=(start_date, end_date))
```

<br>

### ▶︎ 설치 및 실행 방법
#### - Local 개발 및 테스트 용
1. 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동한다.
```shell
git clone https://github.com/kooted-pre-onboarding/8percent-assignment.git
cd 8percent-assignment
```

2. 가상 환경을 생성하고 프로젝트에 사용한 python package를 설치한다
```shell
conda create -n "8percent" python=3.8
conda activate 8percent
```

3. docker 환경 설정 파일을 생성하고 다음을 작성한다.
```shell
touch .env
vi .env
```
``` env
EIGHTPERCENT_SECRET_KEY=SECRET_KEY
EIGHTPERCENT_ALGORITHM=HS256
```

4. 다음 명령어로 서버를 실행시킨다
```shell
docker-compose -f docker-compose.yml up 
```

4-1. 백그라운드로 실행하고싶을 시 `-d`옵션을 추가한다.
``` shell
docker-compose -f docker-compose.yml up -d
```

#### - 배포용

1. 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동한다.
```shell
git clone https://github.com/kooted-pre-onboarding/8percent-assignment.git
cd 8percent-assignment
```

2. 가상 환경을 생성하고 프로젝트에 사용한 python package를 설치한다
```shell
conda create -n "8percent" python=3.8
conda activate 8percent
```

3. docker 환경 설정 파일을 생성하고 다음을 작성한다. 
```shell
touch .env
vi .env
```

``` env
EIGHTPERCENT_SECRET_KEY=SECRET_KEY
EIGHTPERCENT_ALGORITHM=HS256
```

4. 다음 명령어로 서버를 실행시킨다
```shell
sudo docker-compse -f docker-compose-deploy.yml up
```

4-1. 백그라운드로 실행하고싶을 시 `-d`옵션을 추가한다.
```shell
sudo docker-compse -f docker-compose-deploy.yml up -d
```

<br>
<br>
<br>

### ▶︎ 거래 내역이 1억건을 넘어갈 때에 대한 고려
- 저희는 대량 데이터 처리 시 데이터 조회를 문제요소로 판단하여 문제 해결을 위한 방법으로 `Database indexing`을 활용하고자 하였습니다.
``` python
class Transaction(models.Model):
    amount                    = models.PositiveIntegerField()
    balance_after_transaction = models.PositiveIntegerField()
    sum_up                    = models.CharField(max_length=100)
    account                   = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type          = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    created_at                = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transactions'
        indexes = [
            models.Index(fields=['account_id'])
        ]
```
- 하지만 테스트 결과 `pagination`만으로도 조회 성능에는 문제가 되지 않는 상황이라고 판단하였습니다.
- 시행착오 끝에 저희가 내린 결론은 한 테이블에 너무 많은 데이터가 누적되는 것이 문제라고 판단하였습니다.
- 결론적으로 구현한 사항은 아니지만 "`database table partitioning`을 활용한 방안이 더 적합하지 않았을까?" 라는 결론을 내렸습니다.

테스트 결과는 [Postman loadtest 문서 링크](https://documenter.getpostman.com/view/18218753/UVC2H9Er)에서 확인 가능합니다.


> ## API Document & Test

<br>

1. [Postman API 문서 링크](https://documenter.getpostman.com/view/17676214/UVC8BkkC)로  접속해 우측 상단의 `Run in Postman` 버튼을 클릭합니다.
2. 개인 Workspace로 Import 합니다.

3. hostname 환경변수를 deploy로 선택합니다.

4. 배포 주소 `13.125.45.93:8000` 를 확인합니다.
5. API 문서 예시를 참고해 Request를 보냅니다.

<br/>
<br>
<br>

> ## 폴더 구조

<br>

```bash

├── __pycache__
├── accounts
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── dbuploader.py
├── deploy.Dockerfile
├── docker-compose-deploy.yml
├── docker-compose.yml
├── eightpercent
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── local.Dockerfile
├── manage.py
├── pull_request_template.md
├── requirements.txt
└── transactions
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

<br/>
<br/>
<br/>

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 8percent에서 출제한 과제를 기반으로 만들었습니다. 
    
