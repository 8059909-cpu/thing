from enum import Enum  
from dataclasses import dataclass  
from typing import Dict, List, Optional, Callable  
import random  
import math  

class Animatronic(Enum):  
    TOY_FREDDY = "Toy Freddy"  
    TOY_BONNIE = "Toy Bonnie"  
    TOY_CHICA = "Toy Chica"  
    MANGLE = "Mangle"  
    BALLOON_BOY = "Balloon Boy"  
    PUPPET = "Puppet"  
    GOLDEN_FREDDY = "Golden Freddy"  
    WITHERED_FREDDY = "Withered Freddy"  
    WITHERED_BONNIE = "Withered Bonnie"  
    WITHERED_CHICA = "Withered Chica"  
    WITHERED_FOXY = "Withered Foxy"

@dataclass  
class JumpscareEvent:  
    animatronic: Animatronic  
    screen_effect: str  
    audio_clip: str  
    callback: Optional[Callable] = None

class JumpscareManager:  
    def __init__(self):  
        self.jumpscare_events: Dict[Animatronic, JumpscareEvent] = {}  

    def register_jumpscare(self, animatronic: Animatronic, screen_effect: str, audio_clip: str, callback: Optional[Callable] = None):  
        self.jumpscare_events[animatronic] = JumpscareEvent(animatronic, screen_effect, audio_clip, callback)

    def trigger_jumpscare(self, animatronic: Animatronic):  
        if animatronic in self.jumpscare_events:  
            event = self.jumpscare_events[animatronic]  
            print(f"Triggering jumpscare from {event.animatronic.value}")  
            print(f"Displaying effect: {event.screen_effect}")  
            print(f"Playing audio: {event.audio_clip}")  
            if event.callback:  
                event.callback()  
        else:  
            print("No jumpscare registered for this animatronic.")  

    def random_jumpscare(self):  
        animatronics = list(self.jumpscare_events.keys())  
        chosen_animatronic = random.choice(animatronics)  
        self.trigger_jumpscare(chosen_animatronic)  

# Example of usage  

jumpscare_manager = JumpscareManager()  

# Register jumpscares  
jumpscare_manager.register_jumpscare(Animatronic.TOY_FREDDY, "flash", "scary_sound.mp3")  
jumpscare_manager.register_jumpscare(Animatronic.TOY_BONNIE, "fade", "scream.wav")  
jumpscare_manager.register_jumpscare(Animatronic.TOY_CHICA, "shake", "jump scare.mp3")  
jumpscare_manager.register_jumpscare(Animatronic.MANGLE, "static", "mangle.wav")  
jumpscare_manager.register_jumpscare(Animatronic.BALLOON_BOY, "invert", "balloon_boy.mp3")  
jumpscare_manager.register_jumpscare(Animatronic.PUPPET, "blackout", "puppet.wav")  
jumpscare_manager.register_jumpscare(Animatronic.GOLDEN_FREDDY, "blur", "golden_freddy.mp3")  
jumpscare_manager.register_jumpscare(Animatronic.WITHERED_FREDDY, "pulse", "withered_freddy.wav")  
jumpscare_manager.register_jumpscare(Animatronic.WITHERED_BONNIE, "zoom", "withered_bonnie.mp3")  
jumpscare_manager.register_jumpscare(Animatronic.WITHERED_CHICA, "flash", "withered_chica.wav")  
jumpscare_manager.register_jumpscare(Animatronic.WITHERED_FOXY, "shake", "withered_foxy.mp3")  

# Simulate a random jumpscare  
jumpscare_manager.random_jumpscare()