%define name	gizmod
%define version	3.5
%define release	%mkrel 4

Name: 		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Gizmod is an advanced input handler for keyboards, mice, and joypads
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		gizmod-3.5-mdv-fix_build_errors.patch
Patch1:		gizmod-3.5-mdv-fix_cmake_dependencies.patch
URL:		http://gizmod.sourceforge.net
Group:		System/Configuration/Hardware 
License:	Apache License V2.0

BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: boost-devel
BuildRequires: libvisual-devel
BuildRequires: alsa-lib-devel
BuildRequires: libx11-devel
BuildRequires: cmake
BuildRequires: python-devel

%description
Gizmod is an input handler that binds to a specific device and can
adapt to various situations so you can have one meaning in, say, AmaroK
and another in MPlayer, etc. It even includes remote control so you can
send input events to another machine with a locally connected device.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CXXFLAGS="%optflags -DBOOST_FILESYSTEM_VERSION=2"
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

rm -fr %buildroot%_libdir/*.so %buildroot%_includedir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS NOTICE README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/libvisual-0.4
%{_sysconfdir}/*
