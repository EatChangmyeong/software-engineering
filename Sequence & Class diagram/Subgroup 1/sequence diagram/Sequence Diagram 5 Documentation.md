# 요구사항 5에 대한 시퀀스 다이어그램

현재 `sequence diagram` 폴더에는 요구사항 5에 대한 시퀀스 다이어그램이 3개 있으며, 각각 다음과 같다.

* `Sequence Diagram 5 (deprecated).drawio`: 초기에 작성한 시퀀스 다이어그램 (이하 버전 1)
* `Sequence Diagram 5 alt1.drawio`: `PasswordChecker`의 역할을 `Controller`로 통합한 시퀀스 다이어그램 (이하 버전 2)
* `Sequence Diagram 1+5.drawio`: 버전 1을 기반으로 요구사항 1과 4의 일부 내용을 통합한 최종 다이어그램

버전 1에서는 `PasswordChecker` 개념이 존재해 패스워드 일치 여부를 확인하는 기능을 전담하지만, 버전 2에서는 이 개념이 `Controller`로 통합되었다. 각각의 장단점은 다음과 같다.

* `PasswordChecker`가 별도로 존재할 경우 (버전 1)
	* `Controller`가 패스워드 일치 여부를 확인하지 않으므로 관심사가 분리된다.
	* 패스워드 확인 기능의 재사용이 가능하다.
* `PasswordChecker`가 존재하지 않을 경우 (버전 2)
	* 함수 호출 체인이 짧아진다.
	* `PasswordChecker`에 의존하는 대신 `PasswordStorage`에 직접 의존하므로 `Controller`의 연결성은 늘어나지 않는다.

여기에서는 버전 2를 채택할 경우에 비해 버전 1을 채택할 경우의 장점이 명확하다고 판단하여 버전 1의 설계를 채택하였다.