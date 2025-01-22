# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['YWLTL.py'],
    pathex=[],
    binaries=[],
    datas=[('SpinBox.py', '.'), ('CurseForgeImplementations.py', '.'), ('./OnlineModpacksSupport.py/', '.'), ('./RMMUD/', '.'), ('./download-mods.py', '.'), ('requirements.txt', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='YWLTL',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

#PyInstaller spec file
