from django.apps import AppConfig
import random
from .models import *

LANDINGS = [
    "This is the main landing page",
    "Is it Friday yet?",
    "It's so funky and it's low volume... come on, yeah",
    "It's Dean Dart",
    "Todo: Check todos",
    "If only I could be so grossly incandescent",
]

class DashboardConfig(AppConfig):
    name = 'dashboard'

def generateLanding():
    return random.choice(LANDINGS)