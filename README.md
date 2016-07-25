**장고의 MVC**

장고는 MVC(Model - View - Controller) 라는 패턴을 사용한다.  
MVC 패턴을 이용하면 사용자의 인터페이스와 내부의 로직을 분리할 수 있고  
이를 통해서 쉽게 고칠 수 있는 앱을 만들 수 있다고 한다.  
모델은 앱의 정보를 나타내고, 뷰는 사용자 인터페이스, 컨트롤러는 데이터와 로직간의  
동작을 관리한다.  

장고에는 어떻게 MVC 패턴을 사용하고 있을까?  

웹서버로서 장고가 하는 일은 당연하게도 '유저가 보낸 URL에 대해서 어떤 동작을 할 것인지를 결정하는 것' 이다.  
이 작업을 장고는 다음과 같이 처리한다.  
1.HTTP request가 특정 URL에 대해서 들어온다  (사용자 인터페이스)
2.View 함수들중 어떤 함수가 request를 처리 할지를 장고가 결정한다.( = resolving the URL)  
3.view 함수가 request를 처리하고 HTTP response를 반환한다.

즉 장고에서는 View가 반환된 HTTP(인터페이스)뿐만 아니라 어떤 HTTP(data)를 보여줄지 도 결정한다.  
그렇다면 controller는 어디에 있는걸까? 장고의 경우 장고라는 framework 자체가 controller의 역할을 한다.url에 따라 request를 알맞은 view에 보내는 역할..  
=> urls.py에서 url을 보고 알맞은 view로 연결한다.  
Model은 template인가?  



4장에서 보이는 functional_test와 unit test의 차이  

functional test에서는 browser를 url을 통해 받고 그 browser에 대해서 element들을 찾아내는 함수를 사용한다. 여기서는 얻어진 element인 inputbox에 대해서 마찬가지로 input box의 함수인
