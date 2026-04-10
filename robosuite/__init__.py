from robosuite.environments.base import make

# Manipulation environments
from robosuite.environments.manipulation.lift import Lift
from robosuite.environments.manipulation.stack import Stack
from robosuite.environments.manipulation.nut_assembly import NutAssembly
from robosuite.environments.manipulation.pick_place import PickPlace
from robosuite.environments.manipulation.door import Door
from robosuite.environments.manipulation.wipe import Wipe
from robosuite.environments.manipulation.tool_hang import ToolHang
from robosuite.environments.manipulation.two_arm_lift import TwoArmLift
from robosuite.environments.manipulation.two_arm_peg_in_hole import TwoArmPegInHole
from robosuite.environments.manipulation.two_arm_handover import TwoArmHandover
from robosuite.environments.manipulation.two_arm_transport import TwoArmTransport

from robosuite.environments import ALL_ENVIRONMENTS
from robosuite.controllers import (
    ALL_PART_CONTROLLERS,
    load_part_controller_config,
    ALL_COMPOSITE_CONTROLLERS,
    load_composite_controller_config,
)

# Compatibility shim for robosuite 1.4.0 API used by libero.
# In 1.4.0, load_controller_config returned a flat part-controller dict.
# In 1.5.2, the env expects a composite controller config:
#   {"type": "BASIC", "body_parts": {"arms": {"right": <part_config>}}}
# We wrap the part config so libero's call sites work unchanged.
def load_controller_config(custom_fpath=None, default_controller=None):
    part_cfg = load_part_controller_config(
        custom_fpath=custom_fpath, default_controller=default_controller
    )
    # body_parts uses flattened arm keys (not nested under "arms") to match
    # what load_composite_controller_config returns after its flattening step.
    part_cfg.setdefault("gripper", {"type": "GRIP"})
    return {
        "type": "BASIC",
        "body_parts": {
            "right": part_cfg,
        },
    }

ALL_CONTROLLERS = ALL_PART_CONTROLLERS
from robosuite.robots import ALL_ROBOTS
from robosuite.models.grippers import ALL_GRIPPERS
from robosuite.utils.log_utils import ROBOSUITE_DEFAULT_LOGGER

try:
    import robosuite_models
except:
    ROBOSUITE_DEFAULT_LOGGER.warning(
        "Could not import robosuite_models. Some robots may not be available. "
        "If you want to use these robots, please install robosuite_models from "
        "source (https://github.com/ARISE-Initiative/robosuite_models) or through pip install."
    )

try:
    from robosuite.examples.third_party_controller.mink_controller import WholeBodyMinkIK

except:
    ROBOSUITE_DEFAULT_LOGGER.warning(
        "Could not load the mink-based whole-body IK. Make sure you install related import properly (e.g. pip install mink==0.0.5), otherwise you will not be able to use the default IK controller setting for GR1 robot."
    )

__version__ = "1.5.2"
__logo__ = """
      ;     /        ,--.
     ["]   ["]  ,<  |__**|
    /[_]\  [~]\/    |//  |
     ] [   OOO      /o|__|
"""
