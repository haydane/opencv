__doc__ = 'Module to handle converting and subsetting TrueType fonts to Postscript Type 3, Postscript Type 42 and Pdf Type 3 fonts.'
__file__ = '/usr/lib/python3/dist-packages/matplotlib/ttconv.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'matplotlib.ttconv'
__package__ = 'matplotlib'
def convert_ttf_to_ps(filename, output, fonttype, glyph_ids):
    'convert_ttf_to_ps(filename, output, fonttype, glyph_ids)\n\nConverts the Truetype font into a Type 3 or Type 42 Postscript font, optionally subsetting the font to only the desired set of characters.\n\nfilename is the path to a TTF font file.\noutput is a Python file-like object with a write method that the Postscript font data will be written to.\nfonttype may be either 3 or 42.  Type 3 is a "raw Postscript" font. Type 42 is an embedded Truetype font.  Glyph subsetting is not supported for Type 42 fonts.\nglyph_ids (optional) is a list of glyph ids (integers) to keep when subsetting to a Type 3 font.  If glyph_ids is not provided or is None, then all glyphs will be included.  If any of the glyphs specified are composite glyphs, then the component glyphs will also be included.'
    pass

def get_pdf_charprocs(filename, glyph_ids):
    'get_pdf_charprocs(filename, glyph_ids)\n\nGiven a Truetype font file, returns a dictionary containing the PDF Type 3\nrepresentation of its paths.  Useful for subsetting a Truetype font inside\nof a PDF file.\n\nfilename is the path to a TTF font file.\nglyph_ids is a list of the numeric glyph ids to include.\nThe return value is a dictionary where the keys are glyph names and\nthe values are the stream content needed to render that glyph.  This\nis useful to generate the CharProcs dictionary in a PDF Type 3 font.\n'
    pass

