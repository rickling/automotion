package mocktesla

import tesla.Cookies

import javax.servlet.http.Cookie

class LoginController {

    def index() {
        String email = params["user_session[email]"]
        String password = params["user_session[password]"]

        response.addCookie(cookie(Cookies.SESSION, "true"))
        response.addCookie(cookie(Cookies.CREDENTIALS, email))

        render text: "Dummy welcome page"
    }


    private static cookie(String name, String value) {
        def cookie = new Cookie(name, value)
        cookie.path = "/"
        cookie
    }

}
