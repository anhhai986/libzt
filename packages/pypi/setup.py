#!/usr/bin/env python

from setuptools import setup, Extension, Command, Distribution
import glob

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

source_list = ['libzt_wrap.cxx']
source_list.extend(list(glob.glob('data/libzt/src/*.cpp')))
source_list.extend(list(glob.glob('data/zto/node/*.cpp')))
source_list.extend(list(glob.glob('data/zto/osdep/*.cpp')))
source_list.extend(list(glob.glob('data/zto/service/*.cpp')))
source_list.extend(list(glob.glob('data/zto/controller/*.cpp')))

#http_parser_source_list = ['libzt_wrap.cxx']
#http_parser_source_list.extend(list(glob.glob('../../zto/ext/http-parser/*.c')))
#lwip_source_list = ['libzt_wrap.cxx']
#lwip_source_list.extend(list(glob.glob('../../ext/lwip/src/core/*.c')))
#lwip_source_list.extend(list(glob.glob('../../ext/lwip/src/core/ipv4/*.c')))
#lwip_source_list.extend(list(glob.glob('../../ext/lwip/src/core/ipv6/*.c')))

source_list = list(set(source_list)-set(
	['data/zto/osdep/LinuxEthernetTap.cpp','data/zto/osdep/BSDEthernetTap.cpp','data/zto/osdep/OSXEthernetTap.cpp', 'data/zto/osdep/WindowsEthernetTap.cpp']))

#lwip_module = Extension('lwip',
#					extra_compile_args=['-DZT_SDK'],
#					extra_link_args=[],
#					sources=lwip_source_list,
#					include_dirs=['../include',
#							'../../include',
#							'../../ext/lwip/src/include',
#							'../../ext/lwip-contrib/ports/unix/include',]                           
#					)

#http_parser_module = Extension('http_parser',
#					extra_compile_args=[],
#					extra_link_args=[],
#					sources=http_parser_source_list,
#					)

libzt_module = Extension('libzt',
					extra_compile_args=['-std=c++11', '-DZT_SDK', '-DZT_SOFTWARE_UPDATE_DEFAULT=\"disable\"'],
					extra_link_args=['-L.','-llwip','-lhttp'],
					sources=source_list,
					include_dirs=['data/libzt/include',
							'data/libzt/ext/lwip/src/include',
							'data/libzt/ext/lwip-contrib/ports/unix/include',
							'data/zto/include',
							'data/zto/node',
							'data/zto/service',
							'data/zto/osdep',
							'data/zto/controller']                           
					)

setup(    
	include_package_data=True,
    distclass=BinaryDistribution,
	ext_modules = [libzt_module],
	py_modules = ['libzt'],
	name = 'libzt',
	packages = ['libzt'],
	version = '1.1.5a19',
	description = 'ZeroTier, in library form.',
	long_description = 'Encrypted P2P networks between your applications',
	author = 'ZeroTier, Inc.',
	author_email = 'joseph@zerotier.com',
	url = 'https://github.com/zerotier/libzt',
	license='GPLv3',
	download_url = 'https://github.com/zerotier/libzt/archive/1.1.5.tar.gz',
	keywords = 'zerotier sdwan sdn virtual network socket p2p peer-to-peer',
	classifiers = ['Development Status :: 3 - Alpha',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Science/Research',
		'Intended Audience :: System Administrators',
		'Intended Audience :: Telecommunications Industry',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Developers',
		'License :: Free for non-commercial use',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: iOS',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: BSD',
		'Operating System :: Unix',
		'Programming Language :: C++',
		'Programming Language :: C',
		'Programming Language :: Python',
		'Topic :: Internet',
		'Topic :: Security :: Cryptography',
		'Topic :: System :: Networking'
	],
)