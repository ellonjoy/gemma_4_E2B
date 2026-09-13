import flet_camera as fc


cameras = None

def has_human_readable(camera: fc.CameraDescription) -> bool:
    """
    Fungsi untuk memastikan format pembacaan kamera mudah untuk dibaca.
    """

    name = camera.name.strip()
    if not name:
        return False
    if name.startswith("com.apple.avfoundation."):
        return False
    return not (":" in name and "." in name)

def camera_label(camera: fc.CameraDescription) -> str:
    if has_human_readable(camera):
        return camera.name

    direction = camera.lens_direction.value.capitalize()
    lens_map = {
        "wide":"Wide",
        "telephoto":"Telephoto",
        "ultraWide":"Ultra Wide",
        "uknown":"Uknown"
    }
    lens_type = lens_map.get(camera.lens_type.value, camera.lens_type.value)
    return f"{direction} ({lens_type})"

async def get_camera(camera: fc.Camera) -> None:
    global cameras
    cameras = await camera.get_available_cameras()
    seen_labels: dict[str, int] = {}
    for camera in cameras:
        label = camera_label(camera)
        seen_labels[label] = seen_labels.get(label, 0) + 1
        if seen_labels[label] >= 1:
            label = f"{label} {seen_labels[label]}"

async def init_camera(camera: fc.Camera) -> None:
    if not cameras:
        return

    selected_camera = next((c for c in cameras))
    if not selected_camera:
        return

    await camera.initialize(
        description=selected_camera,
        resolution_preset=fc.ResolutionPreset.HIGH,
        enable_audio=False,
        image_format_group=fc.ImageFormatGroup.JPEG
    )

async def take_a_photo(camera: fc.Camera) -> (bytes | None):
    try:
        if not await init_camera(camera):
            data = await camera.take_picture()
            return data
    except RuntimeError:
        return