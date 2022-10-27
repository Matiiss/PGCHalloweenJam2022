#version 300 es

precision mediump float;
uniform sampler2D Texture;
uniform sampler2D Overlay;
in vec2 v_text;

vec2 center = vec2(0.5, 0.5);

out vec3 f_color;
void main() {
  vec4 color;
  vec2 text_size = vec2(textureSize(Texture, 0));
  vec2 pixel = vec2(1.0, 1.0) / text_size;

  vec2 diff = v_text - center;
  diff.y *= text_size.y / text_size.x;
  float dist = length(diff);
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
  vec4 overlay_color = texture(Overlay, v_text);
  f_color = (1.0 - overlay_color.a) * color.rgb + overlay_color.a * overlay_color.rgb;
}
