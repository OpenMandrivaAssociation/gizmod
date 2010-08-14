%define name	gizmod
%define version	3.5
%define release	%mkrel 1

Name: 		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Gizmod is an advanced input handler for keyboards, mice, etc...
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
BuildRequires: X11-devel
BuildRequires: cmake
BuildRequires: gcc-c++
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
%cmake
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS NOTICE README TODO
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_sysconfdir}/*

