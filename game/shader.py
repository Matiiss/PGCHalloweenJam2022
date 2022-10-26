import struct

import pygame
import moderngl


class ShaderDisplay(pygame.Surface):
    def __init__(self, size, display_size, vertex_shader, fragment_shader):
        super().__init__(size, depth=24)
        pygame.display.set_mode(display_size, flags=pygame.OPENGL | pygame.DOUBLEBUF)

        self.ctx = moderngl.create_context()

        texture_coordinates = [0, 1, 1, 1, 0, 0, 1, 0]
        world_coordinates = [-1, -1, 1, -1, -1, 1, 1, 1]
        render_indices = [0, 1, 2, 1, 2, 3]

        prog = self.ctx.program(
            vertex_shader=open(f"shaders/{vertex_shader}").read(),
            fragment_shader=open(f"shaders/{fragment_shader}").read(),
        )

        self.texture = self.ctx.texture(size, 3, pygame.image.tostring(self, "RGB", 1))  # NOQA
        self.texture.repeat_x = False
        self.texture.repeat_y = False
        self.texture.filter = (moderngl.NEAREST, moderngl.NEAREST)

        vbo = self.ctx.buffer(struct.pack('8f', *world_coordinates))
        uvmap = self.ctx.buffer(struct.pack('8f', *texture_coordinates))
        ibo = self.ctx.buffer(struct.pack('6I', *render_indices))

        vao_content = [
            (vbo, '2f', 'vert'),
            (uvmap, '2f', 'in_text')
        ]

        self.vao = self.ctx.vertex_array(prog, vao_content, ibo)

    def update(self):
        texture_data = self.get_view('1')
        self.texture.write(texture_data)
        self.ctx.clear(14 / 255, 40 / 255, 66 / 255)
        self.texture.use()
        self.vao.render()
        pygame.display.flip()
