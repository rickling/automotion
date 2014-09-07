################################################################################################
#  ___  ___ _   _            _          _____         _        ___  ___      _   _             #
# |  \/  || | | |          | |        |_   _|       | |       |  \/  |     | | (_)             #
# | .  . || |_| | __ _  ___| | _____    | | ___  ___| | __ _  | .  . | ___ | |_ _  ___  _ __   #
# | |\/| ||  _  |/ _` |/ __| |/ / __|   | |/ _ \/ __| |/ _` | | |\/| |/ _ \| __| |/ _ \| '_ \  #
# | |  | || | | | (_| | (__|   <\__ \   | |  __/\__ \ | (_| | | |  | | (_) | |_| | (_) | | | | #
# \_|  |_/\_| |_/\__,_|\___|_|\_\___/   \_/\___||___/_|\__,_| \_|  |_/\___/ \__|_|\___/|_| |_| #
################################################################################################
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
lib_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, lib_dir)
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from tesla_vocalizer import TeslaVocalizer
from twilio_vocalizer import TwilioVocalizer
import bloomberg_vocalizer
from math import sqrt
import time
import datetime
from datetime import timedelta

from websocket import create_connection

RDIO_PLAY_PAUSE = "0"
RDIO_NEXT = "1"
RDIO_PREV = "2"
RDIO_VOL_UP = "3"
RDIO_VOL_DOWN = "4"

def do_nothing():
    pass

def magnitude(vector):
    return sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"
        self.tesla = TeslaVocalizer(is_local=False)
        self.twilio = TwilioVocalizer()

        self.TAP_GESTURES = {
            Leap.Finger.TYPE_THUMB : self.tesla.honk_horn,
            Leap.Finger.TYPE_INDEX : self.tesla.lock_door,
            Leap.Finger.TYPE_MIDDLE : self.tesla.unlock_door,
            Leap.Finger.TYPE_RING : self.tesla.flash_lights,
            Leap.Finger.TYPE_PINKY : self.tesla.honk_horn,
        }

        self.ws = create_connection("ws://localhost:9000")

        self.lastAction = datetime.datetime.now()

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.config.set("Gesture.Circle.MinRadius", 30.0)
        controller.config.set("Gesture.Circle.MinArc", 1.5)
        controller.config.set("Gesture.KeyTap.MinDistance", 10.0)
        controller.config.save()

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # Debug for frames
        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
        #  frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            # print handType + " detected"

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction
            pp = hand.palm_position

            ## STOCKS
            if hand.grab_strength > 0.9 and magnitude(hand.palm_velocity) < 40:
                for finger in hand.fingers:
                    if finger.type() == Leap.Finger.TYPE_THUMB:
                        if finger.direction[0] < -0.9:
                            print "Stocks detected"
                            bloomberg_vocalizer.main()

            """

            MIDDLE_F = False
            INDEX_F = False
            if direction[1] < -0.8 and normal[2] > 0.8:
                for finger in hand.fingers:
                    if finger.type() == Leap.Finger.TYPE_MIDDLE:
                        if finger.direction[1] < -0.8:
                            MIDDLE_F = True
                        #print finger.direction
                        # print finger.stabilized_tip_position
                        #print magnitude(finger.stabilized_tip_position - pp)
                    if finger.type() == Leap.Finger.TYPE_INDEX:
                        if finger.direction[1] > 0.3:
                            #print finger.direction

            """
            

            # Get arm bone
            arm = hand.arm

            #Phone call
            PINKY = False
            THUMB = False
            for finger in hand.fingers:
                if finger.type() == Leap.Finger.TYPE_PINKY:
                    if finger.direction[0] < -0.75:
                        PINKY = True
                elif finger.type() == Leap.Finger.TYPE_THUMB:
                    if finger.direction[1] > 0.75:
                        THUMB = True
            if PINKY and THUMB and magnitude(hand.palm_velocity) < 60:
                if datetime.datetime.now() > self.lastAction + timedelta(seconds=2):
                    print "Making a call"
                    self.twilio.vocalize("calling", "+14695855530")
                    self.lastAction = datetime.datetime.now()


            """
            # Get fingers
            for finger in hand.fingers:

                # print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                #     self.finger_names[finger.type()],
                #     finger.id,
                #     finger.length,
                #     finger.width)

                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    # print "      Bone: %s, start: %s, end: %s, direction: %s" % (
                    #     self.bone_names[bone.type],
                    #     bone.prev_joint,
                    #     bone.next_joint,
                    #     bone.direction)
            """

        # Get tools
        for tool in frame.tools:

            print "  Tool id: %d, position: %s, direction: %s" % (
                tool.id, tool.tip_position, tool.direction)

        # Get gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counterclockwise"

                if circle.progress > 1.0:
                    if datetime.datetime.now() > self.lastAction + timedelta(milliseconds=250):
                        if clockwiseness == "clockwise":
                            self.ws.send(RDIO_VOL_UP)
                        else:
                            self.ws.send(RDIO_VOL_DOWN)
                        self.lastAction = datetime.datetime.now()
                        print clockwiseness

                # Calculate the angle swept since the last frame
                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI


            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                #print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                #       gesture.id, self.state_names[gesture.state],
                #      swipe.position, swipe.direction, swipe.speed)
                
                #Sunroof Control
                if datetime.datetime.now() > self.lastAction + timedelta(seconds=2):
                    if swipe.direction[1] > 0.9:
                        print "opening sunroof"
                        self.tesla.open_sun_roof()
                    elif swipe.direction[1] < -0.9:
                        print "closing sunroof"
                        self.tesla.close_sun_roof()
                    elif swipe.direction[2] < -0.9:
                        print "Play/Pause"
                        self.ws.send(RDIO_PLAY_PAUSE)
                    elif swipe.direction[0] > 0.9:
                        print "Next Song"
                        self.ws.send(RDIO_NEXT)
                    elif swipe.direction[0] < -0.9:
                        print "Prev Song"
                        self.ws.send(RDIO_PREV)
                    self.lastAction = datetime.datetime.now()

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                tap = Leap.KeyTapGesture(gesture)
                print "tap detected"

                if tap.pointable.is_finger:
                    if datetime.datetime.now() > self.lastAction + timedelta(seconds=2):
                        finger = Leap.Finger(tap.pointable)
                        self.TAP_GESTURES[finger.type()]()
                        self.lastAction = datetime.datetime.now()


    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
