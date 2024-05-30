#1 top 명령어는 리눅스와 유닉스 기반 시스템에서 사용되는 유틸리티 중 하나로, 시스템의 현재 상태를 모니터링하고 프로세스의 활동을 실시간으로 확인하는 데 사용됩니다. 주로 시스템 리소스 사용량을 파악하거나 프로세스들의 실행 상태를 추적할 때 유용합니다. 일반적으로 top 명령어를 실행하면 CPU 사용량, 메모리 사용량, 스왑 메모리 사용량, 프로세스 수 등 시스템의 기본적인 정보를 화면에 표시합니다. 또한 프로세스들을 CPU 사용량이나 메모리 사용량 등의 기준으로 정렬하여 보여줍니다.
top 명령어를 사용하면서 몇 가지 유용한 키 조합을 사용할 수 있습니다. 일반적으로 사용되는 몇 가지 키는 다음과 같습니다.
예시:
q: top 명령어를 종료합니다.
Space: 화면을 새로 고침합니다.
k: 프로세스를 종료합니다. 종료할 프로세스의 PID를 입력하라는 프롬프트가 나타납니다.
u: 특정 사용자가 시작한 프로세스만 표시합니다. 사용자 이름을 입력하라는 프롬프트가 나타납니다.
M: 메모리 사용량에 따라 프로세스를 정렬합니다.
P: CPU 사용량에 따라 프로세스를 정렬합니다.
T: 프로세스가 실행한 시간에 따라 정렬합니다.
이 외에도 다양한 옵션이 있으며, man top 명령어를 사용하여 자세한 정보를 얻을 수 있습니다.

지금부터는 top 명령어의 디테일 영역에 대해서 알아보도록 하겠습니다. 디테일 영역에는 각 프로세스에 대한 상세한 내용이 나옵니다. 아래의 이미지 부분이 디테일 부분인데요, 각 요소에 대해서 하나씩 보도록하겠습니다.


