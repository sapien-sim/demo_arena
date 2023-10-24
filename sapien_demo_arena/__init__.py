import sapien
from pathlib import Path


class DefaultArena(sapien.Widget):
    def load(self, scene: sapien.Scene):
        scene.set_environment_map(str(Path(__file__).parent / "env.ktx"))
        self.ground = scene.add_ground(0)
        # self.light = scene.add_directional_light([1, 1, -1], [1, 1, 1], True)

    def unload(self, scene: sapien.Scene):
        scene.remove_actor(self.ground)
        # scene.remove_light(self.light)
