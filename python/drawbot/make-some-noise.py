import tnbits.floqmodel

font("InputSansCompressed-Black")
#fontWeight('Black')
fontSize(256)
text(" MAKE\nS0ME\nN0ISE", (100, 100))
f = installedFonts()
for font in f:
    if 'Input' in font:
        print font