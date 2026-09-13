[app]

# (str) Title of your application
title = OSINT WORLD

# (str) Package name
package.name = osintworld

# (str) Package domain (needed for android)
package.domain = org.osintworld

# (str) Source code where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas

# (list) Source directories to exclude
source.exclude_dirs = bin,.buildozer,.git,__pycache__

# (str) Application version
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application is fullscreen
fullscreen = 0

# (str) Android API to use
android.api = 34

# (str) Android NDK version
android.ndk = 25b

# (str) Minimum Android API
android.minapi = 21

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (str) Log level
log_level = 2

# (str) Android app activity class
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Android app theme
android.presplash_color = #101318

# (str) Android app icon
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]

# (str) Warn if buildozer is run as root
warn_on_root = 1
