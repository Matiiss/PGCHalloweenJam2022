#version 300 es

precision mediump float;
uniform sampler2D Texture;
in vec2 v_text;

vec2 center = vec2(0.5, 0.5);

out vec4 f_color;
void main() {
  vec2 text_size = vec2(textureSize(Texture, 0));
  vec2 pixel = vec2(1.0, 1.0) / text_size;

  vec2 diff = v_text - center;
  diff.y *= text_size.y / text_size.x;
  float dist = length(diff);
  vec4 color;
  float kernel = round(max(dist / 0.5 - 0.2, 0.0) * 10.0);
  if (mod(kernel, 2.0) == 1.0) {
    kernel -= 1.0;
  }
  for (float y = -kernel / 2.0; y <= kernel / 2.0; y++) {
    for (float x = -kernel / 2.0; x <= kernel / 2.0; x++) {
        color += texture(Texture, v_text + pixel * vec2(x, y));
    }
  }
  color /= vec4(pow(kernel + 1.0, 2.0));
//  color /= kernel;
  f_color = color;
}
