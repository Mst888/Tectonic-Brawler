# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['scripts\\standalone_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('main.py', '.'), ('cogs', 'cogs'), ('utils', 'utils'), ('requirements.txt', '.'), ('config.json', '.')],
    hiddenimports=['winreg'],
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
    name='TectonicBrawler',
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
    icon=['build_tools\\bot_icon.ico'],
)
