# -*- coding: utf-8 -*-

from sys import path
from radish import before, after

path.append('../calculator/calc')
from calculator import Calculator

@before.each_scenario
def init_calculator(scenario):
    scenario.context.calculator = Calculator(caching=True)

@after.each_scenario
def destory_calculator(scenario):
    del scenario.context.calculator
