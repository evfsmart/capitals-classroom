from sys import exit
from time import sleep
import random
import capitals_dictionaries
import capitals_test_function
import quick_draw_list
import quick_draw_function
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.first_room()
        last_scene = self.scene_map.next_scene('exit')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Exit(Scene):

    farewell = [
        "Good work today. You can close the shell now.\n",
        "Close the shell now.\n",
        "The Capitals Classroom Game has finished. You can close the shell now.\n"
    ]

    def enter(self):
        print(Exit.farewell[randint(0, len(self.farewell)-1)])
        exit(1)


class FirstRoom(Scene):

    def enter(self):
        print(dedent("""
            Welcome to the classroom.\n""")) ; sleep(1)
        print(dedent("""
            Would you like to study Africa, Asia, Europe, North America, South America, or Oceania? \n""")) ; sleep(1)
        print(dedent("""
            If you can't decide, choose Random \n""")) ; sleep(1)
        print(dedent("""
            If you want a quick draw population quiz, choose Quick Draw \n""")) ; sleep(1)
        print(dedent("""
            If you have had enough for today, type EXIT \n"""))

        action = input("> ")
        action = action.lower()

        if action == "africa":
            return 'africa_test'

        elif action == 'asia':
            return 'asia_test'

        elif action == 'europe':
            return 'europe_test'

        elif action == 'north america':
            return 'north_america_test'

        elif action == 'south america':
            return 'south_america_test'

        elif action == 'oceania':
            return 'oceania_test'

        elif action == "random":
            return 'random_scene'

        elif action == "quick draw":
            return 'quick_draw'

        elif action == "exit":
            return 'exit'

        else:
            print("Please enter Africa, Asia, Europe, North America, South America, or Oceania")
            return 'first_room'

class AfricaTest(Scene):

    def enter(self):
        print(dedent("""
            Name the African capital city:
            """))
        capitals_test_function.african_capitals_test()
        return 'first_room'

class AsiaTest(Scene):

    def enter(self):
        print(dedent("""
            Name the Asian capital city:
            """))
        capitals_test_function.asian_capitals_test()
        return 'first_room'

class EuropeTest(Scene):

    def enter(self):
        print(dedent("""
            Name the European capital city:
            """))
        capitals_test_function.european_capitals_test()
        return 'first_room'

class NorthAmericaTest(Scene):

    def enter(self):
        print(dedent("""
            Name the North American capital city:
            """))
        capitals_test_function.north_american_capitals_test()
        return 'first_room'

class SouthAmericaTest(Scene):

    def enter(self):
        print(dedent("""
            Name the South American capital city:
            """))
        capitals_test_function.south_american_capitals_test()
        return 'first_room'

class OceaniaTest(Scene):

    def enter(self):
        print(dedent("""
            Name the Oceania capital city:
            """))
        capitals_test_function.oceania_capitals_test()
        return 'first_room'

class RandomScene(Scene):

    def enter(self):
        scenes_list = list(Map.continent_scenes.keys())
        variable = random.choice(scenes_list)
        return variable

class QuickDraw(Scene):

    def enter(self):
        quick_draw_function.quick_draw()
        return 'first_room'


class Map(object):

    scenes = {
        'first_room': FirstRoom(),
        'random_scene': RandomScene(),
        'africa_test': AfricaTest(),
        'asia_test': AsiaTest(),
        'europe_test': EuropeTest(),
        'north_america_test': NorthAmericaTest(),
        'south_america_test': SouthAmericaTest(),
        'oceania_test': OceaniaTest(),
        'quick_draw': QuickDraw(),
        'exit': Exit()
    }

    continent_scenes = {
        'africa_test': AfricaTest(),
        'asia_test': AsiaTest(),
        'europe_test': EuropeTest(),
        'north_america_test': NorthAmericaTest(),
        'south_america_test': SouthAmericaTest(),
        'oceania_test': OceaniaTest()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def first_room(self):
        return self.next_scene(self.start_scene)


a_map = Map('first_room')
a_game = Engine(a_map)
a_game.play()
