Summary:	Gizmod is an advanced input handler for keyboards, mice, and joypads
Name: 		gizmod
Version:	3.5
Release:	5
Group:		System/Configuration/Hardware 
License:	Apache License V2.0
URL:		http://gizmod.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		gizmod-3.5-mdv-fix_build_errors.patch
Patch1:		gizmod-3.5-mdv-fix_cmake_dependencies.patch
Patch2:		gizmod-3.5_stdlib.patch

BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libvisual-0.4)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(x11)

%description
Gizmod is an input handler that binds to a specific device and can
adapt to various situations so you can have one meaning in, say, AmaroK
and another in MPlayer, etc. It even includes remote control so you can
send input events to another machine with a locally connected device.

%prep
%setup -q
%autopatch -p1

%build
export CXXFLAGS="%optflags -DBOOST_FILESYSTEM_VERSION=2"
%cmake
%make

%install
%makeinstall_std -C build

rm -fr %buildroot%_libdir/*.so %buildroot%_includedir

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS NOTICE README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/libvisual-0.4
%{_sysconfdir}/*
