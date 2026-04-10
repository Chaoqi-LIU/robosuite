"""
Compatibility shim for libero 0.1.1 (written against robosuite 1.4.0).
single_arm_env.py was removed in robosuite 1.5.2; this restores it.
"""

from robosuite.environments.manipulation.manipulation_env import ManipulationEnv


class SingleArmEnv(ManipulationEnv):
    """
    Single-arm manipulation environment. Bridges the robosuite 1.4.0 API
    (mount_types, no lite_physics/seed/load_model_on_init) to 1.5.2's
    ManipulationEnv constructor.
    """

    def __init__(
        self,
        robots,
        env_configuration="default",
        controller_configs=None,
        mount_types="default",
        gripper_types="default",
        initialization_noise=None,
        use_camera_obs=True,
        has_renderer=False,
        has_offscreen_renderer=True,
        render_camera="frontview",
        render_collision_mesh=False,
        render_visual_mesh=True,
        render_gpu_device_id=-1,
        control_freq=20,
        horizon=1000,
        ignore_done=False,
        hard_reset=True,
        camera_names="agentview",
        camera_heights=256,
        camera_widths=256,
        camera_depths=False,
        camera_segmentations=None,
        renderer="mujoco",
        renderer_config=None,
        **kwargs,
    ):
        super().__init__(
            robots=robots,
            env_configuration=env_configuration,
            controller_configs=controller_configs,
            base_types=mount_types,  # renamed mount_types -> base_types in 1.5.2
            gripper_types=gripper_types,
            initialization_noise=initialization_noise,
            use_camera_obs=use_camera_obs,
            has_renderer=has_renderer,
            has_offscreen_renderer=has_offscreen_renderer,
            render_camera=render_camera,
            render_collision_mesh=render_collision_mesh,
            render_visual_mesh=render_visual_mesh,
            render_gpu_device_id=render_gpu_device_id,
            control_freq=control_freq,
            horizon=horizon,
            ignore_done=ignore_done,
            hard_reset=hard_reset,
            camera_names=camera_names,
            camera_heights=camera_heights,
            camera_widths=camera_widths,
            camera_depths=camera_depths,
            camera_segmentations=camera_segmentations,
            renderer=renderer,
            renderer_config=renderer_config,
            **kwargs,
        )

    def _check_robot_configuration(self, robots):
        super()._check_robot_configuration(robots)
        robots = list(robots) if isinstance(robots, (list, tuple)) else [robots]
        assert len(robots) == 1, (
            f"SingleArmEnv expects exactly one robot, got {len(robots)}"
        )
