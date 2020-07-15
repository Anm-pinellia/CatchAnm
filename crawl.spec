# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['crawl.py'],
             pathex=['E:\\CatchAnm'],
             binaries=[],
             datas=[('D:\\Program Files\\python374\\Lib\\site-packages\\scrapy\\mime.types','scrapy'),
	('D:\\Program Files\\python374\\Lib\\site-packages\\scrapy\\VERSION','scrapy'),
	('.','.' )],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='crawl',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
