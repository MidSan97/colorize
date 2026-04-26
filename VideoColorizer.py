from colorize import device
from colorize .device_id import DeviceId
device.set(device = DeviceId.GPU0)

from colorize .visualize import *
plt.style.use('dark_background')
import warnings
warnings.filterwarnings("ignore", category = UserWarning, message = ".*?Your .*? set is empty.*?")

colorizer = get_video_colorizer()

render_factor = 25
source_url = 'https://twitter.com/silentmoviegifs/status/1116751583386034176'
file_name = 'DogShy1926'
file_name_ext = file_name + '.mp4'
result_path = None

if source_url is not None:
    result_path = colorizer.colorize_from_url(source_url, file_name_ext, render_factor = render_factor)
else:
    result_path = colorizer.colorize_from_file_name(file_name_ext, render_factor = render_factor)