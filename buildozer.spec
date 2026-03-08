[app]
# (Dastur nomi)
title = SOSApp
package.name = sosapp
package.domain = org.codexcoder

# Manba fayllar
source.dir = .
source.include_exts = py,kv,png,jpg,atlas

# Versiya
version = 1.0

# Python kutubxonalari
requirements = python3,kivy,plyer

# Displey sozlamalari
orientation = portrait
fullscreen = 0

# Ikonka va presplash (ixtiyoriy, yo‘q bo‘lsa default ishlaydi)
icon.filename = icon.png
presplash.filename = presplash.png

# Android ruxsatnomalari
android.permissions = SEND_SMS,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CALL_PHONE,INTERNET

# Debug / Release
android.debug = 1

# --------------------
[buildozer]
log_level = 2
warn_on_root = 1

# APK build joyi
bin_dir = bin

# Virtualenv va boshqa sozlamalar avtomatik
