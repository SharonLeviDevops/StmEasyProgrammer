# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Stm32EasyProgrammer/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Stm32EasyProgrammer/1.png', '.'), ('C:/Stm32EasyProgrammer/2.png', '.'), ('C:/Stm32EasyProgrammer/3.png', '.'), ('C:/Stm32EasyProgrammer/4.png', '.'), ('C:/Stm32EasyProgrammer/5.png', '.'), ('C:/Stm32EasyProgrammer/6.png', '.'), ('C:/Stm32EasyProgrammer/7.png', '.'), ('C:/Stm32EasyProgrammer/8.png', '.'), ('C:/Stm32EasyProgrammer/22.png', '.'), ('C:/Stm32EasyProgrammer/original_file.bat', '.'), ('C:/Stm32EasyProgrammer/test.bat', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Stm32EasyProgrammer\\icon.ico',
)
