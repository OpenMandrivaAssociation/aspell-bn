%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01.1-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Bengali
%define languagecode bn
%define lc_ctype bn_BD

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.01.1.1
Release:	22
Group:		System/Internationalization
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
Url:		https://aspell.net/
License:	GPLv2
BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

%files
%doc Copyright doc/README
%{_libdir}/aspell-%{aspell_ver}/*

