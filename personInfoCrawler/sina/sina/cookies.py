#!/usr/bin/env python
# -*- encoding:utf-8 -*-


'''

17164008122----ywyrkc5863
17164006073----dxghm2884
17164007936----mqcbx3386
17164000731----qczfe3235
17164009268----wixahe3486

17164003891----dqhei5929
17164000279----ttviht9781
17164000117----xllnd8923
17164006676----diygiq6297s
17164001396----xblhs2669

'''



# 10个cookie
cookieList = [

	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2oSDeRhGeBN7VUX9CnEyT2IHXVURHZarDV6PUJbkdANLVnBkW1Fs_kmSGHlr_JDjAAWqec2nQs7jw..; SUHB=0IIVDDeIQj87Ap; SSOLoginState=1505696324; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D20000174%26lfid%3Dhotword',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2oqDeRhGeBN7VUX9CnEyTWIHXVURHZirDV6PUJbkdANLWnnkW10OSzYWD9tSFdOWUwgbWIirgnfEA..; SUHB=0M2Fe6YD-DRyjB; SSOLoginState=1505696378; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2rPDeRhGeBN7VUX9CnEyTSIHXVURHaHrDV6PUJbkdANLVDykW0daWsvy1TbNWjf4_DHYdz1Wu6r_w..; SUHB=0Ela0ymcOl3n1p; SSOLoginState=1505696415; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2qHDeRhGeBN7VUX9CnEyD6IHXVURHbPrDV6PUJbkdANLVb5kW0VrfS1CAwL5fIMPVhcFVSlVC8XmA..; SUHB=0V5l9BrHDMNntz; SSOLoginState=1505696471; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D20000174%26lfid%3Dhotword%26uicode%3D20000174',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2qoDeRhGeBN7VUX9CnEyD2IHXVURHbgrDV6PUJbkdANLWPVkW0g4UkVMEs_e_yMes_ClbgZ4Wwgag..; SUHB=02Mv3MEmbJ27CD; SSOLoginState=1505696506; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',

	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2twDeRhGeBN7VUX9CnEyTiIHXVURHU4rDV6PUJbkdANLWzFkW1OWN95x8G9Zcv8G-RQpRAOGG913g..; SUHB=0k1Cn3WtdbXopH; SSOLoginState=1505696544; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2tuDeRhGeBN7VYS9CbFzDWIHXVURHUmrDV6PUJbkdAKLWntkW0zdEov_hb6CWP15wCFA8o2YwUBOw..; SUHB=02Mv3MEmbJ27CD; SSOLoginState=1505696574; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2szDeRhGeBN7VUX9CnEyT6IHXVURHV7rDV6PUJbkdAKLU_YkW02kPERaa2Qd9MxOCnOB6O1Brq0dA..; SUHB=0tKqQ8-EdqrnEz; SSOLoginState=1505696612; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2vXDeRhGeBN7VAT8ybPyT-IHXVURHWfrDV6PUJbkdANLW3BkW1nAzw5_9Isk9HTmNM9zg6IU5tLBg..; SUHB=0XDlBlnQRiUL6v; SSOLoginState=1505696648; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',
	'_T_WM=cd885c41afeaf626b370b96cf5f45dd6; SCF=Avnrt-tcucu14NU38tbzq4UOchct24SyTsTp5cyPImAvNriCJmu0HXEUAtxLShmZGNlb9fpGQOeTQndzTTXU5Yg.; ALF=1508039443; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_ZQwDImgkYj2LH7wFvW_-5JpX5KzhUgL.Fo-7eK.p1Kz71h22dJLoIfQLxKBLB.zL12-LxK.L1-zLBoqLxK-LB.eL1h5LxK-LBKML12zLxKML1-2L1hBLxKMLBKnL12zLxK-LB.2L12qLxK-L1K2L1KnLxKML1KBL1-qLxKqLBoBLB.zt; SUB=_2A250u2v8DeRhGeBN7VAT8ybPyTiIHXVURHW0rDV6PUJbkdANLVbmkW0FFJYm63GxHsIHz1MrUQ4nQlmfow..; SUHB=0YhRH5efQuacO-; SSOLoginState=1505696684; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword',

]