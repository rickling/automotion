package tesla

import javax.servlet.http.HttpServletRequest

class Cookies {

    static final String SESSION = "_s_portal_session"
    static final String CREDENTIALS = "user_credentials"

    static checkCookies(HttpServletRequest request) {
        def result = [SESSION, CREDENTIALS].every { cookieName ->
            request.cookies.find { cookie -> cookie.name == cookieName }
        }

        if (!result) {
            throw new AuthorizationException()
        }
    }

}
