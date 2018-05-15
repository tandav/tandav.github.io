from glob import glob
import os
import sys
import webbrowser

images = []
for image_format in ('jpg', 'png'):
    images.extend(glob('screenshots/*.' + image_format))


img_links = ''
for img in sorted(images, key=lambda x: os.path.getmtime(x)):
    img_links += f'<a href=\'{os.path.basename(img)}\'><img src=\'{os.path.basename(img)}\'></a>\n'


with open('screenshots/index_template.html') as template_html:
    screenshots_html_string = template_html.read()


screenshots_html_string = screenshots_html_string.replace('<!-- screenshots -->', img_links)
with open('screenshots/index.html', 'w') as template_html:
    template_html.write(screenshots_html_string)


if '--quiet' in sys.argv:
    pass
else:
    webbrowser.open('file://' + os.getcwd() + '/screenshots/index.html')
    # os.system('open screenshots/index.html')
