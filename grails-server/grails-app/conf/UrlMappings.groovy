class UrlMappings {

	static mappings = {

        "/vehicles/$id/mobile_enabled"(controller: 'vehicles', action: 'mobile_enabled')
        "/vehicles/$id/command/$action"(controller: 'vehicles')

        "/vehicles"(controller: 'vehicles', action: 'vehicles')

        "/$controller/$action?/$id?(.$format)?"{
            constraints {
                // apply constraints here
            }
        }

        "/"(view:"/index")
        "500"(view:'/error')
	}
}
