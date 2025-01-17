# atelier-client

A comprehensive toolkit for state-of-the-art AI image generation compatible with all devices.

## Installation

```bash
pip install atelier-client
```

## Basic Usage

```python
from atelier_client import AtelierClient

# Initialize the client
client = AtelierClient(
    gradio=False,      # Enable/disable Gradio integration
    timeout=180,       # Request timeout in seconds
    log_on=True,       # Enable logging
    save_to="outputs", # Output directory
    save_as="webp"     # Output format (png/webp/jpg/pil)
)

# Generate an image
result = client.image_generate(
    prompt="a beautiful landscape"
)
```

## Features

### Image Generation

```python
# High quality image generation
image_generate(
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    model_name="flux-turbo",   # Optional: Model to use
    image_size="1:1",         # Optional: Output image size ratio
    lora_svi=None,            # Optional: LoRA SVI preset
    lora_flux=None,            # Optional: LoRA Flux preset
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Generate variations of an input image
image_variation(
    image,                    # Required: Source image
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    model_name="flux-turbo",   # Optional: Model to use
    image_size="1:1",         # Optional: Output image size ratio
    strength=None,            # Optional: Variation strength
    lora_svi=None,            # Optional: LoRA SVI preset
    lora_flux=None,            # Optional: LoRA Flux preset
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Instant image generation
realtime_generate(
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    image_size="1:1",         # Optional: Output image size ratio
    lora_rt=None,             # Optional: LoRA RT preset
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Instant drawing canvas
realtime_canvas(
    image,                    # Required: Source image
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    lora_rt=None,             # Optional: LoRA RT preset
    strength=0.9,             # Optional: Creativity level
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)
```

### Image Editing

```python
# Generative image upscaler
image_enhance(
    image,                    # Required: Source image
    prompt=None,              # Optional: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    creativity=0.3,           # Optional: Creativity level
    resemblance=1,            # Optional: Resemblance level
    hdr=0,                    # Optional: HDR strength
    style_name=None           # Optional: Style preset
)

# Standard image upscaling
image_upscale(image)          # Required: Source image

# Inpaint elements into an image
image_inpaint(
    image,                    # Required: Source image
    mask,                     # Required: Mask image
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    strength=0.5,             # Optional: Inpainting strength
    cfg=9.0,                  # Optional: Prompt guidance scale
    style_name=None           # Optional: Style preset
)

# Remove elements from an image
image_erase(
    image,                    # Required: Source image
    mask,                     # Required: Mask image
    cfg=9.0                   # Optional: Prompt guidance scale
)

# Remove background from images
image_bgremove(image)         # Required: Source image

# Extend images beyond their borders
image_outpaint(
    image,                    # Required: Source image
    image_size="16:9"         # Optional: Output image size ratio
)
```

### Style & Control

```python
# Generate images using structural guidance
image_structure(
    image,                    # Required: Source image
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    model_name="svi-turbo",   # Optional: Model to use
    image_size="1:1",         # Optional: Output image size ratio
    strength=None,            # Optional: Guidance strength
    lora_svi=None,            # Optional: LoRA SVI preset
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Generate images using facial guidance
image_facial(
    image,                    # Required: Source image
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    model_name="svi-turbo",   # Optional: Model to use
    image_size="1:1",         # Optional: Output image size ratio
    strength=None,            # Optional: Guidance strength
    lora_svi=None,            # Optional: LoRA SVI preset
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Generate images using style guidance
image_style(
    image,                    # Required: Source image
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    model_name="svi-turbo",   # Optional: Model to use
    image_size="1:1",         # Optional: Output image size ratio
    strength=None,            # Optional: Style strength
    lora_svi=None,            # Optional: LoRA SVI preset
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Control image generation with various methods
image_controlnet(
    image,                    # Required: Source image
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    model_name="sd-toon",     # Optional: Model to use
    controlnet="scribble",    # Optional: Control type
    strength=70,              # Optional: Control strength
    cfg=9.0,                  # Optional: Prompt guidance scale
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Consistent image generation with style
image_consistent(
    prompt,                   # Required: Text prompt
    face_image,               # Required: Face reference
    style_image,              # Required: Style reference
    negative_prompt=None,     # Optional: Negative prompt
    image_size="1:1",         # Optional: Output image size ratio
    face_strength=1.2,        # Optional: Face consistency
    style_strength=0.7,       # Optional: Style strength
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)
```

### Face Enhancement

```python
# Consistent image generation with InstantID
face_identity(
    image,                    # Required: Face reference
    prompt,                   # Required: Text prompt
    negative_prompt=None,     # Optional: Negative prompt
    image_size="1:1",         # Optional: Output image size ratio
    strength=1.0,             # Optional: Face strength
    image_seed=None,          # Optional: Generation seed
    style_name=None           # Optional: Style preset
)

# Restore faces using GFPGAN
face_gfpgan(
    image,                    # Required: Source image
    model_version="1.3"       # Optional: Model version
)

# Restore faces using CodeFormer
face_codeformer(image)        # Required: Source image
```

### Image Analysis

```python
# Generate descriptive captions
image_caption(image)          # Required: Source image

# Convert images to prompts
image_prompt(image)           # Required: Source image
```

## Configuration Options

### Output Formats

- `webp` (default) - High quality, small file size
- `png` - Lossless quality
- `jpg` - Standard compressed format
- `pil` - Returns PIL Image object

### Available Lists

We provide several class methods to retrieve available options for different features. Here's how to access them:

```python
from atelier_client import AtelierClient
client = AtelierClient()

# Models and Sizes
models = client.list_atr_models                 # Base image generation models
sizes = client.list_atr_size                    # Available image size ratios

# Style Options
styles = client.list_sty_styles                 # Style presets
guidance_models = client.list_atr_models_guide  # Guidance-specific models
guidance_types = client.list_atr_g_types        # Types of guidance available

# LoRA Models
lora_models = {
    'svi': client.list_atr_lora_svi,            # SVI-compatible LoRA models
    'flux': client.list_atr_lora_flux,            # Flux-compatible LoRA models
    'rt': client.list_atr_lora_rt               # Realtime-compatible LoRA models
}

# Other Models
controlnets = client.list_atr_controlnets       # Available ControlNet models
gfpgan_models = client.list_atr_gfpgan          # GFPGAN face restoration models
remix_models = client.list_atr_remix_model      # Remix-compatible models

# Example usage:
print(f"Available image models: {models}")
print(f"Available image sizes: {sizes}")
print(f"Available style presets: {styles}")
```

These lists can be used to validate inputs and explore available options for different generation methods. All methods return lists of strings representing the valid options for each category.

## Error Handling

The client includes comprehensive error handling and logging:
- Network connectivity checks
- Input validation
- NSFW content detection
- Request timeout handling
- Detailed logging (when enabled)

## Requirements

- Python 3.8+
- Internet connection

## License

See [LICENSE](LICENSE) for details.
