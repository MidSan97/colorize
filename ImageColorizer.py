from colorize import device
from colorize .device_id import DeviceId
from PIL import Image
device.set(device = DeviceId.GPU0)

from colorize .visualize import *
plt.style.use('dark_background')
torch.backends.cudnn.benchmark = True
import warnings
warnings.filterwarnings("ignore", category = UserWarning, message = ".*?Your .*? set is empty.*?")

colorizer = get_image_colorizer(artistic = True)

render_factor = 35
source_url = None
source_path = 'test_images/image.jpeg'
result_path = None

if source_url is not None:
    result_path = colorizer.plot_transformed_image_from_url(url = source_url, path = source_path, render_factor = render_factor, compare = True)
else:
    result_path = colorizer.plot_transformed_image(path = source_path, render_factor = render_factor, compare = True)