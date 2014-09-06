package mocktesla

import grails.converters.JSON
import tesla.ExceptionHandler

import static tesla.Cookies.checkCookies

class VehiclesController extends ExceptionHandler {

    //the id in the url is available by using params.id
    //to disable authentication, remove the checkCookies call from the action

    def vehicles() {
        checkCookies(request)

        def output = [
                [
                        color       : null,
                        display_name: null,
                        id          : 321,
                        option_codes: 'MS01,RENA,TM00,DRLH,PF00,BT85,PBCW,RFPO,WT19,IBMB,IDPB,TR00,SU01,SC01,TP01,AU01,CH00,HP00,PA00,PS00,AD02,X020,X025,X001,X003,X007,X011,X013',
                        user_id     : 123,
                        vehicle_id  : 1234567890,
                        vin         : '5YJSA1CN5CFP01657',
                        tokens      : ['x', 'x'],
                        state       : 'online'
                ]
        ]


        render output as JSON
    }

    def mobile_enabled() {
        checkCookies(request)
        def output = [reason: '', result: true]
        render output as JSON
    }

    def charge_state() {
        checkCookies(request)
        def output = [
            charging_state: "Complete",  // "Charging", ??
            charge_to_max_range: false,  // current std/max-range setting
            max_range_charge_counter: 0,
            fast_charger_present: false, // connected to Supercharger?
            battery_range: 239.02,       // rated miles
            est_battery_range: 155.79,   // range estimated from recent driving
            ideal_battery_range: 275.09, // ideal miles
            battery_level: 91,           // integer charge percentage
            battery_current: -0.6,       // current flowing into battery
            charge_starting_range: null,
            charge_starting_soc: null,
            charger_voltage: 0,          // only has value while charging
            charger_pilot_current: 40,   // max current allowed by charger & adapter
            charger_actual_current: 0,   // current actually being drawn
            charger_power: 0,            // kW (rounded down) of charger
            time_to_full_charge: null,   // valid only while charging
            charge_rate: -1.0,           // float mi/hr charging or -1 if not charging
            charge_port_door_open: true
        ]
        
        render output as JSON
    }

    def climate_state() {
        checkCookies(request)
        def output = [
            inside_temp: 17.0,          // degC inside car
            outside_temp: 9.5,          // degC outside car or null
            driver_temp_setting: 22.6,  // degC of driver temperature setpoint
            passenger_temp_setting: 22.6, // degC of passenger temperature setpoint
            is_auto_conditioning_on: false, // apparently even if on
            is_front_defroster_on: null, // null or boolean as integer?
            is_rear_defroster_on: false,
            fan_status: 0               // fan speed 0-6 or null
        ]
        render output as JSON
    }
    
    def drive_state() {
        checkCookies(request)
        def output = [
            shift_state: null,          //
            speed: null,                //
            latitude: 33.794839,        // degrees N of equator
            longitude: -84.401593,      // degrees W of the prime meridian
            heading: 4,                 // integer compass heading, 0-359
            gps_as_of: 1359863204       // Unix timestamp of GPS fix
        ]
        render output as JSON
    }

    def gui_settings() {
        checkCookies(request)
        def output = [
            gui_distance_units: "mi/hr",
            gui_temperature_units: "F",
            gui_charge_rate_units: "mi/hr",
            gui_24_hour_time: false,
            gui_range_display: "Rated"
        ]
        render output as JSON
    }
    
    def vehicle_state() {
        checkCookies(request)
        def output = [
            df: false,                  // driver's side front door open
            dr: false,                  // driver's side rear door open
            pf: false,                  // passenger's side front door open
            pr: false,                  // passenger's side rear door open
            ft: false,                  // front trunk is open
            rt: false,                  // rear trunk is open
            car_verson: "1.19.42",      // car firmware version
            locked: true,               // car is locked
            sun_roof_installed: false,  // panoramic roof is installed
            sun_roof_state: "unknown",
            sun_roof_percent_open: 0,   // null if not installed
            dark_rims: false,           // gray rims installed
            wheel_type: "Base19",       // wheel type installed
            has_spoiler: false,         // spoiler is installed
            roof_color: "Colored",      // "None" for panoramic roof
            perf_config: "Base"
        ]
        render output as JSON
    }

    def charge_port_door_open() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def charge_standard() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def charge_max_range() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def set_charge_limit() {
        checkCookies(request)
        require("percent is required parameter") {  params.percent }
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def charge_start() {
        checkCookies(request)
        def output = [
            result: false,
            reason: "failure reason" // "already started" if a charge is in progress
        ]
        render output as JSON
    }

    def charge_stop() {
        checkCookies(request)
        def output = [
            result: false,
            reason: "failure reason" // "not_charging" if a charge was not in progress
        ]
        render output as JSON
    }

    def flash_lights() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def honk_horn() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def door_unlock() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def door_lock() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def set_temps() {
        checkCookies(request)
        require("driver_temp is a required parameter") { params.driver_temp} //celsius
        require("passenger_temp is a required parameter") { params.passenger_temp } //celsius
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def air_conditioning_start() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def air_conditioning_stop() {
        checkCookies(request)
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

    def sun_roof_control() {
        checkCookies(request)
        def reqMessage = "state parameter is required: Possible values [open, close, comfort, vent]"
        require(reqMessage) { params.state }
        def output = [result: false, reason: 'failure reason']
        render output as JSON
    }

}
