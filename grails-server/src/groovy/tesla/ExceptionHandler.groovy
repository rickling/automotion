package tesla

import org.codehaus.groovy.runtime.powerassert.PowerAssertionError

class ExceptionHandler {

    def handleAuthorizationException(AuthorizationException e) {
        def message = "Both the ${Cookies.SESSION} and ${Cookies.CREDENTIALS} cookies must be present"
        render status: 401, text: message
    }

    def handleFailedRequirementException(FailedRequirementException e) {
        def message = e.message
        render status: 400, text: message
    }

    def require(String message, Closure closure) {
        if (!closure()) {
            throw new FailedRequirementException(message)
        }
    }
}
