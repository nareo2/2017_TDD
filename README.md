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



**(4장에서 알게된) functional_test와 unit test의 차이**

```python
def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        inputbox = self.browser.find_element_by_id('id_new_item')

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

```
functional test는 '사용자가 하는 행동을 직접 해보고' 에러가 있는지 찾는 방식이다.
functional test에서는 url을 통해 browser(html 정보를 클래스화 한 것?)를 받고 browser의 element들을 얻는 함수를 사용한다.  
그렇게 얻어진 iinput box의 함수인 send_keys를 이용해서 input box에 값을 넣는다.  
유저가 input box에 값을 써 넣고 엔터를 누르는 과정을 코드로 짠것이다.  
이 예제에서는 어떤 경우가 에러일까? to-do 리스트를 만드는게 목적이므로 input box에 값을 넣었지만 리스트에 추가가 되지 않는 경우가 에러일 것이다. 에러인지는 talbe에 넣어준 값이 있는가로 판단한다.
input box -> table 내부 구현에 관계 없이 html(?)과 관련된 함수만 이용해서 에러가 있는지를 판단하는것!  

그렇다면 unit test에서는?  

```python
def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
```

functional test에서 url을 통해 얻은? home.html을 직접 home_page라는 클래스의 생성자로 request를 넘겨주면서 얻고 이를 직접 home.html과 비교하고 있다. 유저가 이렇게 할 것이다가 아니라 'home_page(request)'라는 생성자가 내가 원하는 대로 home.html이라는 string을 반환하는지를 테스트 하기 위한것!
