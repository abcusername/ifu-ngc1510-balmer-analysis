from astropy.io import fits
import numpy as np

fits_path = r"C:\Users\30126\Desktop\吴鑫星兰州大学\项目\西湖大学 积分视场光谱观测\NGC1510_DATACUBE.fits"

hdu = fits.open(fits_path)
header = hdu[0].header
data = hdu[0].data
var = hdu[1].data

print("========== header 关键信息 ==========")
print("NAXIS  =", header["NAXIS"])
print("NAXIS1 =", header["NAXIS1"])
print("NAXIS2 =", header["NAXIS2"])
print("NAXIS3 =", header["NAXIS3"])
print("CRVAL3 =", header["CRVAL3"])
print("CDELT3 =", header["CDELT3"])

# 波长轴：log10(lambda)
log_wave = header['CRVAL3'] + np.arange(header['NAXIS3']) * header['CDELT3']
wave = 10**log_wave

print("\n========== 波长信息 ==========")
print("wave 长度 =", len(wave))
print("前10个波长 =", wave[:10])
print("最后10个波长 =", wave[-10:])

hdu.close()