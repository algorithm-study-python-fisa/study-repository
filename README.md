# 알고리즘 및 코딩 테스트 문제 풀이📖

---

## 👩‍👦‍👦 **스터디 멤버**

<table align="center">
 <tr>
   <td align="center"><a href="https://github.com/blueoxygens"><img src="https://avatars.githubusercontent.com/blueoxygens" width="150px;" alt=""></td>
 <td align="center"><a href="https://github.com/ye0ngeun"><img src="https://avatars.githubusercontent.com/ye0ngeun" width="150px;" alt=""></td>
    <td align="center"><a href="https://github.com/Jhcki222"><img src="https://avatars.githubusercontent.com/Jhcki222" width="150px;" alt=""></td>
    <td align="center"><a href="https://github.com/wjddydwns"><img src="https://avatars.githubusercontent.com/wjddydwns" width="150px;" alt=""></td>
   
  </tr>
  <tr>
     <td align="center"><a href="https://github.com/blueoxygens"><b>김현진</b></td>
      <td align="center"><a href="https://github.com/ye0ngeun"><b>이영은</b></td>
    <td align="center"><a href="https://github.com/Jhcki222"><b>이종혁</b></td>
    <td align="center"><a href="https://github.com/wjddydwns"><b>정용준</b></td>
  
  </tr>

</table>

<br />

<br />

## ✅ 스터디 진행 방식과 규칙

### 진행 방식

-   매주 **화요일** 강의 이후 대면 스터디 진행
-   알고리즘은 [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)을 참고하여 진행합니다.
-   스터디마다 선정한 알고리즘의 개념을 공부해오고, 공유합니다. 이전주 알고리즘의 문제를 풀어옵니다.
-   수요일까지 공부한 알고리즘의 문제를 각자 선정해옵니다.
-   해당 알고리즘에 해당하는 문제는 플랫폼 제한없이 자유롭게 선정합니다. (BOJ, 프로그래머스 등..)
-   문제 선정 후, 해당 문제를 포함한 **README를 직접 작성**하고 Slack에 공지
-   화요일까지 각자 브랜치에서 문제 풀이 후, PR 올리기
-   **화요일 스터디 전까지 상대방의 PR에 Code Review를 남기기!**
-   대면 스터디에서 각자 구두로 자신의 코드 리뷰 후, Main 브랜치에 머지합니다.

| 월  |      화       |    수    |     목     | 금  | 토  | 일  |
| :-: | :-----------: | :------: | :--------: | :-: | :-: | :-: |
|     | `과제제출 PR` | `스터디` | `문제공지` |     |     |     |

## ✅ PR code review

### 각자 브랜치 이름은 자유입니다. 파일 및 커밋 규칙만 잘 지켜주세요🙏

#### Pull Request로 리뷰하는 방법

-   [Pull Request 보내는 법](https://inpa.tistory.com/entry/GIT-%E2%9A%A1%EF%B8%8F-%EA%B9%83%ED%97%99-PRPull-Request-%EB%B3%B4%EB%82%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-folk-issue)

```
-   Pull Request 규칙 : [문제출처] 이름 / 주차
-   Ex : [BOJ] 이종혁 / 1주차
```

-   리뷰 방식 - 잘한 것은 과감하게 칭찬하기
-   다른 풀이 방법이 있으면 간단히 소개
-   개선 필요한 부분 구체적으로 설명
    <br />

## ✅ 파일명 규칙

```
-   소스코드 파일 명: [문제 플랫폼] 문제이름_번호(Optional)_난이도
    Ex. boj_1234.java , pgs_베스트엘범.py
```

<br />

## ✅ commit 규칙

-   commit 메세지: **[문제 플랫폼] 이름 / 문제이름 / 걸린시간**
-   description: 문제 주소 (optional)
-   터미널에서 작성법:

```
git commit -m "[PGS] 이종혁 / 베스트앨범 / 30 "
```

-   플랫폼 작성법 통일:
    -   [BOJ] - 백준
    -   [PGS] - 프로그래머스
    -   [LTC] - 리트코드
    -   [CFS] - 코드포스
    -   [SEA] - 삼성SW Expert Academy
    -   [ETC] - 그외

<br />

## ✅ 디렉토리 구조

```
├── 📂 jonghyuck
|      ├── 📂 [week1]구현
       │    ├── 💾  boj_2346_실버3.py
       │    ├── 💾  pgs_올바른 괄호.py
       ├── 📂 [week2]자료구조2
       │    ├── 💾boj ....py
       │    ├── 💾pgs ....py
       └── 📂 [Week 3]트리
       │
├── 📂 yeoungeun
...
|

💾README.md
```

## ✅ 문제 리스트

**[ 문제 선정 ]**

> 문제는 [Solved.ac](https://solved.ac/), [코딩테스트 대비 문제집](https://github.com/tony9402/baekjoon) 및 [프로그래머스](https://programmers.co.kr/)를 참고한다.

| 주차  | 스터디 날짜  | 기출 유형 | 문제명                                                                                                                                                                                                                      |
| ----- | ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Week1 | 25.09.23(OT) | 구현      | [소가 길을 건너간 이유1](https://www.acmicpc.net/problem/14467)<br />[키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256)<br />[체스판 다시 칠하기](https://www.acmicpc.net/problem/1018)<br /> |
