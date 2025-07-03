[app]

title = Bill App
package.name = billapp
package.domain = org.fatech

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy==2.3.1,kivymd,materialyoucolor,pillow,cython

requirements.source.kivy = https://github.com/kivy/kivy/archive/2.3.1.zip
requirements.source.kivymd = https://github.com/kivymd/KivyMD/archive/1.1.0.zip
requirements.source.libffi = https://github.com/libffi/libffi/archive/v3.4.6.zip

orientation = portrait
fullscreen = 0

android.permissions = android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=28,android.permission.READ_EXTERNAL_STORAGE

android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a
android.ndk = 25b
android.ndk_path = /usr/local/lib/android/sdk/ndk/25b
android.sdk_path = /usr/local/lib/android/sdk
android.api = 31
android.minapi = 21

android.logcat_filters = *:S python:D

log_level = 2
warn_on_root = 1
