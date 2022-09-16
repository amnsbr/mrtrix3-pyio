from setuptools import setup, find_packages

setup(name='mrtrix3',
      version='py-0.0.1',
      description='Python package to interface with MRtrix3 file formats.',
      url='http://github.com/dchristiaens/mrtrix3-pyio.git',
      author='Daan Christiaens',
      author_email='daan.christiaens@kcl.ac.uk',
      license='MPL',
      packages=find_packages(),
      install_requires=['numpy'],
      zip_safe=False)

