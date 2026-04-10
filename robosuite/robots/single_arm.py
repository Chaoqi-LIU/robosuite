"""
Compatibility shim for libero 0.1.1 (written against robosuite 1.4.0).
SingleArm was removed in robosuite 1.5.2; single-arm robots are now FixedBaseRobot.
"""

from robosuite.robots.fixed_base_robot import FixedBaseRobot

SingleArm = FixedBaseRobot
