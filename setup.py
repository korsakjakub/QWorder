from distutils.core import setup
setup(
  name = 'qworder',
  packages = ['QWORDER'],   # Chose the same as "name"
  version = '0.1',
  license='GPL3.0',
  description = 'QWorder simplifies strings representing sequences of quantum gates',
  author = 'Jakub Korsak',
  author_email = 'jakub.korsak@protonmail.com',
  url = 'https://github.com/korsakjakub/qworder',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['QUANTUM', 'COMPUTING', 'GATESTRINGS', 'SIMPLIFIER', 'PAULI', 'MATRIX', 'HADAMARD'],
  install_requires=[
          'csv',
          'os',
          'numpy',
          'typing',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
  ],
)
