import sys

"""
Setup script for BAMQC  -- Comprehensive QC package for NGS data alignment file
Copyright (c) 2015 Ying Jin <yjin@cshl.edu>
This code is free software;you can redistribute it and/or modify it
under the terms of the Artistic License (see the file COPYING included
with the distribution).
"""

if sys.version_info[0] != 2 or sys.version_info[1] < 7:
	print >> sys.stderr, "ERROR: RSeQC requires Python 2.7"
	sys.exit()

#from distutils.core import setup
#from distutils.extension import Extension

from setuptools import setup, Extension
#from distutils.core import setup
from Cython.Build import cythonize
#from distutils.extension import Extension

#from distutils.core import Command

# Use build_ext from Cython
command_classes = {}

# Use build_ext from Cython if found
try:
    import Cython.Distutils
    command_classes['build_ext'] = Cython.Distutils.build_ext
except:
    pass

#sourcefiles = ['./src/PyGeneFeatures.pyx', './src/IntervalTree.cpp', './src/GeneFeatures.cpp']

#extensions = [Extension("PyGeneFeatures", sourcefiles)]


setup(name = "BAMQC",
      version = "0.5",
      description = 'Quality control tools for NGS alignment file',
      keywords='Quality control BAM file',
      packages = ['libBAMQC'],
#     package_data={'libBAMQC': ['PyGeneFeatures.so','libGeneFeatures.so']},
      install_requires=['argparse','pysam>=0.8'],
      scripts = ["BAMqc_mp"],
      author = "Ying Jin",
      author_email ="yjin@cshl.edu",
      license='GPLv3',
      platforms = ['Linux','MacOS'],
      url='http://hammelllab.labsites.cshl.edu/software#BAMQC',
      zip_safe = False,
      include_package_data=True,
      cmdclass=command_classes,
      #ext_modules = cythonize(extensions)
      ext_modules = cythonize([Extension( "PyGeneFeatures",
                              sources = [ "src/PyGeneFeatures.cpp","src/IntervalTree.cpp","src/GeneFeatures.cpp", "src/rRNA.cpp"],
                              language="c++",
                              extra_compile_args=["-std=c++11"],
                              extra_link_args=["-std=c++11"],
                              #libraries = ["GeneFeatures"],
                              #library_dirs = ["./src"],
                              #"src/IntervalTree.cpp","src/GeneFeatures.cpp"],
                              include_dirs=["src"])]),
      #                         "src/IntervalTree.cpp",
      #                         "src/GeneFeatures.cpp"])]),'''
      )

